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
