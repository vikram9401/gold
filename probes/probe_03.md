# Probe 03 — Single Listing Deep Dive (Sold Trade)

**Date:** 2026-04-17  
**Endpoint:** `GET https://csfloat.com/api/v1/listings/786245374879861366`  
**Script:** `probes/probe_03.py`

---

## Response Headers

```
Date: Fri, 17 Apr 2026 14:59:07 GMT
Content-Type: application/json; charset=utf-8
x-ratelimit-limit:     50000
x-ratelimit-remaining: 47989
x-ratelimit-reset:     1776492352
server: cloudflare
cf-cache-status: DYNAMIC
Cache-Control: max-age=0
```

### CRITICAL: Rate limit is 50,000 — not 200

Previous probes showed `x-ratelimit-limit: 200`. This request returned **50,000** with **47,989 remaining**.
The earlier 200-limit responses were almost certainly from a different rate limit tier or endpoint bucket.
With 50K requests per window this scanner is fully viable. Reset at epoch `1776492352` ≈ 2026-04-23
(~6 days from now), suggesting a **weekly rolling window** — ~7,100 requests/day sustainable.

---

## Full JSON Response

```json
{
  "id": "786245374879861366",
  "created_at": "2024-12-09T14:58:25.104873Z",
  "type": "buy_now",
  "price": 7900,
  "state": "sold",
  "seller": {
    "away": false,
    "flags": 48,
    "obfuscated_id": "11909300729368790277",
    "online": false,
    "stall_public": false,
    "statistics": {
      "median_trade_time": 72,
      "total_avoided_trades": 0,
      "total_failed_trades": 0,
      "total_trades": 1145,
      "total_verified_trades": 1145
    }
  },
  "reference": {
    "base_price": 96,
    "float_factor": 1,
    "predicted_price": 96,
    "quantity": 1232,
    "last_updated": "2026-04-16T20:17:54.682384Z"
  },
  "item": {
    "asset_id": "34968247161",
    "def_index": 32,
    "paint_index": 246,
    "paint_seed": 952,
    "float_value": 0.08155030012130737,
    "is_stattrak": false,
    "is_souvenir": false,
    "rarity": 4,
    "quality": 4,
    "market_hash_name": "P2000 | Amber Fade (Minimal Wear)",
    "stickers": [
      {
        "stickerId": 56,
        "slot": 0,
        "name": "Sticker | Fnatic (Holo) | Katowice 2014",
        "reference": {
          "price": 100000,
          "quantity": 5,
          "updated_at": "2026-04-16T06:22:13.260672Z"
        }
      }
    ],
    "tradable": 0,
    "d_param": "2776049305621916296",
    "is_commodity": false,
    "type": "skin",
    "rarity_name": "Restricted",
    "type_name": "Skin",
    "item_name": "P2000 | Amber Fade",
    "wear_name": "Minimal Wear",
    "collection": "The Dust 2 Collection",
    "badges": ["rare_sticker"],
    "fade": {
      "seed": 952,
      "percentage": 88.98303,
      "rank": 546,
      "type": "amber-fade"
    },
    "gs_sig": "463f06af8c1aa787d4bd"
  },
  "is_seller": false,
  "is_watchlisted": false,
  "watchers": 33,
  "sold_at": "2026-04-16T20:57:17.019726Z"
}
```

---

## Extracted Fields

| Field | Value |
|---|---|
| market_hash_name | P2000 \| Amber Fade (Minimal Wear) |
| float_value | 0.08155 |
| price | 7900c = **$79.00** |
| reference.predicted_price | 96c = $0.96 |
| reference.base_price | 96c = $0.96 |
| reference.float_factor | 1.0 |
| discount | -8129% (price >> reference — sticker value not in reference) |
| watchers | **33** |
| created_at | 2024-12-09T14:58:25Z (listed 16+ months ago) |
| sold_at | 2026-04-16T20:57:17Z |
| sticker | Fnatic (Holo) \| Katowice 2014 — **$1,000.00** |
| sticker_total | **$1,000.00** |
| sticker_ratio | **12.66x** (sticker is 12.7× the listing price) |
| state | sold |

---

## Trade Analysis

**What happened:** A P2000 | Amber Fade (skin worth ~$0.96 base) was listed for $79 because it carries a **Fnatic (Holo) | Katowice 2014** sticker currently valued at **$1,000**. The buyer paid $79 for $1,000 of sticker value — an 8,129% discount relative to sticker value.

**Why 33 watchers:** This is a legitimate sticker-value play that the market recognized. The watcher count (33) reflects crowd attention to a deeply mispriced item. Katowice 2014 holos are extremely rare collectibles.

**Why 16 months listed:** Either the seller didn't know the sticker's value, or intentionally priced it low to move it. Listing date is Dec 2024 — the skin sat for 16 months before selling Apr 16 2026.

**Sticker ratio of 12.66x** means the sticker alone is worth 12.7× what the buyer paid. This is the archetype of the scanner's target signal.

---

## Undocumented Fields Found

### `state: "sold"`
Sold listings are accessible via the single-listing endpoint. `state` can be `"listed"` or `"sold"` (and likely `"reserved"`). Useful for historical analysis.

### `sold_at`
ISO8601 timestamp of when the trade completed. Only present on sold listings. Allows computing time-to-sale.

### `item.badges` array
String array of CSFloat-assigned badges. Observed value: `["rare_sticker"]`. Likely other values exist (e.g., `"low_float"`, `"fade"`, etc.). **This is a pre-computed signal from CSFloat — extremely useful for filtering.**

### `item.fade` object
Present on fade-type skins. Contains:
- `seed` — paint seed (same as `paint_seed`)
- `percentage` — fade percentage (0–100), higher = more colorful
- `rank` — rank among all fade skins of this type (lower = rarer pattern)
- `type` — fade category string (e.g., `"amber-fade"`)

This listing: 88.98% fade, rank 546. Not a top-tier fade but respectable.

### `item.d_param`
Steam inspect URL D parameter, separate from the full `inspect_link`. Internal Steam economy identifier.

### `reference.quantity: 1232`
Number of this skin type listed on CSFloat. High quantity (1232) = liquid market. Combined with `float_factor: 1.0` means this float is not premium/discount.

### `seller.statistics.median_trade_time: 72`
72 seconds median trade time — this is a fast, reliable seller (1145 total trades, 0 failed).

---

## Key Takeaways for Scanner Design

1. **`item.badges` is the most important discovery** — CSFloat pre-flags `"rare_sticker"` for us. Filter on this instead of computing sticker ratios on every listing.
2. **`state` + `sold_at`** enable sold-listing analysis — can probe historical trades to calibrate what sticker ratios actually sell.
3. **Rate limit is 50,000/window** (not 200) — the earlier 200 limit was from a different endpoint bucket. Scanner is fully viable.
4. **`reference` does not include sticker value** — predicted_price reflects the bare skin only. A listing priced above reference is not necessarily overpriced; it may carry sticker premium.
5. **Watcher count on sold listing = 33** — high watcher count (≥10?) on a sticker-value listing is a strong buy signal worth alerting on immediately.
6. **Single-listing endpoint works on sold items** — useful for backtesting and understanding what the market considered good deals.
