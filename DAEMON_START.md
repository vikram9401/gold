# Daemon Start — Gold Scanner

**Date:** 2026-04-17  
**Start time:** 08:44:16 UTC  
**Observation window:** 3 minutes

---

## Start Command

```bash
mkdir -p /Volumes/T9/Projects/gold/logs
cd /Volumes/T9/Projects/gold
nohup python3 -u scanner.py > logs/scanner.log 2>&1 &
```

Note: `-u` flag required for unbuffered stdout — without it, print output sits in Python's buffer and never reaches the log file until the process exits.

**PID:** 49942  
**Status:** `pgrep -f scanner.py` confirmed running.

---

## Log Output (3-minute capture)

```
Gold scanner starting — max_price=$150.00, min_ratio=5.0x, interval=90s
Sending connectivity test...
  [ok] Test message sent to Telegram
[08:44:16] ALERT: AWP | Redline (Field-Tested) $140.00, ratio 13.65x → sent
[08:44:16] Polled 50 listings — 1 match (AWP | Redline (Field-Tested) $140.00, ratio 13.65x)
[08:45:47] Polled 50 listings — 0 matches
[08:47:17] Polled 50 listings — 0 matches
```

---

## Summary

| Metric | Value |
|---|---|
| Poll cycles completed | 3 |
| Matches found | 1 |
| Alerts sent | 1 |
| Telegram connectivity | Confirmed |

---

## Match Detail

**AWP | Redline (Field-Tested)**  
- Price: $140.00  
- Sticker ratio: 13.65x  
- Sticker value: ~$1,911  
- Found in first poll cycle, alert sent immediately  
- Telegram photo alert delivered via sendPhoto

---

## Notes

- Scanner fires on first poll — no warm-up delay
- 90s interval producing clean cadence: 08:44:16 → 08:45:47 → 08:47:17
- Daemon is running persistently; logs accumulating at `logs/scanner.log`
- `logs/` directory is gitignored (covered by `data/` exclusion — should add explicit entry)
