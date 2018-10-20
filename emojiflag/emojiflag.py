import re
from .utils import DEFAULTS, COUNTRY_CODE_RE, OFFSET


def get(locale):
    locale = str(locale)
    if not locale or locale.isdigit() or len(locale) == 0:
        return ''
    code = code_for_locale(locale)
    if code:
        return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)
    else:
        return code


def code_for_locale(locale):
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
