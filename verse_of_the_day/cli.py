"""Command-line interface: reads arguments and runs the program."""

import argparse
import sys

from verse_of_the_day.api import TRANSLATIONS, fetch_verse, pick_verse_number
from verse_of_the_day.display import format_verse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Show a Quran verse with an English or Urdu translation."
    )
    parser.add_argument(
        "--lang",
        choices=TRANSLATIONS.keys(),
        default="en",
        help="translation language: en (English) or ur (Urdu). Default: en",
    )
    parser.add_argument(
        "--verse",
        help='show a specific verse, e.g. "2:255" (surah:verse) instead of a random one',
    )
    parser.add_argument(
        "--daily",
        action="store_true",
        help="show the same verse all day (a 'verse of the day')",
    )
    return parser.parse_args()


def run():
    # Make sure Arabic/Urdu text prints correctly, even on Windows terminals.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args()
    reference = args.verse or pick_verse_number(daily=args.daily)

    verse = fetch_verse(reference, args.lang)
    print(format_verse(verse))