import json
import os
import requests
from dotenv import dotenv_values

env = dotenv_values(os.path.expanduser("~/.env.gold"))
api_key = env["CSFLOAT_API_KEY"]

url = "https://csfloat.com/api/v1/listings"
params = {"limit": 3, "sort_by": "highest_discount"}
headers = {"Authorization": api_key}

resp = requests.get(url, params=params, headers=headers)

print("=== RESPONSE HEADERS ===")
for k, v in resp.headers.items():
    print(f"{k}: {v}")

print("\n=== FULL JSON RESPONSE ===")
data = resp.json()
print(json.dumps(data, indent=2))

print("\n=== EXTRACTED FIELDS PER LISTING ===")
listings = data.get("data", [])
for i, listing in enumerate(listings):
    item = listing.get("item", {})
    print(f"\n--- Listing {i+1} ---")
    print(f"  id:               {listing.get('id')}")
    print(f"  market_hash_name: {item.get('market_hash_name')}")
    price_cents = listing.get('price')
    print(f"  price:            {price_cents}c = ${price_cents/100:.2f}" if price_cents is not None else "  price:            None")
    print(f"  watchers:         {listing.get('watchers')}")
    ref = listing.get('reference_price')
    print(f"  reference_price:  {ref}c = ${ref/100:.2f}" if ref is not None else "  reference_price:  None")
    print(f"  created_at:       {listing.get('created_at')}")
    print(f"  float_value:      {item.get('float_value')}")
    stickers = item.get("stickers", [])
    if stickers:
        print(f"  stickers ({len(stickers)}):")
        for s in stickers:
            scm = s.get("scm", {})
            scm_price = scm.get("price")
            scm_str = f"${scm_price/100:.2f}" if scm_price is not None else "N/A"
            print(f"    - {s.get('name')} | scm.price: {scm_str}")
    else:
        print("  stickers:         none")
