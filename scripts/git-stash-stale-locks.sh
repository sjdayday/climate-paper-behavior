#!/usr/bin/env bash
# Move leftover git lock/temp files into .git/_stale-locks/<timestamp>/ instead of
# deleting them (Claude sessions on this computer cannot delete files without a
# per-session approval, but can move them). Then report the stash size.
#
# Usage:
#   scripts/git-stash-stale-locks.sh          # move only files older than 60 s
#   scripts/git-stash-stale-locks.sh --now    # right after Claude's own git command, same shell call
#   scripts/git-stash-stale-locks.sh --report # report stash size only, move nothing
#
# The age check keeps it from touching a lock held by a git command you are
# running at the same moment on your Mac.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
G=.git; STASH="$G/_stale-locks"; MINAGE=60
MODE="${1:-}"

if [[ "$MODE" != "--report" ]]; then
  now=$(date +%s); dest="$STASH/$(date +%Y%m%d-%H%M%S)"; moved=0
  while IFS= read -r -d '' f; do
    age=$(( now - $(stat -c %Y "$f") ))
    if [[ "$MODE" == "--now" || $age -ge $MINAGE ]]; then
      rel="${f#$G/}"; mkdir -p "$dest/$(dirname "$rel")"; mv "$f" "$dest/$rel"; moved=$((moved+1))
    fi
  done < <(find "$G" -path "$STASH" -prune -o \( -name '*.lock' -o -name 'tmp_obj_*' \) -type f -print0)
  echo "moved: $moved"
fi

if [[ -d "$STASH" ]]; then
  n=$(find "$STASH" -type f | wc -l | tr -d ' ')
  kb=$(du -sk "$STASH" | cut -f1)
  echo "stash: $n files, ${kb} KB in $STASH"
  # Thresholds for offering a cleanup (see CLAUDE.md)
  if (( n > 100 || kb > 20480 )); then echo "CLEANUP SUGGESTED (over 100 files or 20 MB)"; fi
else
  echo "stash: empty"
fi
