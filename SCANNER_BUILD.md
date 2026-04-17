# Scanner Build Notes

**Date:** 2026-04-17  
**File:** `scanner.py`

---

## What Was Built

A polling daemon that scans CSFloat for buy-now listings with mispriced sticker value and alerts via Telegram.

## Config (top of scanner.py)

| Parameter | Value | Meaning |
|---|---|---|
| POLL_INTERVAL_SECONDS | 90 | Seconds between polls |
| MAX_PRICE_CENTS | 15000 | Max listing price ($150) |
| MIN_STICKER_RATIO | 5.0 | Min sticker_total / price |
| API_KEY_FILE | ~/.env.gold | CSFloat API key |
| TETOS_CONF | ~/.tetos.conf | Telegram credentials |

## Filter Logic

Three conditions must all pass:
1. `"rare_sticker"` in `item.badges` — CSFloat pre-flags these
2. `price <= MAX_PRICE_CENTS` — low entry price
3. `sticker_total / price >= MIN_STICKER_RATIO` — strong value ratio

Seen IDs tracked in-memory (`seen_ids` set) to deduplicate across polls.

## Telegram Alert

- Sends photo via `sendPhoto` if `item.cs2_screenshot_id` present
- Screenshot URL: `https://csfloat.pics/m/{cs2_screenshot_id}/playside.png?v=3`
- Falls back to `sendMessage` if sendPhoto fails or no screenshot
- Includes fade info if `item.fade` present

## Credentials

- `~/.env.gold` — CSFloat API key (created in probe setup)
- `~/.tetos.conf` — Telegram bot token + chat ID (sourced from `~/.openclaw/openclaw.json`)
  - Bot token: TetOS bot (`@TetOS_mini_bot`)
  - Chat ID: user's personal Telegram ID

## Test Run Output

```
Gold scanner starting — max_price=$150.00, min_ratio=5.0x, interval=90s
Sending connectivity test...
  [ok] Test message sent to Telegram
[08:39:15] Polled 50 listings — 0 matches
```

Telegram connectivity confirmed. 0 matches in this poll cycle (expected — rare_sticker under $150 is infrequent).

## Build Issues Encountered

- **Python 3.9 f-string backslash restriction** — complex nested f-strings with backslash escapes are a syntax error in Python 3.9. Fixed by building strings with concatenation instead.
- **`~/.tetos.conf` did not exist** — created from values in `~/.openclaw/openclaw.json` (`channels.telegram.botToken` and `channels.telegram.allowFrom[0]`).

## How to Run

```bash
# Test mode (one poll, then exit)
python3 scanner.py --test

# Daemon mode
python3 scanner.py
```

## Next Steps

- Run as a persistent daemon (launchd or nohup)
- Consider increasing limit to 100 if API supports it
- Add minimum single-sticker threshold (e.g., skip if no individual sticker > $50)
- Track sold_at on matched listings to measure how fast they move
