import argparse
import os
import sys
import time
from datetime import datetime, timezone
from dotenv import dotenv_values
import requests

# ── config ────────────────────────────────────────────────────────────────────
POLL_INTERVAL_SECONDS = 90
MAX_PRICE_CENTS       = 15000   # $150.00
MIN_STICKER_RATIO     = 5.0
API_KEY_FILE          = "~/.env.gold"
TETOS_CONF            = "~/.tetos.conf"

LISTINGS_URL   = "https://csfloat.com/api/v1/listings"
SCREENSHOT_URL = "https://csfloat.pics/m/{cs2_screenshot_id}/playside.png?v=3"
LISTING_URL    = "https://csfloat.com/item/{listing_id}"
TELEGRAM_API   = "https://api.telegram.org/bot{token}/{method}"
# ─────────────────────────────────────────────────────────────────────────────


def load_env(path):
    return dotenv_values(os.path.expanduser(path))


def sticker_total(item):
    return sum(s.get("reference", {}).get("price", 0) for s in item.get("stickers", []))


def mins_ago(iso):
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return int((datetime.now(timezone.utc) - dt).total_seconds() / 60)
    except Exception:
        return "?"


def build_message(listing):
    item      = listing.get("item", {})
    ref       = listing.get("reference", {})
    price     = listing.get("price", 0)
    pred      = ref.get("predicted_price", 0)
    stickers  = item.get("stickers", [])
    stk_total = sticker_total(item)
    stk_ratio = stk_total / price if price else 0
    fade      = item.get("fade")
    lid       = listing.get("id", "")

    sticker_lines = "\n".join(
        "  \u2022 " + s.get("name", "?") + " \u2014 $" + f"{s.get('reference', {}).get('price', 0)/100:.2f}"
        for s in stickers
    )

    fade_line = ""
    if fade:
        pct  = fade.get("percentage", 0)
        rank = fade.get("rank", "?")
        fade_line = "\n\U0001f308 Fade: " + f"{pct:.2f}% (rank #{rank})"

    mins = mins_ago(listing.get("created_at", ""))
    return (
        "\U0001f7e1 GOLD ALERT\n"
        + item.get("market_hash_name", "?") + "\n\n"
        + "\U0001f4b0 Price: $" + f"{price/100:.2f}\n"
        + "\U0001f4ca Predicted: $" + f"{pred/100:.2f}\n"
        + "\U0001f3af Sticker ratio: " + f"{stk_ratio:.2f}x\n\n"
        + "\U0001f3f7 Stickers:\n" + sticker_lines + "\n"
        + "\U0001f48e Total sticker value: $" + f"{stk_total/100:.2f}\n\n"
        + "\U0001f522 Float: " + str(item.get("float_value", "?"))
        + fade_line + "\n"
        + "\U0001f4c5 Listed: " + str(mins) + " mins ago\n"
        + "\U0001f441 Watchers: " + str(listing.get("watchers", 0)) + "\n\n"
        + "\U0001f517 " + LISTING_URL.format(listing_id=lid)
    )


def send_telegram(token, chat_id, listing):
    item    = listing.get("item", {})
    message = build_message(listing)
    ss_id   = item.get("cs2_screenshot_id")

    if ss_id:
        photo_url = SCREENSHOT_URL.format(cs2_screenshot_id=ss_id)
        try:
            r = requests.post(
                TELEGRAM_API.format(token=token, method="sendPhoto"),
                data={"chat_id": chat_id, "photo": photo_url,
                      "caption": message, "parse_mode": "HTML"},
                timeout=15,
            )
            if r.ok:
                return
            print("  [warn] sendPhoto failed (" + str(r.status_code) + "), falling back to sendMessage")
        except Exception as e:
            print("  [warn] sendPhoto exception: " + str(e) + ", falling back to sendMessage")

    try:
        r = requests.post(
            TELEGRAM_API.format(token=token, method="sendMessage"),
            data={"chat_id": chat_id, "text": message, "parse_mode": "HTML"},
            timeout=15,
        )
        if not r.ok:
            print("  [error] sendMessage failed: " + str(r.status_code) + " " + r.text[:200])
    except Exception as e:
        print("  [error] sendMessage exception: " + str(e))


def poll(csfloat_key, tg_token, tg_chat, seen_ids):
    params  = {"limit": 50, "type": "buy_now", "sort_by": "most_recent"}
    headers = {"Authorization": csfloat_key}
    ts      = datetime.now().strftime("%H:%M:%S")

    try:
        resp = requests.get(LISTINGS_URL, params=params, headers=headers, timeout=15)
        resp.raise_for_status()
        listings = resp.json().get("data", [])
    except Exception as e:
        print("[" + ts + "] Poll error: " + str(e))
        return

    matches = []
    for l in listings:
        try:
            item  = l.get("item", {})
            if "rare_sticker" not in item.get("badges", []):
                continue
            price = l.get("price", 0)
            if price > MAX_PRICE_CENTS:
                continue
            stk = sticker_total(item)
            if price == 0 or stk / price < MIN_STICKER_RATIO:
                continue
            matches.append(l)
        except Exception:
            continue

    new_matches = [l for l in matches if l.get("id") not in seen_ids]

    for l in new_matches:
        try:
            item  = l.get("item", {})
            price = l.get("price", 0)
            stk   = sticker_total(item)
            ratio = stk / price if price else 0
            name  = item.get("market_hash_name", "?")
            seen_ids.add(l.get("id"))
            send_telegram(tg_token, tg_chat, l)
            print("[" + ts + "] ALERT: " + name + " $" + f"{price/100:.2f}, ratio {ratio:.2f}x" + " \u2192 sent")
        except Exception as e:
            print("[" + ts + "] ALERT send error: " + str(e))

    if new_matches:
        parts = []
        for l in new_matches:
            nm    = l.get("item", {}).get("market_hash_name", "?")
            pr    = l.get("price", 0)
            st    = sticker_total(l.get("item", {}))
            ratio = st / pr if pr else 0
            parts.append(nm + " $" + f"{pr/100:.2f}, ratio {ratio:.2f}x")
        word = "matches" if len(new_matches) != 1 else "match"
        summary = str(len(new_matches)) + " " + word + " (" + ", ".join(parts) + ")"
    else:
        summary = "0 matches"

    print("[" + ts + "] Polled " + str(len(listings)) + " listings \u2014 " + summary)


def send_test_message(tg_token, tg_chat):
    try:
        r = requests.post(
            TELEGRAM_API.format(token=tg_token, method="sendMessage"),
            data={"chat_id": tg_chat,
                  "text": "\U0001f7e1 Gold scanner online \u2014 connectivity test OK"},
            timeout=15,
        )
        if r.ok:
            print("  [ok] Test message sent to Telegram")
        else:
            print("  [error] Test message failed: " + str(r.status_code) + " " + r.text[:200])
    except Exception as e:
        print("  [error] Test message exception: " + str(e))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true",
                        help="Run one poll cycle and exit")
    args = parser.parse_args()

    gold_env  = load_env(API_KEY_FILE)
    tetos_env = load_env(TETOS_CONF)

    csfloat_key = gold_env.get("CSFLOAT_API_KEY")
    tg_token    = tetos_env.get("TELEGRAM_BOT_TOKEN")
    tg_chat     = tetos_env.get("TELEGRAM_CHAT_ID")

    if not csfloat_key:
        sys.exit("[error] CSFLOAT_API_KEY not found in " + API_KEY_FILE)
    if not tg_token or not tg_chat:
        sys.exit("[error] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not found in " + TETOS_CONF)

    print("Gold scanner starting \u2014 max_price=$" + f"{MAX_PRICE_CENTS/100:.2f}, "
          + "min_ratio=" + str(MIN_STICKER_RATIO) + "x, interval=" + str(POLL_INTERVAL_SECONDS) + "s")

    print("Sending connectivity test...")
    send_test_message(tg_token, tg_chat)

    seen_ids = set()

    if args.test:
        poll(csfloat_key, tg_token, tg_chat, seen_ids)
        return

    while True:
        poll(csfloat_key, tg_token, tg_chat, seen_ids)
        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
