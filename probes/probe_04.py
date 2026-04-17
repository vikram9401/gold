import os, json, requests
from datetime import datetime, timezone
from dotenv import dotenv_values

env = dotenv_values(os.path.expanduser("~/.env.gold"))
api_key = env["CSFLOAT_API_KEY"]
headers = {"Authorization": api_key}

url = "https://csfloat.com/api/v1/listings"
params = {"limit": 50, "type": "buy_now", "sort_by": "most_recent"}

print(f"\n=== RUN TIMESTAMP: {datetime.now(timezone.utc).isoformat()} ===")

resp = requests.get(url, params=params, headers=headers)
data = resp.json()
listings = data.get("data", [])

matches = [l for l in listings if "rare_sticker" in l.get("item", {}).get("badges", [])]

for l in matches:
    item = l.get("item", {})
    ref  = l.get("reference", {})
    price = l.get("price", 0)
    pred  = ref.get("predicted_price", 0)
    stickers = item.get("stickers", [])
    stk_total = sum(s.get("reference", {}).get("price", 0) for s in stickers)
    stk_ratio = stk_total / price if price else 0

    print(f"\n  listing_id:    {l.get('id')}")
    print(f"  name:          {item.get('market_hash_name')}")
    print(f"  price:         ${price/100:.2f}")
    print(f"  predicted:     ${pred/100:.2f}")
    print(f"  watchers:      {l.get('watchers')}")
    print(f"  created_at:    {l.get('created_at')}")
    for s in stickers:
        sp = s.get("reference", {}).get("price", 0)
        print(f"  sticker:       {s.get('name')} — ${sp/100:.2f}")
    print(f"  sticker_total: ${stk_total/100:.2f}")
    print(f"  sticker_ratio: {stk_ratio:.2f}x")
    print(f"  url:           https://csfloat.com/item/{l.get('id')}")

print(f"\nScanned {len(listings)} listings, {len(matches)} had rare_sticker badge")
