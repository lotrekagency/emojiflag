# Emojiflag 🏳️‍🌈 🇺🇸 🇪🇸 🇮🇹
[![Open Source Love png3](https://badges.frapsoft.com/os/v3/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Latest Version](https://img.shields.io/pypi/v/emojiflag.svg)](https://pypi.python.org/pypi/emojiflag/)
[![codecov](https://codecov.io/gh/lotrekagency/emojiflag/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/emojiflag)
[![Build Status](https://travis-ci.org/lotrekagency/emojiflag.svg?branch=master)](https://travis-ci.org/lotrekagency/emojiflag)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lotrekagency/emojiflag/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6febe99f004349029b9aaa285f9db555)](https://www.codacy.com/app/Owanesh/emojiflag?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lotrekagency/emojiflag&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/emojiflag.svg)](https://badge.fury.io/py/emojiflag)

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


### Credits

https://schinckel.net/2015/10/29/unicode-flags-in-python/
