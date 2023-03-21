from src.paml2html import paml2html
from pathlib import Path
import unittest


class TestPaml(unittest.TestCase):
    def test_empty_text(self):
        text = ''
        result = paml2html.convert_from_text(text)
        expected = ''
        self.assertEqual(result, expected)

    def test_empty_file(self):
        fpath = Path(__file__).resolve().parent / 'fixtures' / 'empty.paml'
        result = paml2html.convert_from_file(fpath)
        expected = ''
        self.assertEqual(result, expected)
