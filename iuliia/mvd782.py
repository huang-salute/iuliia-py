"""
MVD 782-2000 transliteration schema.
https://dangry.ru/iuliia/mvd-782/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "yo",
        "ж": "zh",
        "й": "y",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    },
}

PREV_MAPPING = {
    # е
    "ае": "ye",
    "ее": "ye",
    "ёе": "ye",
    "ие": "ye",
    "ое": "ye",
    "уе": "ye",
    "ъе": "ye",
    "ые": "ye",
    "ье": "ye",
    "эе": "ye",
    "юе": "ye",
    "яе": "ye",
    # ё
    "бё": "ye",
    "вё": "ye",
    "гё": "ye",
    "дё": "ye",
    "зё": "ye",
    "кё": "ye",
    "лё": "ye",
    "мё": "ye",
    "нё": "ye",
    "пё": "ye",
    "рё": "ye",
    "сё": "ye",
    "тё": "ye",
    "фё": "ye",
    "хё": "ye",
    "цё": "ye",
    "жё": "e",
    "чё": "e",
    "шё": "e",
    "щё": "e",
    # и
    "ьи": "yi",
}

NEXT_MAPPING = {
    "ъе": "",
    "ье": "",
    "ъё": "",
    "ьё": "",
    "ьи": "",
}

MVD_782 = Schema(MAPPING, prev_mapping=PREV_MAPPING, next_mapping=NEXT_MAPPING)
