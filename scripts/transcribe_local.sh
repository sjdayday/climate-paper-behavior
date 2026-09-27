#!/usr/bin/env bash
# Local transcription for protocol v0.2 D4 (recordings without a usable caption track).
# Runs on Steve's Mac. One-time setup:
#   brew install ffmpeg whisper-cpp yt-dlp
# The model is downloaded once to ~/.cache/whisper (about 1.6 GB).
#
# Usage:
#   scripts/transcribe_local.sh <audio-or-video URL | local file> <output path without extension>
# Example:
#   scripts/transcribe_local.sh \
#     "https://web.archive.org/web/20211027173223id_/https://www.heartland.org/sebin/b/d/ECN_Ronan_Connolly_Oct27.mp3" \
#     pilot/connolly-2021/communications/sources/transcripts/CN21_Heartland-podcast_2021-10-27
#
# Output (next to the given path):
#   <out>.txt        plain transcript
#   <out>.vtt        timestamped transcript (for checking quotes against the audio)
#   <out>.meta.json  source, audio SHA-256, tool and model versions, date
# The audio itself is kept in ~/.cache/whisper/audio (not committed), named by its hash.
set -euo pipefail

SRC="${1:?source URL or file}"
OUT="${2:?output path without extension}"
MODEL_NAME="ggml-large-v3-turbo.bin"
CACHE="$HOME/.cache/whisper"
MODEL="$CACHE/$MODEL_NAME"
mkdir -p "$CACHE/audio" "$(dirname "$OUT")"

for t in ffmpeg whisper-cli shasum; do
  command -v "$t" >/dev/null || { echo "missing: $t (brew install ffmpeg whisper-cpp)"; exit 1; }
done

if [ ! -f "$MODEL" ]; then
  echo "Downloading model $MODEL_NAME ..."
  curl -L --fail -o "$MODEL" "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/$MODEL_NAME"
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# 1. Get the audio
case "$SRC" in
  *youtube.com/*|*youtu.be/*)
    command -v yt-dlp >/dev/null || { echo "missing: yt-dlp (brew install yt-dlp)"; exit 1; }
    yt-dlp -q -x --audio-format m4a -o "$TMP/src.%(ext)s" "$SRC"
    RAW="$(ls "$TMP"/src.*)"; METHOD="yt-dlp $(yt-dlp --version)";;
  http*)
    curl -L --fail -s -o "$TMP/src.bin" "$SRC"; RAW="$TMP/src.bin"; METHOD="curl";;
  *)
    RAW="$SRC"; METHOD="local file";;
esac

SHA="$(shasum -a 256 "$RAW" | cut -d' ' -f1)"
BYTES="$(wc -c < "$RAW" | tr -d ' ')"
cp -n "$RAW" "$CACHE/audio/$SHA.${RAW##*.}" || true

# 2. Convert to 16 kHz mono WAV and transcribe
ffmpeg -loglevel error -y -i "$RAW" -ar 16000 -ac 1 -c:a pcm_s16le "$TMP/a.wav"
DUR="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$TMP/a.wav")"
whisper-cli -m "$MODEL" -f "$TMP/a.wav" -l auto -otxt -ovtt -of "$OUT" >/dev/null 2>"$TMP/log" \
  || { cat "$TMP/log"; exit 1; }

WVER="$(brew list --versions whisper-cpp 2>/dev/null || echo whisper-cpp-unknown)"
MSHA="$(shasum -a 256 "$MODEL" | cut -d' ' -f1)"
cat > "$OUT.meta.json" <<EOF
{
  "source": "$SRC",
  "retrieval": "$METHOD",
  "audio_sha256": "$SHA",
  "audio_bytes": $BYTES,
  "duration_s": $DUR,
  "asr_tool": "$WVER",
  "asr_model": "$MODEL_NAME",
  "asr_model_sha256": "$MSHA",
  "language": "auto",
  "transcribed": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "flags": ["ASR", "quotes to be hand-checked against audio before scoring (protocol v0.2 D4)"]
}
EOF
echo "Wrote $OUT.txt, $OUT.vtt, $OUT.meta.json (audio sha256 $SHA)"
