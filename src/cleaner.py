from src.utils import (
    normalize_spaces,
    is_empty,
    remove_non_printable,
    normalize_persian_chars
)

def clean_text(text: str) -> str:
    if is_empty(text):
        return ""

    text = remove_non_printable(text)
    text = normalize_persian_chars(text)
    text = normalize_spaces(text)

    return text
