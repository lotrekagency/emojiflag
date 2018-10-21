# Emojiflag 🏳️‍🌈 🇺🇸 🇪🇸 🇮🇹
[![Open Source Love png3](https://badges.frapsoft.com/os/v3/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Latest Version](https://img.shields.io/pypi/v/emojiflag.svg)](https://pypi.python.org/pypi/emojiflag/)
[![codecov](https://codecov.io/gh/lotrekagency/emojiflag/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/emojiflag)
[![Build Status](https://travis-ci.org/lotrekagency/emojiflag.svg?branch=master)](https://travis-ci.org/lotrekagency/emojiflag)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Owanesh/emojiflag/blob/master/LICENSE)

* * *

### Install

    pip install emojiflag

### Use it ✌🏻
```py
import emojiflag

emojiflag.get('nl')
>>> 🇳🇱

emojiflag.get('en_US')
>>> 🇺🇸

emojiflag.get('it')
>>> 🇮🇹

```


### Test it 💪🏻
```sh
pip install -r requirements-dev.txt

pytest -s --cov emojiflag
```


### The idea

```py
OFFSET = ord('🇦') - ord('A')

def flag(code):
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)
```

From https://schinckel.net/2015/10/29/unicode-flags-in-python/
