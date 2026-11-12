"""Entry point: run with `python main.py`."""

from verse_of_the_day.api import fetch_verse

print(fetch_verse("1:2", "en"))