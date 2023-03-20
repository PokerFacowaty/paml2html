from src.paml2html import paml2html
import unittest

'''While running, paml2html starts with a fresh set of yattag's variables:
   doc, tag, text, line, as mentioned in yattag's docs: https://www.yattag.org/

   These are set every time convert_from_file or convert_from_text is called
   for normal use cases, as well as at the top of the paml2html.py file for
   unit testing purposes (so that the variables a particular function is trying
   to use is defined).

   Every unit test also redefines these variables at the end to make sure they
   are empty before the next test populates them. Had that not been the case,
   one test running after the other would append its result to the one made by
   the previous test.

   You might find it strange to see paml in a list such as header1 instead of
   a string, but functions expecting the paml_lines variable expect paml in a
   list of strings ending in \n with an additional empty line at the end either
   already there or added by convert_from_file or convert_from_text.
   '''


class TestPaml(unittest.TestCase):

    # Headers

    def test_header1(self):
        header1 = ["# Header 1\n", ""]
        paml2html.add_header(header1, 0)
        expected = "<h1>Header 1</h1>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_header2(self):
        header2 = ["## Header 2\n", ""]
        paml2html.add_header(header2, 0)
        expected = "<h2>Header 2</h2>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_header3(self):
        header3 = ["### Header 3\n", ""]
        paml2html.add_header(header3, 0)
        expected = "<h3>Header 3</h3>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_header4(self):
        header4 = ["#### Header 4\n", ""]
        paml2html.add_header(header4, 0)
        expected = "<h4>Header 4</h4>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_header5(self):
        header5 = ["##### Header 5\n", ""]
        paml2html.add_header(header5, 0)
        expected = "<h5>Header 5</h5>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_header6(self):
        header6 = ["###### Header 6\n", ""]
        paml2html.add_header(header6, 0)
        expected = "<h6>Header 6</h6>"
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    # Collapsibles

    # Collapsible-specific content

    # Code block

    def test_code_block_no_comments(self):
        block = ["```\n", "This is a code block\n", "with no comment.\n",
                 "```\n", ""]
        expected = '''<div class="block-code-box"><code class="block-code"><pre>This is a code block
with no comment.
</pre></code></div>'''

        paml2html.add_code_block(block, 0)
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_code_block_comment(self):
        block = ['```/* Comment */\n', 'This is a code block\n',
                 'with a comment.\n', '```\n', '']
        expected = '''<div class="block-code-box"><div class="block-code-comment">Comment</div><code class="block-code"><pre>This is a code block
with a comment.
</pre></code></div>'''

        paml2html.add_code_block(block, 0)
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_code_block_small_comment_only(self):
        block = ['```/** Small comment **/\n', 'This is a code block\n',
                 'with a comment.\n', '```\n', '']
        expected = '''<div class="block-code-box"><div class="block-code-small-comment">Small comment</div><code class="block-code"><pre>This is a code block
with a comment.
</pre></code></div>'''

        paml2html.add_code_block(block, 0)
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    def test_code_block_both_comments(self):
        block = ['```/** Small comment **/\n', 'This is a code block\n',
                 'with a comment.\n', '```\n', '']
        expected = '''<div class="block-code-box"><div class="block-code-small-comment">Small comment</div><code class="block-code"><pre>This is a code block
with a comment.
</pre></code></div>'''

        paml2html.add_code_block(block, 0)
        self.assertEqual(paml2html.doc.getvalue(), expected)

        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()

    # Images

    # Paragraphs

    # Unordered lists + content

    # Ordered lists + content

    # Tables

    # Raw HTML

    # Text elements

    # Text formatting as a whole


if __name__ == '__main__':
    unittest.main()
