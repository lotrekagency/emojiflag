
Emojiflag 🏳️‍🌈 🇺🇸 🇪🇸 🇮🇹
========================


.. image:: https://badges.frapsoft.com/os/v3/open-source.png?v=103
   :target: https://github.com/ellerbrock/open-source-badges/
   :alt: Open Source Love png3


.. image:: https://img.shields.io/pypi/v/emojiflag.svg
   :target: https://pypi.python.org/pypi/emojiflag/
   :alt: Latest Version


.. image:: https://codecov.io/gh/lotrekagency/emojiflag/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lotrekagency/emojiflag
   :alt: codecov


.. image:: https://travis-ci.org/lotrekagency/emojiflag.svg?branch=master
   :target: https://travis-ci.org/lotrekagency/emojiflag
   :alt: Build Status


.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/lotrekagency/emojiflag/blob/master/LICENSE
   :alt: License: MIT


.. image:: https://api.codacy.com/project/badge/Grade/6febe99f004349029b9aaa285f9db555
   :target: https://www.codacy.com/app/Owanesh/emojiflag?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lotrekagency/emojiflag&amp;utm_campaign=Badge_Grade
   :alt: Codacy Badge


.. image:: https://badge.fury.io/py/emojiflag.svg
   :alt: PyPi version Badge
   :target: https://badge.fury.io/py/emojiflag


----

Install
^^^^^^^

.. code-block::

   pip install emojiflag


Use it ✌🏻
^^^^^^^^^^

.. code-block:: py

   import emojiflag

   emojiflag.get('nl')
   >>> 🇳🇱

   emojiflag.get('en_US')
   >>> 🇺🇸

   emojiflag.get('it')
   >>> 🇮🇹

Test it 💪🏻
^^^^^^^^^^^^

.. code-block:: sh

   pip install -r requirements-dev.txt

   pytest -s --cov emojiflag

Credits
^^^^^^^

https://schinckel.net/2015/10/29/unicode-flags-in-python/
