# Probe 04 — rare_sticker Badge Client-Side Filter (5 Runs × 5 Min)

**Date:** 2026-04-17  
**Endpoint:** `GET /api/v1/listings?limit=50&type=buy_now&sort_by=most_recent`  
**Runs:** 5 × limit=50, spaced 5 minutes apart  
**Total listings scanned:** 250  
**Total rare_sticker matches:** 7

---

## Run 1 — 2026-04-17T15:08:08Z

**Scanned 50 listings, 1 had rare_sticker badge**

```
listing_id:    965267305732902689
name:          AK-47 | Blue Laminate (Field-Tested)
price:         $490.00
predicted:     $17.14
watchers:      0
created_at:    2026-04-17T15:07:39Z
sticker:       Sticker | Team LDLC.com | Katowice 2014 — $1587.56
sticker:       Sticker | Team LDLC.com | Katowice 2014 — $1587.56
sticker:       Sticker | Team LDLC.com | Katowice 2014 — $1587.56
sticker:       Sticker | Luminosity Gaming (Foil) | MLG Columbus 2016 — $99.89
sticker_total: $4862.57
sticker_ratio: 9.92x
url:           https://csfloat.com/item/965267305732902689
```

---

## Run 2 — 2026-04-17T15:13:08Z

**Scanned 50 listings, 0 had rare_sticker badge**

---

## Run 3 — 2026-04-17T15:18:08Z

**Scanned 50 listings, 0 had rare_sticker badge**

---

## Run 4 — 2026-04-17T15:23:09Z

**Scanned 50 listings, 1 had rare_sticker badge**

```
listing_id:    965271177276817629
name:          AK-47 | Blue Laminate (Field-Tested)
price:         $330.00
predicted:     $17.62
watchers:      0
created_at:    2026-04-17T15:23:02Z
sticker:       Sticker | iBUYPOWER | Katowice 2014 — $5068.23
sticker:       Sticker | Team Dignitas | Katowice 2014 — $900.91
sticker:       Sticker | mousesports | Katowice 2014 — $551.83
sticker:       Sticker | Natus Vincere | 2020 RMR — $0.03
sticker_total: $6521.00
sticker_ratio: 19.76x
url:           https://csfloat.com/item/965271177276817629
```

---

## Run 5 — 2026-04-17T15:28:09Z

**Scanned 50 listings, 5 had rare_sticker badge**

```
listing_id:    965272447593088216
name:          Glock-18 | Candy Apple (Factory New)
price:         $304.00
predicted:     $2.95
watchers:      0
created_at:    2026-04-17T15:28:05Z
sticker:       Sticker | 3DMAX | Katowice 2014 — $715.03
sticker:       Sticker | compLexity Gaming (Holo) | Katowice 2014 — $2399.99
sticker:       Sticker | LGB eSports | Katowice 2014 — $799.71
sticker:       Sticker | Tyloo | Stockholm 2021 — $0.19
sticker:       Sticker | ZywOo | Austin 2025 — $0.04
sticker_total: $3914.96
sticker_ratio: 12.88x
url:           https://csfloat.com/item/965272447593088216

listing_id:    965272446343185611
name:          M4A1-S | Guardian (Minimal Wear)
price:         $310.00
predicted:     $31.45
watchers:      0
created_at:    2026-04-17T15:28:05Z
sticker:       Sticker | Team LDLC.com | Katowice 2014 — $1587.56
sticker:       Sticker | Titan | Katowice 2014 — $3581.08
sticker:       Sticker | Clan-Mystik | Katowice 2014 — $703.04
sticker_total: $5871.68
sticker_ratio: 18.94x
url:           https://csfloat.com/item/965272446343185611

listing_id:    965272442945799307
name:          AWP | Redline (Field-Tested)
price:         $1000.00
predicted:     $38.96
watchers:      0
created_at:    2026-04-17T15:28:04Z
sticker:       Sticker | Ninjas in Pyjamas (Holo) | Katowice 2014 — $7745.54
sticker:       Sticker | Virtus.Pro (Holo) | Katowice 2014 — $5058.63
sticker:       Sticker | Fnatic (Holo) | Katowice 2014 — $1000.00
sticker:       Sticker | Natus Vincere (Holo) | Katowice 2014 — $11054.79
sticker_total: $24858.96
sticker_ratio: 24.86x
url:           https://csfloat.com/item/965272442945799307

listing_id:    965272441901417603
name:          Desert Eagle | Cobalt Disruption (Minimal Wear)
price:         $835.00
predicted:     $85.91
watchers:      0
created_at:    2026-04-17T15:28:04Z
sticker:       Sticker | Team Dignitas (Holo) | Katowice 2014 — $26367.03
sticker:       Sticker | Fnatic (Holo) | Katowice 2015 — $151.00
sticker_total: $26518.03
sticker_ratio: 31.76x
url:           https://csfloat.com/item/965272441901417603

listing_id:    965272440764761208
name:          Glock-18 | Dragon Tattoo (Factory New)
price:         $425.00
predicted:     $181.60
watchers:      0
created_at:    2026-04-17T15:28:04Z
sticker:       Sticker | HellRaisers | Katowice 2014 — $584.55
sticker:       Sticker | Titan | Katowice 2014 — $3581.08
sticker:       Sticker | Chrome Dome (Holo) — $4.04
sticker:       Sticker | ropz (Champion) | Austin 2025 — $0.03
sticker_total: $4169.70
sticker_ratio: 9.81x
url:           https://csfloat.com/item/965272440764761208
```

---

## Repeat Listing Analysis

**No listing appeared in more than one run.** Every match was a fresh listing at the time of scan. This means rare_sticker items are either selling quickly or the 5-minute gap between runs is enough to miss them in subsequent `most_recent` windows.

---

## Summary Table

| Run | Time (UTC) | Scanned | Matches | Listings |
|---|---|---|---|---|
| 1 | 15:08 | 50 | 1 | AK-47 Blue Laminate — $490, 9.92x |
| 2 | 15:13 | 50 | 0 | — |
| 3 | 15:18 | 50 | 0 | — |
| 4 | 15:23 | 50 | 1 | AK-47 Blue Laminate — $330, 19.76x |
| 5 | 15:28 | 50 | 5 | Glock Candy Apple, M4A1-S Guardian, AWP Redline, Deagle Cobalt, Glock Dragon Tattoo |

**Hit rate:** 7 matches / 250 scanned = **2.8%** of buy-now listings carry rare_sticker badge  
**Average per run:** 1.4 matches / run  
**Run 5 bulk event:** All 5 listings created within 2 seconds of each other — one seller bulk-listed their entire Katowice 2014 inventory simultaneously.

---

## Key Observations

### Katowice 2014 stickers dominate
All 7 matches carry at least one Katowice 2014 sticker. These are the most valuable vintage stickers in CS2, from the first-ever major tournament. Some highlights:
- Team Dignitas (Holo) Katowice 2014: **$26,367**
- NaVi (Holo) Katowice 2014: **$11,055**
- NiP (Holo) Katowice 2014: **$7,746**
- iBUYPOWER Katowice 2014: **$5,068**

### Prices are high but still below sticker value
Sellers are aware the stickers have value — none of these are "$0.15 auctions with $1,000 stickers." Prices range $304–$1,000. But sticker ratios still range 9.81x–31.76x, meaning buyers get enormous sticker value at a fraction of market price.

### All watchers = 0 at listing time
Every match had 0 watchers — these are freshly listed. Watcher accumulation is a later signal, not an immediate one. The scanner should alert immediately on listing, not wait for watchers.

### Sticker ratio thresholds seen
- Floor: ~9.8x (Glock Dragon Tattoo)  
- Ceiling: ~31.8x (Deagle Cobalt Disruption with $26K Dignitas Holo)
- The P2000 trade from probe_03 was 12.66x — solidly mid-range by this sample.

### Run 5 bulk listing event
One seller listed 5 items within 2 seconds at 15:28:03–05 UTC. This is a motivated seller clearing inventory fast. Total sticker value across 5 items: ~$65K. Total asking price: ~$2,874. These are the highest-value opportunities and they appear in clusters.

---

## Architecture Notes

### Scanner design implications

**Poll interval:** 5 minutes between runs missed 0 repeat listings, meaning items either sell or fall out of the `most_recent` window within 5 minutes. To catch everything: poll every **60–90 seconds** at limit=50. At ~125 listings/min throughput, a 60s poll at limit=50 catches roughly half of new listings. At limit=100 (if supported) or two sequential requests, coverage approaches full.

**Alert immediately on listing:** Don't wait for watchers — rare_sticker items are identifiable the moment they're listed. Alert as soon as badge is detected.

**Bulk listing events:** Multiple rare_sticker items may appear in the same scan. Run 5 shows 5 in one batch. The scanner should process all matches per poll, not just the first.

**Deduplication is essential:** Track seen listing IDs in the DB to avoid re-alerting if a listing reappears across poll windows (didn't happen in this probe, but will at higher poll frequency).

**Rate budget at 60s polling:**
- 1 request/min = 60 req/hr = 1,440 req/day
- With 50K weekly limit (~7,100/day): well within budget.
- Could even poll every 30s (2,880/day) without concern.

**Filter worthiness:** 2.8% hit rate on the badge filter means ~97% of listings are discarded client-side with zero extra API calls. The badge is an efficient signal.

**Minimum ratio threshold:** Consider alerting only when `sticker_ratio >= 5x` to avoid low-value noise. All matches here were ≥9.8x, so 5x is a conservative floor.
