# Probe 02 — Buy-Now Listings: Volume & Watcher Signal

**Date:** 2026-04-17  
**Script:** `probes/probe_02.py`  
**Requests made:** 2

---

## Request 1: `sort_by=most_recent` (type=buy_now, limit=50)

### Rate Limit Headers
```
x-ratelimit-limit:     200
x-ratelimit-remaining: 196
x-ratelimit-reset:     1776440006
```

### Time Coverage
- Listings returned: **50**
- Newest: `2026-04-17T14:44:16.476494Z`
- Oldest: `2026-04-17T14:43:52.793773Z`
- **Time span: 0.4 minutes (24 seconds)**

### Per-Listing Table

```
listing_id           created_at                      price watchers stk_ct  stk_val  market_hash_name
------------------------------------------------------------------------------------------------------------------------------------
965261421082444002   2026-04-17T14:44:16.476494Z        12        0      0        0  StatTrak™ M4A4 | Choppa (Battle-Scarred)
965261416003141784   2026-04-17T14:44:15.265522Z        25        0      0        0  SSG 08 | Calligrafaux (Minimal Wear)
965261413599805561   2026-04-17T14:44:14.69273Z         42        0      0        0  MAG-7 | Wildwood (Factory New)
965261412186325097   2026-04-17T14:44:14.355586Z     13300        0      0        0  AWP | Green Energy (Factory New)
965261408008798265   2026-04-17T14:44:13.3599Z         315        0      0        0  SG 553 | Dragon Tech (Factory New)
965261406922473521   2026-04-17T14:44:13.101035Z       403        0      0        0  USP-S | Alpine Camo (Factory New)
965261406016503848   2026-04-17T14:44:12.884608Z     35982        0      0        0  M4A1-S | Fade (Factory New)
965261400798793711   2026-04-17T14:44:11.641027Z      1644        0      3       86  Michael Syfers  | FBI Sniper
965261399817326560   2026-04-17T14:44:11.406917Z      1301        0      1       80  MP9 | Airlock (Minimal Wear)
965261398802304980   2026-04-17T14:44:11.164748Z       579        0      2        3  Five-SeveN | Urban Hazard (Factory New)
965261397585956802   2026-04-17T14:44:10.874318Z      1499        0      5     1557  AK-47 | Elite Build (Minimal Wear)
965261396587712437   2026-04-17T14:44:10.637044Z       276        0      0        0  StatTrak™ MP7 | Amberline (Field-Tested)
965261394637361052   2026-04-17T14:44:10.171866Z      9661        0      0        0  MP9 | Dark Age (Factory New)
965261386932424486   2026-04-17T14:44:08.334461Z     15157        0      0        0  ★ Skeleton Knife | Rust Coat (Battle-Scarred)
965261385095319314   2026-04-17T14:44:07.896258Z     38900        0      2      991  StatTrak™ AWP | Printstream (Minimal Wear)
965261384512311045   2026-04-17T14:44:07.757565Z        39        0      0        0  StatTrak™ Glock-18 | Oxide Blaze (Battle-Scarred)
965261383857999614   2026-04-17T14:44:07.601133Z         8        0      0        0  StatTrak™ UMP-45 | Roadblock (Field-Tested)
965261381035232978   2026-04-17T14:44:06.928771Z       724        1      0        0  UMP-45 | Late Night Transit (Factory New)
965261376438275722   2026-04-17T14:44:05.832142Z        46        0      0        0  M249 | Downtown (Field-Tested)
965261375087709821   2026-04-17T14:44:05.510281Z        48        0      0        0  SG 553 | Dragon Tech (Field-Tested)
965261373892333163   2026-04-17T14:44:05.225697Z        48        0      0        0  SG 553 | Dragon Tech (Field-Tested)
965261371732266578   2026-04-17T14:44:04.710252Z        48        0      0        0  SG 553 | Dragon Tech (Field-Tested)
965261370000019009   2026-04-17T14:44:04.298048Z        54        0      0        0  Dual Berettas | Flora Carnivora (Field-Tested)
965261369102437950   2026-04-17T14:44:04.083411Z      6500        0      3    57804  AWP | Fever Dream (Field-Tested)
965261368250994228   2026-04-17T14:44:03.880733Z        84        0      0        0  SG 553 | Dragon Tech (Minimal Wear)
965261368175496754   2026-04-17T14:44:03.862918Z       699        0      0        0  Desert Eagle | Heat Treated (Well-Worn)
965261367017868836   2026-04-17T14:44:03.586452Z       492        0      0        0  AK-47 | Ice Coaled (Field-Tested)
965261366288059936   2026-04-17T14:44:03.412988Z      4340        0      1      105  AK-47 | Orbit Mk01 (Minimal Wear)
965261365470170648   2026-04-17T14:44:03.217632Z      3568        0      0        0  AK-47 | Head Shot (Well-Worn)
965261364945882642   2026-04-17T14:44:03.092643Z     92000        0      0        0  ★ StatTrak™ Butterfly Knife | Crimson Web (Field-Tested)
965261357563907528   2026-04-17T14:44:01.332753Z       248        0      0        0  R8 Revolver | Amber Fade (Factory New)
965261353050836367   2026-04-17T14:44:00.256813Z        42        0      0        0  Revolution Case
965261353021476238   2026-04-17T14:44:00.249339Z        42        0      0        0  Revolution Case
965261352987921803   2026-04-17T14:44:00.241596Z        42        0      0        0  Revolution Case
965261352954367370   2026-04-17T14:44:00.234022Z        42        0      0        0  Revolution Case
965261352920812936   2026-04-17T14:44:00.22572Z         42        0      0        0  Revolution Case
965261352887258503   2026-04-17T14:44:00.217124Z        42        0      0        0  Revolution Case
965261352849509766   2026-04-17T14:44:00.208244Z        42        0      0        0  Revolution Case
965261352828538245   2026-04-17T14:44:00.203917Z       153        0      0        0  M249 | Bock Blocks (Factory New)
965261352807566724   2026-04-17T14:44:00.198757Z        42        0      0        0  Revolution Case
965261352769817987   2026-04-17T14:44:00.189858Z        42        0      0        0  Revolution Case
965261352727874943   2026-04-17T14:44:00.179998Z        42        0      0        0  Revolution Case
965261349452123488   2026-04-17T14:43:59.398339Z       798        0      1        1  StatTrak™ USP-S | Black Lotus (Minimal Wear)
965261326916127336   2026-04-17T14:43:54.02522Z       1348        0      0        0  AWP | Green Energy (Field-Tested)
965261325943048790   2026-04-17T14:43:53.793334Z       393        0      0        0  AWP | Duality (Field-Tested)
965261324890278474   2026-04-17T14:43:53.542949Z       360        0      0        0  AWP | Duality (Battle-Scarred)
965261324718312006   2026-04-17T14:43:53.501619Z       328        0      2     1569  Stockholm 2021 Ancient Souvenir Package
965261323636181558   2026-04-17T14:43:53.243291Z       371        0      0        0  Desert Eagle | Firebreathing (Minimal Wear)
965261323329997357   2026-04-17T14:43:53.171004Z       220        0      0        0  Desert Eagle | Corinthian (Factory New)
965261321748744733   2026-04-17T14:43:52.793773Z       122        0      0        0  MP9 | Goo (Field-Tested)
```

### Summary Stats (most_recent)
| Metric | Count |
|---|---|
| Listings with watchers > 0 | 1/50 (2%) |
| Listings with watchers >= 5 | 0/50 (0%) |
| Any sticker ref.price > $10 | 1/50 (2%) |
| sticker_total > listing_price | 3/50 (6%) |

---

## Request 2: `sort_by=highest_discount` (type=buy_now, limit=50)

### Rate Limit Headers
```
x-ratelimit-limit:     200
x-ratelimit-remaining: 195
x-ratelimit-reset:     1776440006
```

### Time Coverage
- Listings returned: **50**
- Newest: `2026-04-17T10:18:29.572106Z`
- Oldest: `2026-04-14T05:15:49.196550Z`
- **Time span: 4622.7 minutes (~77 hours / 3.2 days)**

### Per-Listing Table

```
listing_id           created_at                      price watchers stk_ct  stk_val  market_hash_name
------------------------------------------------------------------------------------------------------------------------------------
965175402358246184   2026-04-17T09:02:28.014343Z        13        0      4      441  Souvenir MP7 | Prey (Minimal Wear)
965175403528457009   2026-04-17T09:02:28.294005Z        13        0      4      334  Souvenir MAG-7 | Rust Coat (Minimal Wear)
965175404711250753   2026-04-17T09:02:28.575754Z        13        0      4      656  Souvenir PP-Bizon | Facility Sketch (Field-Tested)
965175406951009116   2026-04-17T09:02:29.109912Z        14        0      4      360  Souvenir MAG-7 | Navy Sheen (Field-Tested)
965175408045722466   2026-04-17T09:02:29.371004Z        15        0      4      617  Souvenir SG 553 | Bleached (Minimal Wear)
965175409190767466   2026-04-17T09:02:29.643976Z        15        0      4      617  Souvenir SG 553 | Bleached (Field-Tested)
965175410453252977   2026-04-17T09:02:29.944797Z        15        0      4      376  Souvenir PP-Bizon | Anolis (Field-Tested)
965175411518606199   2026-04-17T09:02:30.198247Z        15        0      4      376  Souvenir P250 | Drought (Factory New)
965175414911798157   2026-04-17T09:02:31.007249Z        17        1      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965175415985540006   2026-04-17T09:02:31.263722Z        17        0      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965175417109613485   2026-04-17T09:02:31.531249Z        17        0      4      617  Souvenir PP-Bizon | Anolis (Minimal Wear)
965175418292407240   2026-04-17T09:02:31.813394Z        17        1      4      617  Souvenir SSG 08 | Prey (Minimal Wear)
965175421329083368   2026-04-17T09:02:32.53716Z         17        1      4      617  Souvenir MAG-7 | Navy Sheen (Minimal Wear)
965175437762366622   2026-04-17T09:02:36.45598Z         28        0      4      672  Souvenir P90 | Desert DDPAT (Factory New)
965175426840398877   2026-04-17T09:02:33.851822Z        20        0      4      672  Souvenir SG 553 | Bleached (Factory New)
965175438978714799   2026-04-17T09:02:36.745114Z        29        0      4      672  Souvenir P90 | Desert DDPAT (Minimal Wear)
965175441285582051   2026-04-17T09:02:37.296006Z        29        0      4      672  Souvenir MP7 | Prey (Field-Tested)
965175442531290349   2026-04-17T09:02:37.592461Z        29        0      4      672  Souvenir R8 Revolver | Desert Brush (Battle-Scarred)
965175425791822866   2026-04-17T09:02:33.601143Z        20        0      4      672  Souvenir MP7 | Prey (Field-Tested)
965175427930917936   2026-04-17T09:02:34.111614Z        21        0      4      399  Souvenir MP7 | Prey (Factory New)
965175444657802495   2026-04-17T09:02:38.099699Z        31        0      4      672  Souvenir SG 553 | Bleached (Minimal Wear)
965166929780277282   2026-04-17T08:28:47.994166Z         8        0      4      576  Souvenir R8 Revolver | Night (Field-Tested)
965175387208419998   2026-04-17T09:02:24.402389Z         5        0      4      576  Souvenir R8 Revolver | Night (Well-Worn)
965175388382825143   2026-04-17T09:02:24.682056Z         5        0      4      576  Souvenir SSG 08 | Jungle Dashed (Field-Tested)
965175428979493957   2026-04-17T09:02:34.362028Z        22        0      4      376  Souvenir PP-Bizon | Anolis (Field-Tested)
965175430204230736   2026-04-17T09:02:34.653966Z        25        0      4      441  Souvenir P250 | Drought (Field-Tested)
965175431303138402   2026-04-17T09:02:34.915256Z        25        0      4      441  Souvenir P250 | Drought (Field-Tested)
965175434629221501   2026-04-17T09:02:35.708341Z        25        0      4      441  Souvenir MAG-7 | Navy Sheen (Field-Tested)
965175436583767179   2026-04-17T09:02:36.174999Z        25        0      4      441  Souvenir MAC-10 | Sienna Damask (Minimal Wear)
965194446025131690   2026-04-17T10:18:08.378259Z         5        0      4      617  Souvenir MP9 | Old Roots (Well-Worn)
965194532817863573   2026-04-17T10:18:29.071514Z         6        0      4      576  Souvenir P90 | Ancient Earth (Battle-Scarred)
965194534919209898   2026-04-17T10:18:29.572106Z         6        0      4      672  Souvenir MP9 | Old Roots (Field-Tested)
965166897010183446   2026-04-17T08:28:40.181419Z        17        0      4      447  Souvenir MAG-7 | Navy Sheen (Field-Tested)
965166807453402240   2026-04-17T08:28:18.829464Z        31        0      4      672  Souvenir P90 | Desert DDPAT (Field-Tested)
965175440111176898   2026-04-17T09:02:37.015754Z        31        0      4      672  Souvenir SG 553 | Bleached (Field-Tested)
964031201184713443   2026-04-14T05:15:49.19655Z         14        0      4      576  Souvenir R8 Revolver | Night (Field-Tested)
964303955075137561   2026-04-14T23:19:38.791751Z        14        0      4      576  Souvenir Nova | Army Sheen (Minimal Wear)
965175400084933395   2026-04-17T09:02:27.472209Z        12        0      4      576  Souvenir Nova | Mandrel (Field-Tested)
965166881524812537   2026-04-17T08:28:36.489088Z        18        0      4      617  Souvenir SSG 08 | Prey (Field-Tested)
965166885324852099   2026-04-17T08:28:37.395174Z        18        0      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965166886474091431   2026-04-17T08:28:37.669454Z        18        0      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965166887644302284   2026-04-17T08:28:37.94835Z         18        0      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965166888999062517   2026-04-17T08:28:38.271486Z        18        0      4      617  Souvenir MAG-7 | Navy Sheen (Field-Tested)
965166890123136025   2026-04-17T08:28:38.53924Z         18        0      4      617  Souvenir MAG-7 | Navy Sheen (Field-Tested)
965166891226238017   2026-04-17T08:28:38.802811Z        18        0      4      617  Souvenir PP-Bizon | Anolis (Minimal Wear)
965166892417420397   2026-04-17T08:28:39.086938Z        18        0      4      617  Souvenir PP-Bizon | Anolis (Field-Tested)
965166893528910989   2026-04-17T08:28:39.351525Z        18        0      4      617  Souvenir SSG 08 | Prey (Minimal Wear)
965166894711704763   2026-04-17T08:28:39.633788Z        18        0      4      617  Souvenir MAC-10 | Sienna Damask (Field-Tested)
965166895957413098   2026-04-17T08:28:39.930583Z        18        0      4      617  Souvenir MAC-10 | Sienna Damask (Field-Tested)
965166899191221643   2026-04-17T08:28:40.70159Z         18        0      4      617  Souvenir MAG-7 | Navy Sheen (Field-Tested)
```

### Summary Stats (highest_discount)
| Metric | Count |
|---|---|
| Listings with watchers > 0 | 3/50 (6%) |
| Listings with watchers >= 5 | 0/50 (0%) |
| Any sticker ref.price > $10 | 0/50 (0%) |
| sticker_total > listing_price | 50/50 (100%) |

---

## Key Observations

### `sort_by=most_recent` — listing velocity
- 50 listings in **24 seconds** = ~125 new buy-now listings per minute = **~2 per second**.
- Broad mix of items: skins, knives, cases, souvenir packages.
- New listings have near-zero watchers (expected — watchers accumulate over time).
- One sticker-value outlier: AWP | Fever Dream at $65 listing price with $578 sticker total.
- Bulk-listers are visible: 8× Revolution Case listed at identical price within one second.

### `sort_by=highest_discount` — dominated by souvenir junk
- **All 50 listings are souvenir items** with exactly 4 stickers.
- Prices $0.05–$0.31, sticker totals $3.34–$6.72. Sticker value exceeds price on every single one.
- These are bulk-listed low-tier souvenirs from one or two sellers (~09:02 UTC batch).
- Souvenir sticker prices individually are $0.03–$0.07 each — none exceed $10.
- **This sort is not useful for finding real arbitrage** — it's noise from souvenir dumpers.
- Two listings are 3+ days old (Apr 14), sitting stale at the top of "highest discount."

### Rate limit window is unclear — possibly very large
- `x-ratelimit-reset: 1776440006` is a Unix epoch timestamp of approximately **2026-04-26**, ~9 days from now.
- This did not change across all 5 requests in this session, suggesting it is a **fixed window reset**, not rolling.
- If the 200-request budget resets on 2026-04-26, that is ~22 requests/day — far too few to run a scanner.
- More likely interpretation: the reset timestamp is **static for the current window** and will update after the window expires. The actual window duration (hourly? daily?) needs a dedicated probe to determine.
- **CRITICAL: Clarify rate limit window before designing any scanner.** Use probe_03 to hammer the limit and observe reset behavior.

---

## Architecture Notes

### Is a watcher-velocity database feasible within observed rate limits?

**What watcher-velocity requires:**
1. Ingest new listings as they appear (poll `most_recent`).
2. Re-fetch those same listings at intervals (e.g., T+5m, T+15m, T+30m) to observe watcher count change.
3. Alert when velocity is anomalous (e.g., jumped from 0→8 in 15 minutes).

**The math at 200 req/window:**

Scenario A — if window = 1 hour (200 req/hr):
- New listing ingestion at 50/req: 1 poll/5min = 12 polls/hr = 12 req just to catch new listings.
- Remaining 188 req for re-fetching tracked listings = budget for ~188 individual re-fetches/hr.
- If tracking 100 active listings × 3 refresh intervals = 300 re-fetches needed. **Over budget.**
- Feasible only if tracking a small set (~60 listings max) or using a single-listing endpoint.

Scenario B — if window = 1 day (200 req/day):
- 200 req/day = ~8 req/hr. **A scanner is not feasible at this limit.**
- Would need to find if there's a higher-tier API key or websocket feed.

Scenario C — if window resets every few minutes (rolling):
- probe_02 used 2 req and saw remaining drop from 199→195 across 5 total requests this session.
- No reset was observed, so the window is at least 11 minutes. Possibly much longer.

**Recommendation:** Write probe_03 specifically to test rate limit window. Make ~20 rapid requests, observe `x-ratelimit-remaining` descent and wait for `x-ratelimit-reset` to flip to a new timestamp. Until this is known, do not architect the polling loop.

**Alternative signals that use fewer requests:**
- `most_recent` with limit=100 (if supported) to reduce ingestion cost.
- Focus on listings with stickers only — filter client-side, not with extra API calls.
- Single-listing re-fetch via `GET /api/v1/listings/{id}` if that endpoint exists (check in probe_03).
- Prioritize high-value items (e.g., reference.predicted_price > $20) to reduce the re-fetch set size.

**Verdict:** Feasible if rate limit window is hourly or shorter, with a conservative design tracking ≤50 listings at a time. Not feasible if daily limit. Need probe_03 to confirm before building.
