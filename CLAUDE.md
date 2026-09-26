# Notes for Claude sessions in this repo

## Git housekeeping on Steve's computer

Claude sessions here cannot delete files without a per-session approval, so git
may leave lock files (`.git/*.lock`, `.git/objects/maintenance.lock`) and
`tmp_obj_*` files behind after a commit, checkout or merge. Leftover locks make
the next git command fail.

- Do not request delete permission for these. Instead, in the same shell call as
  any git command that writes (commit, checkout, merge, rebase, branch, tag), run
  `scripts/git-stash-stale-locks.sh --now` right after it. This moves leftovers
  into `.git/_stale-locks/` (inside `.git`, so never tracked).
- If a git command fails with "Unable to create ... .lock: File exists", run
  `scripts/git-stash-stale-locks.sh` (no flag; it only moves files older than
  60 seconds, so it won't disturb a git command Steve is running himself), then retry.
- Check the stash at the start of each session that uses git
  (`scripts/git-stash-stale-locks.sh --report`) and after each git write.
  When it reports CLEANUP SUGGESTED (over 100 files or 20 MB), offer Steve
  a cleanup. He can empty `.git/_stale-locks/` himself, or approve deletion
  for that session.

## Repo map

- `sources/paper-behavior-codebook_v0.2.md`: Stage 1 instrument (papers). v0.1 kept for history.
- `sources/communication-behavior-protocol_v0.2.md`: Stage 2 protocol (public communications about the papers). v0.1 kept for history. Stage 2 runs only after Stage 1 is scored and frozen (protocol §2).
- `sources/lexicons/`: per-language certainty-marker lexicons (English in the codebook; German starter list) and the register lexicon (`register_dismissive_v0.1.*`).
- `sources/study-design-explainer_draft1.md`: study-design explainer draft. Paper PDFs are also in `sources/`.
- `pilot/`: Stage 1 pilot exhibits for LS11 and FR11 at the top level.
  - `pilot/communications/`: Stage 2 pilot for LS11 and FR11 (inventory, Exhibit 4 and Addendum 1, German review packet, verbatim captures including `sources/threads/`). See its README.
  - `pilot/connolly-2021/`: Connolly et al. 2021. Stage 1 (Exhibit 3) at the top; Stage 2 (inventory, Exhibit 5, captures) in `communications/`.
  - `pilot/register/`: register (PC-9) and reply-claim data for all pilot papers.
- `src/fable-vs-opus/`: scorer-model equivalence harness (v2 is the reference implementation).
- `scripts/`: repo housekeeping (`git-stash-stale-locks.sh`) and analysis helpers (`register_count.py`).
