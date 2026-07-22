"""Synchronize a public Google Scholar profile into Jekyll's data directory."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_data" / "scholar.json"
SCHOLAR_ID = os.getenv("GOOGLE_SCHOLAR_ID", "wdxoBcUAAAAJ")
PROFILE_URL = "https://scholar.google.com/citations"


def number(text: str) -> int:
    digits = re.sub(r"[^0-9]", "", text)
    return int(digits) if digits else 0


def fetch_profile() -> dict:
    response = requests.get(
        PROFILE_URL,
        params={
            "user": SCHOLAR_ID,
            "hl": "en",
            "view_op": "list_works",
            "sortby": "pubdate",
            "pagesize": "100",
        },
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            )
        },
        timeout=30,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.select_one("#gs_captcha_ccl") or not soup.select_one("#gsc_prf_in"):
        raise RuntimeError(
            "Google Scholar did not return the public profile (it may be rate limiting this runner)."
        )

    stat_rows = soup.select("#gsc_rsb_st tbody tr")
    stats: dict[str, int] = {}
    for key, row in zip(("citations", "h_index", "i10_index"), stat_rows):
        values = row.select(".gsc_rsb_std")
        stats[key] = number(values[0].get_text(strip=True)) if values else 0

    publications = []
    for row in soup.select("#gsc_a_b .gsc_a_tr"):
        title_link = row.select_one(".gsc_a_at")
        if not title_link:
            continue

        gray_lines = row.select(".gs_gray")
        href = urljoin(PROFILE_URL, title_link.get("href", ""))
        citation_for_view = parse_qs(urlparse(href).query).get("citation_for_view", [""])[0]
        publication_id = citation_for_view.rsplit(":", 1)[-1]
        citation_link = row.select_one(".gsc_a_c a")
        year_cell = row.select_one(".gsc_a_y")

        publications.append(
            {
                "id": publication_id,
                "title": title_link.get_text(" ", strip=True),
                "authors": gray_lines[0].get_text(" ", strip=True) if gray_lines else "",
                "venue": gray_lines[1].get_text(" ", strip=True) if len(gray_lines) > 1 else "",
                "year": year_cell.get_text(strip=True) if year_cell else "",
                "citations": number(citation_link.get_text(strip=True)) if citation_link else 0,
                "scholar_url": href,
            }
        )

    if not publications:
        raise RuntimeError("No publications were found; refusing to overwrite the existing data.")

    return {
        "profile": {
            "id": SCHOLAR_ID,
            "name": soup.select_one("#gsc_prf_in").get_text(" ", strip=True),
            "url": f"{PROFILE_URL}?user={SCHOLAR_ID}&hl=en",
            **stats,
        },
        "publications": publications,
    }


def main() -> None:
    data = fetch_profile()
    existing = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else {}
    comparable_existing = {
        "profile": existing.get("profile"),
        "publications": existing.get("publications"),
    }
    if data == comparable_existing:
        print(f"Scholar data is already current ({len(data['publications'])} publications).")
        return

    data["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {OUTPUT} with {len(data['publications'])} publications.")


if __name__ == "__main__":
    main()
