"""Entry point: run with `python main.py`."""

import sys

from verse_of_the_day.api import fetch_verse, pick_verse_number
from verse_of_the_day.display import format_verse

# Make sure Arabic text prints correctly, even on Windows terminals.
sys.stdout.reconfigure(encoding="utf-8")

verse_number = pick_verse_number()
verse = fetch_verse(verse_number, "en")
print(format_verse(verse))