# Gold — CS2 Skin Scanner

## Project Overview
CS2 skin arbitrage scanner targeting CSFloat marketplace.
Monitors listings for mispriced sticker value, motivated sellers, and watcher momentum.

## Stack
- Python 3
- SQLite (data/gold.db)
- TetOS (@TetOS_mini_bot) for Telegram alerts
- Runs on Mini (always-on)

## Key Concepts
- All prices from CSFloat API are in cents — always convert to dollars for display
- watchers field = number of users watching a listing (crowd-sourced mispricing signal)
- reference_price = CSFloat's suggested fair price for the item
- Sticker SCM prices come inline on each listing under item.stickers[].scm.price

## Rules
- Never automate buying — read-only scanner only (risk of account ban)
- Git: checkpoint commit before edits, commit after every change, never git checkout
- All Claude Code prompts must be fully self-contained

## Files
- CLAUDE.md — this file
- data/gold.db — SQLite database (read-write)
- probes/ — one-off investigation scripts (not production)
