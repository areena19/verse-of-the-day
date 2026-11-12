# Verse of the Day

A command-line Python app that shows a Quran verse in Arabic with an English or Urdu translation, using live data from the [AlQuran Cloud API](https://alquran.cloud/api) (no API key needed).

## What it does

- Picks a random verse (out of 6,236) and shows the Arabic text with its translation
- Supports English (`en`) and Urdu (`ur`) translations
- Can show a specific verse, e.g. `2:255`
- Has a `--daily` mode that shows the same verse all day, so it works as a real "verse of the day"
- Handles timeouts, connection problems and invalid verses with clear error messages

## Install

Requires Python 3.8 or newer.

```bash
git clone https://github.com/areena19/verse-of-the-day.git
cd verse-of-the-day

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
# Random verse with English translation
python main.py

# Random verse with Urdu translation
python main.py --lang ur

# A specific verse (surah:verse)
python main.py --verse 2:255

# Same verse for the whole day
python main.py --daily
```

| Option | Meaning |
|--------|---------|
| `--lang en\|ur` | Translation language (default: `en`) |
| `--verse S:V` | Show a specific verse instead of a random one |
| `--daily` | Show one verse per day instead of a new random one each run |
| `-h`, `--help` | Show the help message |

## Sample output

`python main.py --daily`

```
============================================================
Ibrahim (سُورَةُ إِبۡرَاهِيمَ) - 14:4
============================================================

وَمَآ أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوْمِهِۦ لِيُبَيِّنَ لَهُمْ ۖ فَيُضِلُّ ٱللَّهُ مَن يَشَآءُ وَيَهْدِى مَن يَشَآءُ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ

And We did not send any messenger except [speaking] in the language of his people to state clearly for them, and Allah sends astray [thereby] whom He wills and guides whom He wills. And He is the Exalted in Might, the Wise.

Translation: Saheeh International
============================================================
```

`python main.py --lang ur`

```
============================================================
Saad (سُورَةُ صٓ) - 38:36
============================================================

فَسَخَّرْنَا لَهُ ٱلرِّيحَ تَجْرِى بِأَمْرِهِۦ رُخَآءً حَيْثُ أَصَابَ

پھر ہم نے ہوا کو ان کے زیرفرمان کردیا کہ جہاں وہ پہنچنا چاہتے ان کے حکم سے نرم نرم چلنے لگتی

Translation: جالندہری
============================================================
```

Invalid input shows a friendly error:

```
$ python main.py --verse 999:999
Error: verse "999:999" was not found. Try something like 2:255.
```

## API used

[AlQuran Cloud API](https://alquran.cloud/api): free, no key required.

Endpoint: `GET https://api.alquran.cloud/v1/ayah/{reference}/editions/quran-uthmani,{translation}`

## Project structure

```
verse-of-the-day/
├── main.py                  # entry point
├── requirements.txt         # dependencies (requests)
├── .gitignore
├── README.md
└── verse_of_the_day/
    ├── __init__.py
    ├── api.py               # fetch a verse, pick a random verse number
    ├── display.py           # format a verse for printing
    └── cli.py               # arguments and error handling
```