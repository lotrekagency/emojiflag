"""This module actually contains the `get` function definition."""
import re
from .utils import (COUNTRY_CODE_RE, DEFAULTS,
                    EXTRA_FLAGS, OFFSET)


def get(locale: str) -> str:
    """Get emoji flag for given locale.

    Args:
        locale (str): Locale code.

    Returns:
        str: Emoji flag.

    Examples:
        >>> get(':nl:')  # Get by 2 letters.
        '🇳🇱'
        >>> get('ru-RU')  # Get by locale code.
        '🇷🇺'
        >>> get('racing')  # Get non-country flag.
        '🏁'
        >>> get(':qq_QQ:')  # Get nonexistent flag.
        '🇶🇶'
    """
    locale = str(locale)
    if not locale or locale.isdigit() or len(locale) == 0:
        return ''

    if ':' in locale:
        locale = locale.replace(":", "")
    if locale in EXTRA_FLAGS.keys():
        return EXTRA_FLAGS[locale]

    code = code_for_locale(locale)
    if code:
        return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)
    else:
        return code


def code_for_locale(locale: str) -> str:
    """Get country code for given locale.

    Args:
        locale (str): Locale code.

    Returns:
        str: Country code.
    """
    locale = locale.upper()
    split = re.split('_|-', locale)
    lang = split[0]
    code = ''
    if len(split) == 2:
        code = split.pop()
    if not re.compile(COUNTRY_CODE_RE).match(code):
        if lang.lower() in DEFAULTS:
            code = DEFAULTS[lang.lower()]
    return code
