from src.paml2html import paml2html
import unittest


class TestPaml(unittest.TestCase):
    def test_empty_text(self):
        text = ''
        result = paml2html.convert_from_text(text)
        expected = ''
        self.assertEqual(result, expected)
