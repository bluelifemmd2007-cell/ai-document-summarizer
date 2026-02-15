import re

# حذف فاصله‌های اضافی
def normalize_spaces(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

# چک کردن خالی بودن متن
def is_empty(text: str) -> bool:
    return len(text.strip()) == 0

# حذف کاراکترهای غیرقابل چاپ
def remove_non_printable(text: str) -> str:
    return ''.join(ch for ch in text if ch.isprintable())

# نرمال‌سازی حروف فارسی/عربی
def normalize_persian_chars(text: str) -> str:
    replacements = {
        'ي': 'ی',
        'ك': 'ک',
        'ۀ': 'ه',
        'ة': 'ه',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
