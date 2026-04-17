import json
import os
import re
from datetime import datetime, timezone
from dotenv import dotenv_values
import requests

env = dotenv_values(os.path.expanduser("~/.env.gold"))
api_key = env["CSFLOAT_API_KEY"]
headers = {"Authorization": api_key}

REQUESTS = [
    ("most_recent",      "https://csfloat.com/api/v1/listings?limit=50&type=buy_now&sort_by=most_recent"),
    ("highest_discount", "https://csfloat.com/api/v1/listings?limit=50&type=buy_now&sort_by=highest_discount"),
]

def sticker_total(item):
    total = 0
    for s in item.get("stickers", []):
        total += s.get("reference", {}).get("price", 0)
    return total

def parse_dt(s):
    # Normalize variable-length fractional seconds to 6 digits (Python 3.9 compat)
    s = re.sub(r'\.(\d+)', lambda m: '.' + m.group(1).ljust(6, '0')[:6], s)
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

for label, url in REQUESTS:
    print(f"\n{'='*70}")
    print(f"REQUEST: {label}")
    print(f"URL: {url}")
    print('='*70)

    resp = requests.get(url, headers=headers)

    print("\n--- Rate Limit Headers ---")
    for h in ("x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-reset"):
        print(f"  {h}: {resp.headers.get(h)}")

    data = resp.json()
    listings = data.get("data", [])
    print(f"\nTotal listings returned: {len(listings)}")

    if not listings:
        print("  (no listings)")
        continue

    times = [parse_dt(l["created_at"]) for l in listings]
    newest = max(times)
    oldest = min(times)
    span_min = (newest - oldest).total_seconds() / 60

    print(f"Newest created_at:  {newest.isoformat()}")
    print(f"Oldest created_at:  {oldest.isoformat()}")
    print(f"Time span:          {span_min:.1f} minutes")

    print(f"\n{'listing_id':<20} {'created_at':<28} {'price':>8} {'watchers':>8} {'stk_ct':>6} {'stk_val':>8}  market_hash_name")
    print("-" * 140)

    w_gt0 = w_ge5 = stk_gt10 = stk_gt_price = 0

    for l in listings:
        item = l.get("item", {})
        lid = l.get("id", "")
        cat = l.get("created_at", "")
        price = l.get("price", 0)
        watchers = l.get("watchers", 0)
        mhn = item.get("market_hash_name", "")
        stks = item.get("stickers", [])
        stk_count = len(stks)
        stk_val = sticker_total(item)

        print(f"{lid:<20} {cat:<28} {price:>8} {watchers:>8} {stk_count:>6} {stk_val:>8}  {mhn}")

        if watchers > 0:  w_gt0 += 1
        if watchers >= 5: w_ge5 += 1
        if any(s.get("reference", {}).get("price", 0) > 1000 for s in stks):
            stk_gt10 += 1
        if stk_val > price:
            stk_gt_price += 1

    print(f"\n--- Summary Stats ({label}) ---")
    print(f"  Listings with watchers > 0:                   {w_gt0}/{len(listings)}")
    print(f"  Listings with watchers >= 5:                  {w_ge5}/{len(listings)}")
    print(f"  Listings with any sticker ref.price > $10:    {stk_gt10}/{len(listings)}")
    print(f"  Listings where sticker_total > listing_price: {stk_gt_price}/{len(listings)}")
