"""Talks to the AlQuran Cloud API (fetching and choosing verses)."""

import requests

import random
from datetime import date

BASE_URL = "https://api.alquran.cloud/v1"
ARABIC_EDITION = "quran-uthmani"
TRANSLATIONS = {
    "en": "en.sahih",
    "ur": "ur.jalandhry",
}

TIMEOUT_SECONDS = 10
TOTAL_VERSES = 6236

def fetch_verse(reference, language="en"):
    """Fetch one verse (Arabic + translation) from the API.

    reference: a verse number (1-6236) or "surah:verse" such as "2:255".
    Returns a dictionary with the pieces we want to display.
    """
    translation_edition = TRANSLATIONS[language]
    url = f"{BASE_URL}/ayah/{reference}/editions/{ARABIC_EDITION},{translation_edition}"

    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    editions = response.json()["data"]

    # The API returns one entry per edition; find each by its identifier.
    by_edition = {item["edition"]["identifier"]: item for item in editions}
    arabic = by_edition[ARABIC_EDITION]
    translated = by_edition[translation_edition]

    return {
        "surah_number": arabic["surah"]["number"],
        "surah_name": arabic["surah"]["englishName"],
        "surah_arabic_name": arabic["surah"]["name"],
        "verse_number": arabic["numberInSurah"],
        "arabic": arabic["text"],
        "translation": translated["text"],
        "translator": translated["edition"]["name"],
    }

def pick_verse_number(daily=False):
    """Return a verse number between 1 and 6236.

    With daily=True the same verse is returned for the whole day,
    because the random generator is seeded with today's date.
    """
    if daily:
        generator = random.Random(date.today().isoformat())
        return generator.randint(1, TOTAL_VERSES)
    return random.randint(1, TOTAL_VERSES)