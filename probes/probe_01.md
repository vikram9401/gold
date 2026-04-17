# Probe 01 — CSFloat API Listings Observation

**Date:** 2026-04-17  
**Endpoint:** `GET https://csfloat.com/api/v1/listings?limit=3&sort_by=highest_discount`  
**Script:** `probes/probe_01.py`

---

## Response Headers

```
Date: Fri, 17 Apr 2026 14:33:26 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
vary: Origin
x-ratelimit-limit: 200
x-ratelimit-remaining: 199
x-ratelimit-reset: 1776440006
server: cloudflare
Via: 1.1 google
cf-cache-status: DYNAMIC
Cache-Control: max-age=0
Content-Encoding: gzip
CF-RAY: 9edc25163ff52f73-LAX
alt-svc: h3=":443"; ma=86400
```

---

## Rate Limits

- **Limit:** 200 requests per window
- **Reset:** epoch `1776440006` — a rolling window, not hourly. ~3.3 req/sec sustainable.
- **Cloudflare-fronted** — LAX PoP, via Google backbone.

---

## Full JSON Response

```json
{
  "data": [
    {
      "id": "965257241286544914",
      "created_at": "2026-04-17T14:27:39.935103Z",
      "type": "auction",
      "price": 15,
      "description": "world nr 1 starttrak",
      "state": "listed",
      "seller": {
        "avatar": "https://avatars.steamstatic.com/834f66a42e015a336cd50d17ab09511a538f4e5c_full.jpg",
        "away": false,
        "flags": 48,
        "online": false,
        "stall_public": true,
        "statistics": {
          "median_trade_time": 200,
          "total_avoided_trades": 2,
          "total_failed_trades": 2,
          "total_trades": 47,
          "total_verified_trades": 45
        },
        "steam_id": "76561198305685156",
        "username": "Chael Sonnen"
      },
      "reference": {
        "base_price": 3479,
        "predicted_price": 3479,
        "quantity": 53,
        "last_updated": "2026-04-17T14:23:14.918371Z"
      },
      "item": {
        "asset_id": "50350546489",
        "def_index": 7,
        "paint_index": 1425,
        "paint_seed": 3,
        "float_value": 0.9944719076156616,
        "icon_url": "i0CoZ81Ui0m-...",
        "is_stattrak": true,
        "is_souvenir": false,
        "rarity": 5,
        "quality": 9,
        "market_hash_name": "StatTrak™ AK-47 | Crane Flight (Battle-Scarred)",
        "tradable": 0,
        "cs2_screenshot_id": "1812090974162423056",
        "cs2_screenshot_at": "2026-03-22T19:13:21.225321Z",
        "is_commodity": false,
        "type": "skin",
        "rarity_name": "Classified",
        "type_name": "Skin",
        "item_name": "AK-47 | Crane Flight",
        "wear_name": "Battle-Scarred",
        "description": "...",
        "collection": "The Dead Hand Collection",
        "serialized_inspect": "steam://rungame/...",
        "gs_sig": "885f44e4dffcbf1fcd98"
      },
      "is_seller": false,
      "is_watchlisted": false,
      "watchers": 3,
      "auction_details": {
        "reserve_price": 10,
        "top_bid": {
          "id": "965258645468218079",
          "created_at": "2026-04-17T14:33:14.718602Z",
          "price": 15,
          "contract_id": "965257241286544914",
          "state": "active",
          "obfuscated_buyer_id": "6210792195162945244"
        },
        "expires_at": "2026-04-20T14:27:39.934091Z",
        "min_next_bid": 20
      }
    },
    {
      "id": "965257411172630790",
      "created_at": "2026-04-17T14:28:20.439471Z",
      "type": "auction",
      "price": 10,
      "state": "listed",
      "seller": {
        "away": false,
        "flags": 48,
        "obfuscated_id": "7096395178028856365",
        "online": false,
        "stall_public": false,
        "statistics": { "median_trade_time": 143, "total_avoided_trades": 0, "total_failed_trades": 0, "total_trades": 27, "total_verified_trades": 27 }
      },
      "reference": {
        "base_price": 497,
        "float_factor": 0.98974365,
        "predicted_price": 492,
        "quantity": 351,
        "last_updated": "2026-04-17T14:27:47.150312Z"
      },
      "item": {
        "asset_id": "47533913149",
        "def_index": 1,
        "paint_index": 1050,
        "paint_seed": 514,
        "float_value": 0.1329258680343628,
        "is_stattrak": true,
        "is_souvenir": false,
        "rarity": 4,
        "quality": 9,
        "market_hash_name": "StatTrak™ Desert Eagle | Trigger Discipline (Minimal Wear)",
        "stickers": [
          {
            "stickerId": 5145,
            "slot": 1,
            "icon_url": "https://community.akamai.steamstatic.com/...",
            "name": "Sticker | NiKo (Holo) | Stockholm 2021",
            "reference": { "price": 698, "quantity": 563, "updated_at": "2026-04-16T04:20:47.191405Z" }
          },
          {
            "stickerId": 7264,
            "slot": 2,
            "offset_x": 0.014752984,
            "offset_y": 4.9322844e-05,
            "icon_url": "https://community.akamai.steamstatic.com/...",
            "name": "Sticker | G2 Esports (Holo) | Copenhagen 2024",
            "reference": { "price": 526, "quantity": 418, "updated_at": "2026-04-16T03:19:53.490591Z" }
          }
        ],
        "tradable": 0,
        "is_commodity": false,
        "type": "skin",
        "rarity_name": "Restricted",
        "type_name": "Skin",
        "item_name": "Desert Eagle | Trigger Discipline",
        "wear_name": "Minimal Wear",
        "collection": "The Snakebite Collection",
        "gs_sig": "8eab22749dc3306692ca"
      },
      "is_seller": false,
      "is_watchlisted": false,
      "watchers": 0,
      "auction_details": {
        "reserve_price": 10,
        "expires_at": "2026-04-18T14:28:20.436636Z",
        "min_next_bid": 10
      }
    },
    {
      "id": "965254055700072397",
      "created_at": "2026-04-17T14:15:00.43262Z",
      "type": "auction",
      "price": 15,
      "description": "Clouds & Sun, Check Stall ❤️",
      "state": "listed",
      "seller": {
        "avatar": "https://avatars.steamstatic.com/...",
        "away": false,
        "flags": 48,
        "online": true,
        "stall_public": true,
        "statistics": { "median_trade_time": 94, "total_avoided_trades": 0, "total_failed_trades": 1, "total_trades": 2851, "total_verified_trades": 2850 },
        "steam_id": "76561198919885084",
        "username": "non c'è morte"
      },
      "reference": {
        "base_price": 515,
        "float_factor": 1.0861099,
        "predicted_price": 559,
        "quantity": 14213,
        "last_updated": "2026-04-17T14:14:11.97141Z"
      },
      "item": {
        "asset_id": "50459886910",
        "def_index": 60,
        "paint_index": 1338,
        "paint_seed": 418,
        "float_value": 0.08304156363010406,
        "is_stattrak": false,
        "is_souvenir": false,
        "rarity": 5,
        "quality": 4,
        "market_hash_name": "M4A1-S | Solitude (Minimal Wear)",
        "tradable": 0,
        "is_commodity": false,
        "type": "skin",
        "rarity_name": "Classified",
        "type_name": "Skin",
        "item_name": "M4A1-S | Solitude",
        "wear_name": "Minimal Wear",
        "collection": "Limited Edition Item",
        "gs_sig": "254a854c409ce04c246c"
      },
      "is_seller": false,
      "is_watchlisted": false,
      "watchers": 3,
      "auction_details": {
        "reserve_price": 10,
        "top_bid": {
          "id": "965258688644384553",
          "created_at": "2026-04-17T14:33:25.012065Z",
          "price": 15,
          "contract_id": "965254055700072397",
          "state": "active",
          "obfuscated_buyer_id": "6210792195162945244"
        },
        "expires_at": "2026-04-24T14:15:00.431466Z",
        "min_next_bid": 20
      }
    }
  ],
  "cursor": "CAEQCBjGpYnPBiDNj4igsa7Rsg0ovoqT_bsBQS3zo4ZGeps_6R6SnBH7"
}
```

---

## Extracted Fields Per Listing

| Field | Listing 1 | Listing 2 | Listing 3 |
|---|---|---|---|
| id | 965257241286544914 | 965257411172630790 | 965254055700072397 |
| market_hash_name | StatTrak™ AK-47 \| Crane Flight (BS) | StatTrak™ Desert Eagle \| Trigger Discipline (MW) | M4A1-S \| Solitude (MW) |
| price | 15c = $0.15 | 10c = $0.10 | 15c = $0.15 |
| reference.predicted_price | 3479c = $34.79 | 492c = $4.92 | 559c = $5.59 |
| reference.base_price | 3479c = $34.79 | 497c = $4.97 | 515c = $5.15 |
| discount (approx) | 99.6% | 98.0% | 97.3% |
| watchers | 3 | 0 | 3 |
| float_value | 0.9945 | 0.1329 | 0.0830 |
| stickers | none | NiKo Holo Stockholm 2021 ($6.98), G2 Holo Copenhagen 2024 ($5.26) | none |
| type | auction | auction | auction |

---

## Field Notes — Discrepancies & Undocumented Fields

### CRITICAL: `reference_price` is NOT a top-level field
CLAUDE.md documents it as `reference_price` on the listing root. **It does not exist there.**  
The actual structure is a nested `reference` object:
```
listing.reference.predicted_price  ← use this as the fair-value price
listing.reference.base_price       ← base before float adjustment
listing.reference.float_factor     ← float premium/discount multiplier (optional)
listing.reference.quantity         ← how many of this skin exist on CSFloat
listing.reference.last_updated     ← when reference was last computed
```

### CRITICAL: Sticker prices are NOT at `item.stickers[].scm.price`
CLAUDE.md says `scm.price`. **There is no `scm` key.** The actual structure is:
```
item.stickers[].reference.price     ← price in cents (this is the SCM/market price)
item.stickers[].reference.quantity  ← how many listed
item.stickers[].reference.updated_at
```

### `sort_by=highest_discount` returns auctions only (in this sample)
All 3 results are `"type": "auction"` with absurdly low prices ($0.10–$0.15 on $5–$35 items). This sort may be dominated by auctions. To find buy-now mispriced listings, may need `type=buy_now` filter param.

### `auction_details` object (undocumented structure)
Present on all auction listings:
- `reserve_price` — minimum the seller will accept (cents)
- `expires_at` — ISO8601 auction end time
- `min_next_bid` — minimum bid increment from current price (cents)
- `top_bid` (optional) — present if bids exist: `id`, `price`, `state`, `obfuscated_buyer_id`

### `listing.type` field
Values seen: `"auction"`. Likely also `"buy_now"` for fixed-price listings.

### `seller.flags` (undocumented)
Numeric field, value `48` on all 3 sellers. Unknown meaning — possibly a bitmask for seller permissions/verification status.

### `seller.obfuscated_id` vs `seller.steam_id`
Public stalls expose `steam_id` + `username` + `avatar`. Private stalls (`stall_public: false`) replace these with `obfuscated_id` only.

### `item.gs_sig` (undocumented)
Short hex string on every item (e.g., `"885f44e4dffcbf1fcd98"`). Likely an internal integrity signature or game-server verification token.

### `item.tradable: 0`
All items have `tradable: 0` — these are trade-locked items (common after market purchase). Not a blocker for CSFloat since it uses its own escrow system.

### `item.paint_seed` and `item.paint_index`
Numeric fields present on all skins. `paint_seed` is the pattern seed (relevant for knives/gloves), `paint_index` maps to the skin design.

### `item.def_index`
Steam item definition index (weapon type identifier).

### `item.quality`
Numeric quality (9 = StatTrak, 4 = Normal). Maps to Steam economy quality values.

### `stickers[].stickerId`
Numeric sticker definition ID.

### `stickers[].offset_x` / `stickers[].offset_y`
Float position offsets for sticker placement on the weapon model. Only present when non-default. Seen on listing 2, sticker 2: `offset_x: 0.014752984, offset_y: 4.93e-05`.

### `stickers[].slot`
Integer 0–4, the sticker slot position on the weapon.

### `cursor` (top-level pagination)
Base64-ish opaque cursor for paginating results. Pass as `cursor=<value>` in next request.

### `listing.description`
Optional free-text seller note. Present on listings 1 and 3, absent on listing 2.

### `listing.is_watchlisted` / `listing.is_seller`
Always `false` for API requests (these are viewer-context fields, meaningless without auth session).

---

## Key Takeaways for Scanner Design

1. **Use `listing.reference.predicted_price`** (not `reference_price`) as fair value.
2. **Use `stickers[].reference.price`** (not `scm.price`) for sticker value.
3. **`sort_by=highest_discount` surfaces auctions** — need to test with `type=buy_now` to find fixed-price steals.
4. **Rate limit:** 200 req/window — be conservative, ~1 req/sec is safe.
5. **`float_factor`** in reference is useful: when `float_factor > 1.0`, the float is premium (rarer pattern); factor it into true value.
6. **`watchers`** field confirmed at listing root — usable as signal.
7. **`reference.quantity`** tells us market depth — low quantity = less liquid = harder to flip.
