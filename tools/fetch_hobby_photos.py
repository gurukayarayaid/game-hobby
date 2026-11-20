"""Download curated Creative Commons hobby photos from Openverse for the game.

Usage:
  python tools/fetch_hobby_photos.py --dry-run   # list candidate photos
  python tools/fetch_hobby_photos.py             # download + write credits
"""
import argparse
import io
import os
import random
import sys
import time

import requests
from PIL import Image, ImageOps

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "assets", "hobbies")
CREDITS = os.path.join(OUT, "CREDITS.md")
API = "https://api.openverse.org/v1/images/"
HEADERS = {"User-Agent": "game-hobby-build/1.0 (educational flashcards)"}
ALLOWED_LICENSES = {"by", "by-sa", "cc0", "pdm"}

# name: (search query, preferred title substring)
QUERIES = {
    "reading": ("reading book", "Girl reading book"),
    "swimming": ("kids swimming pool", "Learning to swim"),
    "painting": ("artist painting picture easel", "Revolutionary Street Artist"),
    "cycling": ("cycling bicycle rider", "Velib riders"),
    "cooking": ("chef preparing food kitchen", "chef preparing food kitchen restaurant"),
    "dancing": ("ballet dancer dancing", "Modern Ballet Dancer"),
    "singing": ("singing microphone singer", "Singer with microphone"),
    "gardening": ("gardening flowers", "Garden flower"),
    "fishing": ("fishing rod fisherman", "Surf Fishing"),
    "hiking": ("hiking mountains trail", "Grinnell Glacier Trail"),
    "sketching": ("pencil drawing art", "Cartoon artist sketch"),
    "sewing": ("person sewing hobby", "Needle & Thread"),
    "jogging": ("runner jogging", "Runner Jogging"),
    "yoga": ("yoga pose", "Yoga Pose"),
    "chess": ("chess board game", "chess game"),
    "soccer": ("soccer ball football", "Soccer"),
    "tennis": ("tennis racket ball court", "Roger Federer wins the 2007 US Open"),
    "guitar": ("acoustic guitar instrument", "playing the guitar"),
    "drums": ("drum kit drums", "Trap Kit Drum Drums"),
    "camping": ("camping tent", "Camping Tent"),
}


def search(term, page_size=8):
    params = {
        "q": term,
        "page_size": page_size,
        "license": ",".join(sorted(ALLOWED_LICENSES)),
        "mature": "false",
    }
    last_error = None
    for attempt in range(4):
        try:
            r = requests.get(API, params=params, headers=HEADERS, timeout=35)
            r.raise_for_status()
            return r.json().get("results", [])
        except requests.RequestException as exc:
            last_error = exc
            time.sleep(random.uniform(1.5, 4.0) * (attempt + 1))
    raise last_error


def candidates(term):
    out = []
    for item in search(term):
        lic = (item.get("license") or "").lower()
        if lic not in ALLOWED_LICENSES:
            continue
        if not item.get("thumbnail") or not item.get("url"):
            continue
        out.append(item)
    return out


def ordered_items(name, query, preferred):
    items = candidates(query)
    if not items:
        raise RuntimeError(f"no usable photo for {name!r}")
    needle = preferred.lower()
    preferred_items = [i for i in items if needle in (i.get("title") or "").lower()]
    if preferred_items:
        return preferred_items + [i for i in items if i not in preferred_items]
    return items


def download_photo(item, path, size=480):
    thumb = item["thumbnail"]
    sep = "&" if "?" in thumb else "?"
    url = f"{thumb}{sep}width={size}"
    last_error = None
    for attempt in range(4):
        try:
            r = requests.get(url, headers=HEADERS, timeout=45)
            r.raise_for_status()
            im = Image.open(io.BytesIO(r.content)).convert("RGB")
            im = ImageOps.fit(im, (size, size), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
            im.save(path, "JPEG", quality=88, optimize=True)
            return
        except (requests.RequestException, OSError) as exc:
            last_error = exc
            time.sleep(random.uniform(1.0, 2.5) * (attempt + 1))
    raise last_error


def download_one(name, query, preferred, path):
    errors = []
    for item in ordered_items(name, query, preferred):
        try:
            download_photo(item, path)
            return item
        except Exception as exc:
            errors.append(str(exc).splitlines()[0])
    raise RuntimeError(f"no downloadable photo for {name!r}: {errors[:3]}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.dry_run:
        for name, (query, preferred) in QUERIES.items():
            print(f"\n== {name}: {query} (want {preferred!r}) ==", flush=True)
            try:
                items = ordered_items(name, query, preferred)[:5]
            except Exception as exc:
                print(f"  ERROR: {exc}", flush=True)
                continue
            for item in items:
                print(f"  {item.get('title')!r:60} {item.get('license'):6} {item.get('creator')}", flush=True)
        return

    os.makedirs(OUT, exist_ok=True)
    picked = {}
    for name, (query, preferred) in QUERIES.items():
        path = os.path.join(OUT, name + ".jpg")
        item = download_one(name, query, preferred, path)
        picked[name] = item
        print(f"{name:10s} <- {item.get('title')} ({item.get('license')}, {item.get('creator')})", flush=True)
        time.sleep(random.uniform(0.3, 0.8))

    lines = [
        "# Hobby photo credits",
        "",
        "Photos downloaded from [Openverse](https://openverse.org/) under the listed Creative Commons licenses.",
        "They are cropped to square for the game cards.",
        "",
        "| Hobby | Photo | Creator | License | Source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name, item in picked.items():
        title = (item.get("title") or name).replace("|", "\\|")
        creator = (item.get("creator") or "unknown").replace("|", "\\|")
        lic = item.get("license") or "-"
        src = item.get("foreign_landing_url") or item.get("source") or item.get("url") or "-"
        lines.append(f"| {name} | {title} | {creator} | {lic} | {src} |")
    with open(CREDITS, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nWrote credits: {CREDITS}")


if __name__ == "__main__":
    main()
