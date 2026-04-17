import json
import os
from dotenv import dotenv_values
import requests

env = dotenv_values(os.path.expanduser("~/.env.gold"))
api_key = env["CSFLOAT_API_KEY"]

url = "https://csfloat.com/api/v1/listings/786245374879861366"
resp = requests.get(url, headers={"Authorization": api_key})

print("=== RESPONSE HEADERS ===")
for k, v in resp.headers.items():
    print(f"  {k}: {v}")

print("\n=== FULL JSON RESPONSE ===")
data = resp.json()
print(json.dumps(data, indent=2))

print("\n=== EXTRACTED FIELDS ===")
item = data.get("item", {})
ref  = data.get("reference", {})

price     = data.get("price", 0)
pred      = ref.get("predicted_price", 0)
base      = ref.get("base_price", 0)
ff        = ref.get("float_factor")
discount  = (pred - price) / pred * 100 if pred else 0

stickers  = item.get("stickers", [])
stk_total = sum(s.get("reference", {}).get("price", 0) for s in stickers)
stk_ratio = stk_total / price if price else 0

print(f"  market_hash_name:         {item.get('market_hash_name')}")
print(f"  float_value:              {item.get('float_value')}")
print(f"  price:                    {price}c = ${price/100:.2f}")
print(f"  reference.predicted_price:{pred}c = ${pred/100:.2f}")
print(f"  reference.base_price:     {base}c = ${base/100:.2f}")
print(f"  reference.float_factor:   {ff}")
print(f"  discount:                 {discount:.1f}%")
print(f"  watchers:                 {data.get('watchers')}")
print(f"  created_at:               {data.get('created_at')}")

print(f"\n  stickers ({len(stickers)}):")
for s in stickers:
    sp = s.get("reference", {}).get("price", 0)
    print(f"    slot {s.get('slot')}: {s.get('name')} — ${sp/100:.2f}")

print(f"\n  sticker_total:  {stk_total}c = ${stk_total/100:.2f}")
print(f"  sticker_ratio:  {stk_ratio:.2f}x  (sticker value is {stk_ratio:.1f}x the listing price)")
