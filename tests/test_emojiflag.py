import unittest
from emojiflag import emojiflag


class TestEmojiFlag(unittest.TestCase):

    def test_country_lower(self):
        self.assertEqual('🇮🇹', emojiflag.get('it'))

    def test_country_upper(self):
        self.assertEqual('🇮🇹', emojiflag.get('IT'))

    def test_mixed(self):
        self.assertEqual('🇺🇸', emojiflag.get('en_US'))

    def test_integer(self):
        self.assertEqual('', emojiflag.get(123))

    def test_not_lang(self):
        self.assertEqual('', emojiflag.get('owanesh'))

    def test_code_for_locale(self):
        self.assertEqual('IT', emojiflag.code_for_locale('it_IT'))
        self.assertEqual('GB', emojiflag.code_for_locale('en_GB'))
