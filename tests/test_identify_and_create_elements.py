from paml2html import paml2html
import unittest

'''These tests all test the identify_element function (it doesn't return
   anything so testing it this way sounds like the most sensible option) as
   well as creating new PaML elements with different types of content inside
   them.

   While running, paml2html starts with a fresh set of yattag's variables:
   doc, tag, text, line, as mentioned in yattag's docs: https://www.yattag.org/

   These are set every time convert_from_file or convert_from_text is called
   for normal use cases, as well as at the top of the paml2html.py file for
   unit testing purposes (so that the variables that a particular function is
   trying to use are defined).

   Every unit test also redefines these variables at the end (but before
   assertEqual in case the test fails) to make sure they are empty before the
   next test populates them. Had that not been the case, one test running after
   the other would append its result to the one made by the previous test.

   You might find it strange to see paml in a list such as header1 instead of
   a string, but functions expecting the paml_lines variable expect paml in a
   list of strings ending in \n with an additional empty line at the end either
   already there or added by convert_from_file or convert_from_text.'''


class TestPaml(unittest.TestCase):

    # Headers

    def test_header1(self):
        header1 = ["# Header 1\n", ""]
        expected = "<h1>Header 1</h1>"
        paml2html.identify_element(header1, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header2(self):
        header2 = ["## Header 2\n", ""]
        expected = "<h2>Header 2</h2>"
        paml2html.identify_element(header2, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header3(self):
        header3 = ["### Header 3\n", ""]
        expected = "<h3>Header 3</h3>"
        paml2html.identify_element(header3, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header4(self):
        header4 = ["#### Header 4\n", ""]
        expected = "<h4>Header 4</h4>"
        paml2html.identify_element(header4, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header5(self):
        header5 = ["##### Header 5\n", ""]
        expected = "<h5>Header 5</h5>"
        paml2html.identify_element(header5, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header6(self):
        header6 = ["###### Header 6\n", ""]
        expected = "<h6>Header 6</h6>"
        paml2html.identify_element(header6, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Collapsibles

    def test_l_collapsible_with_icon(self):
        coll = ['>l➤ coll\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> coll'
               + '</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_l_collapsible_with_icon_and_content(self):
        # A command is used as content since it's intended to be used with
        # collapsibles anyway
        coll = ['>l➤ collapsible\n',
                '    /Ctrl + E /* Comment */ /** Small comment **/\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> '
               + 'collapsible</summary>'

               + '<div class="entry"><div class="command-box"><span class='
               + '"command">Ctrl + E</span><span class="same-line-comment">'
               + 'Comment</span><div class="small-comment">Small comment</div>'
               + '</div></div></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_l_collapsible_without_icon(self):
        coll = ['>l coll\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header">coll</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_r_collapsible_with_icon(self):
        coll = ['>r➤ coll\n', '']
        exp = ('<div class="collapsible-box-half-right"><details>'
               + '<summary class="header"><span class="icon">➤</span> coll'
               + '</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_r_collapsible_without_icon(self):
        coll = ['>r coll\n', '']
        exp = ('<div class="collapsible-box-half-right"><details>'
               + '<summary class="header">coll</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_full_collapsible_with_icon(self):
        coll = ['>f➤ coll\n', '']
        exp = ('<div class="collapsible-box-full"><details>'
               + '<summary class="header"><span class="icon">➤</span> coll'
               + '</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_full_collapsible_without_icon(self):
        coll = ['>f coll\n', '']
        exp = ('<div class="collapsible-box-full"><details>'
               + '<summary class="header">coll</summary></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_nested_collapsible(self):
        coll = ['>l➤ collapsible\n',
                '    >l➤ nested collapsible\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> '
               + 'collapsible</summary>'

               + '<details><summary class="header">'
               + '<span class="icon">➤</span> nested collapsible</summary>'
               + '</details></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_nested_collapsible_with_content_in_primary(self):
        coll = ['>l➤ collapsible\n',
                '    /Ctrl + E /* Comment */ /** Small comment **/\n',
                '    >l➤ collapsible\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> '
               + 'collapsible</summary>'

               + '<div class="entry"><div class="command-box">'
               + '<span class="command">Ctrl + E</span>'
               + '<span class="same-line-comment">Comment</span>'
               + '<div class="small-comment">Small comment</div></div></div>'

               + '<details><summary class="header"><span class="icon">➤</span>'
               + ' collapsible</summary></details></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_nested_collapsible_with_content_in_nested(self):
        coll = ['>l➤ collapsible\n',
                '    >l➤ collapsible\n',
                '        /Ctrl + E /* Comment */ /** Small comment **/\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> '
               + 'collapsible</summary>'

               + '<details><summary class="header"><span class="icon">➤</span>'
               + ' collapsible</summary>'

               + '<div class="entry"><div class="command-box">'
               + '<span class="command">Ctrl + E</span>'
               + '<span class="same-line-comment">Comment</span>'
               + '<div class="small-comment">Small comment</div></div></div>'
               + '</details></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    def test_nested_collapsible_with_content_in_both(self):
        coll = ['>l➤ collapsible\n',
                '    /Ctrl + E /* Comment */ /** Small comment **/\n',
                '    >l➤ collapsible\n',
                '        /Ctrl + E /* Comment */ /** Small comment **/\n', '']
        exp = ('<div class="collapsible-box-half-left"><details>'
               + '<summary class="header"><span class="icon">➤</span> '
               + 'collapsible</summary>'

               + '<div class="entry"><div class="command-box">'
               + '<span class="command">Ctrl + E</span>'
               + '<span class="same-line-comment">Comment</span>'
               + '<div class="small-comment">Small comment</div></div></div>'

               + '<details><summary class="header"><span class="icon">➤</span>'
               + ' collapsible</summary>'

               + '<div class="entry"><div class="command-box">'
               + '<span class="command">Ctrl + E</span>'
               + '<span class="same-line-comment">Comment</span>'
               + '<div class="small-comment">Small comment</div>'
               + '</div></div></details></details></div>')
        paml2html.identify_element(coll, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, exp)

    # Command

    def test_command_no_comments(self):
        comm = ['/Ctrl + E\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span></div>')
        paml2html.identify_element(comm, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_with_comment(self):
        comm = ['/Ctrl + E /* Comment */\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><span class="same-line-comment">Comment'
                    + '</span></div>')
        paml2html.identify_element(comm, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_with_small_comment(self):
        comm = ['/Ctrl + E /** Small comment **/\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><div class="small-comment">Small comment</div>'
                    + '</div>')
        paml2html.identify_element(comm, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_with_both_comments(self):
        comm = ['/Ctrl + E /* Comment */ /** Small comment **/\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><span class="same-line-comment">Comment</span>'
                    + '<div class="small-comment">Small comment</div></div>')
        paml2html.identify_element(comm, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Code line

    def test_code_line_no_comments(self):
        line = ['```\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><code class="line-code">'
                    + 'This is a code line</code></div>')
        paml2html.identify_element(line, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_with_comment(self):
        line = ['```/* Comment */\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-comment"'
                    + '>Comment</div><code class="line-code">This is a code '
                    + 'line</code></div>')
        paml2html.identify_element(line, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_with_small_comment(self):
        line = ['```/** Small comment **/\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-small-'
                    + 'comment">Small comment</div><code class="line-code">'
                    + 'This is a code line</code></div>')
        paml2html.identify_element(line, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_with_both_comments(self):
        line = ['```/* Comment *//** Small comment **/\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-comment"'
                    + '>Comment</div><div class="line-code-small-comment">'
                    + 'Small comment</div><code class="line-code">This is a '
                    + 'code line</code></div>')
        paml2html.identify_element(line, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Code block

    def test_code_block_no_comments(self):
        block = ["```\n",
                 "This is a code block\n",
                 "with no comment.\n",
                 "```\n",
                 ""]
        expected = ('<div class="block-code-box"><code class="block-code">'
                    + '<pre>This is a code block\n'
                    + 'with no comment.</pre></code></div>')
        paml2html.identify_element(block, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_with_comment(self):
        block = ['```/* Comment */\n',
                 'This is a code block\n',
                 'with a comment.\n',
                 '```\n',
                 '']
        expected = ('<div class="block-code-box">'
                    + '<div class="block-code-comment">Comment</div>'
                    + '<code class="block-code"><pre>This is a code block\n'
                    + 'with a comment.</pre></code></div>')
        paml2html.identify_element(block, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_with_small_comment(self):
        block = ['```/** Small comment **/\n',
                 'This is a code block\n',
                 'with a comment.\n',
                 '```\n',
                 '']
        expected = ('<div class="block-code-box">'
                    + '<div class="block-code-small-comment">Small comment'
                    + '</div><code class="block-code">'
                    + '<pre>This is a code block\n'
                    + 'with a comment.</pre></code></div>')
        paml2html.identify_element(block, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_with_both_comments(self):
        block = ['```/** Small comment **/\n',
                 'This is a code block\n',
                 'with a comment.\n',
                 '```\n',
                 '']
        expected = ('<div class="block-code-box">'
                    + '<div class="block-code-small-comment">'
                    + 'Small comment</div><code class="block-code">'
                    + '<pre>This is a code block\n'
                    + 'with a comment.</pre></code></div>')
        paml2html.identify_element(block, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Images

    def test_image(self):
        image = ['![alt text](image.png)\n',
                 '']
        expected = '<img alt="alt text" src="image.png" />'
        paml2html.identify_element(image, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Paragraphs

    def test_empty_paragraph(self):
        para = ['{\n', '}\n', '']
        expected = '<div class="paragraph"><p></p></div>'
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_empty_one_line_paragraph(self):
        para = ['{\n', '\n', '}\n', '']
        expected = '<div class="paragraph"><p></p></div>'
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_single_line_paragraph(self):
        para = ['{\n',
                'Simple paragraph\n',
                '}\n',
                '']
        expected = '<div class="paragraph"><p>Simple paragraph</p></div>'
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_single_line_paragraph_with_indentation(self):
        # The output should look exactly the same, as the indentation is only
        # for visual purposes

        para = ['{\n',
                '    Paragraph with 4 spaces\n',
                '}\n',
                '']
        expected = ('<div class="paragraph">'
                    + '<p>Paragraph with 4 spaces</p></div>')
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_multi_line_paragraph(self):
        para = ['{\n',
                'Paragraph with no indentation\n',
                '\n',
                'Second paragraph\n',
                '}\n',
                '']
        expected = ('<div class="paragraph"><p>Paragraph with no indentation'
                    + '<br><br>Second paragraph</p></div>')
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_multi_line_paragraph_with_indentation(self):
        # The output should look exactly the same, as the indentation is only
        # for visual purposes

        para = ['{\n',
                '    Paragraph with 4 spaces\n',
                '\n',
                '    Second paragraph with 4 spaces\n',
                '}\n',
                '']
        expected = ('<div class="paragraph"><p>Paragraph with 4 spaces'
                    + '<br><br>Second paragraph with 4 spaces</p></div>')
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_single_line_paragraph_with_left_picture(self):
        para = ['{!l[alt text](image.png)\n',
                'some text\n',
                '}\n',
                '']
        expected = ('<div class="paragraph"><img alt="alt text" '
                    + 'src="image.png" class="img-half-left" />'
                    + '<p>some text</p></div>')
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_single_line_paragraph_with_right_picture(self):
        para = ['{!r[alt text](image.png)\n',
                'some text\n',
                '}\n',
                '']
        expected = ('<div class="paragraph"><img alt="alt text" '
                    + 'src="image.png" class="img-half-right" />'
                    + '<p>some text</p></div>')
        paml2html.identify_element(para, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Unordered lists

    def test_unordered_list_with_single_element(self):
        ulist = ['- Element\n', '']
        expected = '<ul><li>Element</li></ul>'
        paml2html.identify_element(ulist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_list_with_multiple_elements(self):
        ulist = ['- Element 1\n',
                 '- Element 2\n',
                 '- Element 3\n',
                 '']
        expected = ('<ul><li>Element 1</li>'
                    + '<li>Element 2</li>'
                    + '<li>Element 3</li></ul>')
        paml2html.identify_element(ulist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_list_nested(self):
        ulist = ['- Element 1\n',
                 '    - Subelement\n',
                 '- Element 2\n', '']
        expected = ('<ul><li>Element 1</li>'
                    + '<ul><li>Subelement</li></ul>'
                    + '<li>Element 2</li></ul>')
        paml2html.identify_element(ulist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_list_nested_two_levels(self):
        ulist = ['- Element 1\n',
                 '    - Subelement 1\n',
                 '        - Subsubelement\n',
                 '    - Subelement 2\n',
                 '- Element 2\n', '']
        expected = ('<ul><li>Element 1</li>'
                    + '<ul><li>Subelement 1</li>'
                    + '<ul><li>Subsubelement</li></ul>'
                    + '<li>Subelement 2</li></ul>'
                    + '<li>Element 2</li></ul>')
        paml2html.identify_element(ulist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Ordered lists

    def test_ordered_list_with_single_element(self):
        olist = ['1. Element\n', '']
        expected = ('<ol><li>Element</li></ol>')
        paml2html.identify_element(olist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_list_with_multiple_element(self):
        olist = ['1. Element\n',
                 '2. Element\n',
                 '3. Element\n',
                 '']
        expected = ('<ol><li>Element</li>'
                    + '<li>Element</li>'
                    + '<li>Element</li></ol>')
        paml2html.identify_element(olist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_list_nested(self):
        olist = ['1. Element 1\n',
                 '    1. Subelement\n',
                 '2. Element 2\n', '']
        expected = ('<ol><li>Element 1</li>'
                    + '<ol><li>Subelement</li></ol>'
                    + '<li>Element 2</li></ol>')
        paml2html.identify_element(olist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_list_nested_two_levels(self):
        olist = ['1. Element 1\n',
                 '    1. Subelement 1\n',
                 '        1. Subsubelement\n',
                 '    2. Subelement 2\n',
                 '2. Element 2\n', '']
        expected = ('<ol><li>Element 1</li>'
                    + '<ol><li>Subelement 1</li>'
                    + '<ol><li>Subsubelement</li></ol>'
                    + '<li>Subelement 2</li></ol>'
                    + '<li>Element 2</li></ol>')
        paml2html.identify_element(olist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Mixed lists

    def test_mixed_list_one_level_starting_unordered(self):
        mlist = ['- Element 1\n',
                 '    1. Subelement 1\n',
                 '- Element 2\n', '']
        expected = ('<ul><li>Element 1</li>'
                    + '<ol><li>Subelement 1</li></ol>'
                    + '<li>Element 2</li></ul>')
        paml2html.identify_element(mlist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_two_levels_starting_unordered(self):
        mlist = ['- Element 1\n',
                 '    1. Subelement 1\n',
                 '        - Subsubelement\n',
                 '    2. Subelement 2\n',
                 '- Element 2\n', '']
        expected = ('<ul><li>Element 1</li>'
                    + '<ol><li>Subelement 1</li>'
                    + '<ul><li>Subsubelement</li></ul>'
                    + '<li>Subelement 2</li></ol>'
                    + '<li>Element 2</li></ul>')
        paml2html.identify_element(mlist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_one_level_starting_ordered(self):
        mlist = ['1. Element 1\n',
                 '    - Subelement 1\n',
                 '2. Element 2\n', '']
        expected = ('<ol><li>Element 1</li>'
                    + '<ul><li>Subelement 1</li></ul>'
                    + '<li>Element 2</li></ol>')
        paml2html.identify_element(mlist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_two_levels_starting_ordered(self):
        mlist = ['1. Element 1\n',
                 '    - Subelement 1\n',
                 '        1. Subsubelement\n',
                 '    - Subelement 2\n',
                 '2. Element 2\n', '']
        expected = ('<ol><li>Element 1</li>'
                    + '<ul><li>Subelement 1</li>'
                    + '<ol><li>Subsubelement</li></ol>'
                    + '<li>Subelement 2</li></ul>'
                    + '<li>Element 2</li></ol>')
        paml2html.identify_element(mlist, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Tables

    def test_table_with_headers(self):
        table = ['| Head2 | 2Head |\n',
                 '| ----- | ----- |\n',
                 '| text  | text2 |\n',
                 '']
        expected = ('<table><tr><th>Head2</th><th>2Head</th></tr>'
                    + '<tr><td>text</td><td>text2</td></tr></table>')
        paml2html.identify_element(table, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_table_without_headers(self):
        table = ['| a | b |\n',
                 '| c | d |\n',
                 '']
        expected = ('<table><tr><td>a</td><td>b</td>'
                    + '</tr><tr><td>c</td><td>d</td></tr></table>')
        paml2html.identify_element(table, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    # Raw HTML

    def test_raw_html_empty(self):
        html = ['<\n', '>\n', '']
        expected = ''
        paml2html.identify_element(html, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_raw_html_empty_line(self):
        html = ['<\n', '\n', '>\n', '']
        expected = ''
        paml2html.identify_element(html, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_raw_html_content_line(self):
        html = ['<\n',
                '<p>A paragraph</p>\n',
                '>\n', '']
        expected = '<p>A paragraph</p>'
        paml2html.identify_element(html, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_raw_html_content_multiple_lines(self):
        html = ['<\n',
                '<p>A paragraph</p>\n',
                '<div>A div</div>\n',
                '>\n', '']
        expected = '<p>A paragraph</p><div>A div</div>'
        paml2html.identify_element(html, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_raw_html_content_multiple_lines_with_breaks(self):
        html = ['<\n',
                '<p>A paragraph</p>\n',
                '\n',
                '<div>A div</div>\n',
                '>\n', '']
        expected = '<p>A paragraph</p><div>A div</div>'
        paml2html.identify_element(html, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
