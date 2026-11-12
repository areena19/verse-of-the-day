"""Turns verse data into text that is ready to print."""

def format_verse(verse):
    """Turn the verse dictionary into text ready to print."""
    title = (
        f"{verse['surah_name']} ({verse['surah_arabic_name']}) "
        f"- {verse['surah_number']}:{verse['verse_number']}"
    )
    line = "=" * 60
    return (
        f"{line}\n{title}\n{line}\n\n"
        f"{verse['arabic']}\n\n"
        f"{verse['translation']}\n\n"
        f"Translation: {verse['translator']}\n{line}"
    )