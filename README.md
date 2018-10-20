# Emojiflag

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

```


### Test it 💪🏻
```sh
pip install -r requirements-dev.txt

pytest -s --cov emojiflag
```


### The idea

>>> OFFSET = ord('🇦') - ord('A')
>>> def flag(code):
...     return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

From https://schinckel.net/2015/10/29/unicode-flags-in-python/
