import contextlib
import io
import unittest
from unittest.mock import patch

import main


class UnicodeWordTests(unittest.TestCase):
    def test_curly_and_straight_apostrophes_share_frequency(self):
        self.assertEqual(main.count_words(main.get_words("Don't don’t DON'T")), {"don't": 3})

    def test_equivalent_unicode_spellings_share_frequency(self):
        self.assertEqual(main.count_words(main.get_words("Café Cafe\u0301 CAFÉ")), {"café": 3})

    def test_multilingual_words_and_punctuation(self):
        self.assertEqual(main.get_words("Қазақша, РУССКИЙ! state-of-the-art foo_bar one--two"),
                         ["қазақша", "русский", "state-of-the-art", "foo", "bar", "one", "two"])

    def test_search_uses_the_same_normalization(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="DON’T"), contextlib.redirect_stdout(output):
            main.search_word({"don't": 3})
        self.assertIn("appears 3 time(s)", output.getvalue())

    def test_empty_or_punctuation_only_text(self):
        self.assertEqual(main.get_words("___ -- '' …"), [])


if __name__ == "__main__":
    unittest.main()
