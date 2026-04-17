# Gold — Bootstrap Findings

## Date
2026-04-17

## What Was Built
- `/Volumes/T9/Projects/gold/` created on Mini (M4 Mac Mini, always-on)
- Directory structure: `data/` (SQLite DB, gitignored), `probes/` (one-off scripts)
- `CLAUDE.md` — project rules and key concepts
- `README.md` — project summary
- `.gitignore` — excludes `.env`, `data/`, `__pycache__/`, `*.pyc`, `.DS_Store`

## Git Setup
- Repo initialized and first commit made: `44afb71`
- GitHub repo created: https://github.com/vikram9401/gold
- Remote: `git@github.com:vikram9401/gold.git` (SSH, matches other projects)
- `gh` CLI installed via Homebrew (`/opt/homebrew/bin/gh`), authenticated as `vikram9401`

## Notes
- `gh` is not on the default SSH PATH on Mini — invoke via `/opt/homebrew/bin/gh`
- SSH key `/Users/vik/.ssh/id_ed25519.pub` was already on GitHub; confirmed working
- `data/` is gitignored — `gold.db` will live locally on Mini only

## Next Steps
- Build CSFloat API poller
- Define SQLite schema for listings
- Wire up Telegram alerts via @TetOS_mini_bot
