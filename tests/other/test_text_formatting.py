from src.paml2html import paml2html
import unittest

'''This is the place for all tests related to complex text formatting using
   format_txt(), such as mixing text decorators, decorating links etc. They are
   separated from unit tests as I, following the advice of my neighborhood
   tester, figured it would look cleaner and more organized this way.

   These start with obscure tests with just text (like decorations overlapping)
   and later on elements such as lists are only tested with basic links and
   basic formatting, since they call the same format_txt function with text for
   basic and advanced formatting, the latter having been tested on just text in
   the early tests. There is no need to test if a link with an overlapping
   decorations inside works in a doubly-nested list.

   A rule of thumb for wheter a test is too obscure is usually whether GitHub
   flavored markdown passes it. I've left some in that failed to conform to
   this rule since they are an effect of the way paml2html works and didn't
   need any changes. All of them have appriopriate docstrings.
   '''


class TestPaml(unittest.TestCase):
    def test_text_bold_and_italics(self):
        paml = '**__bold and italics__**'
        expected = '<b><i>bold and italics</i></b>'
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_text_bold_and_italics_reversed_ending(self):
        paml = '**__bold and italics**__'
        expected = '<b><i>bold and italics</b></i>'
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_text_bold_and_italics_partially_overlapping(self):
        '''GitHub flavored Markdown doesn't process this one properly, but it
        works like a charm with paml. My guess is having __ as italics instead
        of * could've helped here.'''
        paml = '**over__lap**ping__'
        expected = '<b>over<i>lap</b>ping</i>'
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_inside(self):
        paml = '[**link in bold**](https://pokerfacowaty.com)'
        expected = ('<a target="_blank" href="https://pokerfacowaty.com">'
                    + '<b>link in bold</b></a>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_outside(self):
        paml = '**[link in bold](https://pokerfacowaty.com)**'
        expected = ('<b><a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link in bold</a></b>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_italics_inside(self):
        paml = '[__link in italics__](https://pokerfacowaty.com)'
        expected = ('<a target="_blank" href="https://pokerfacowaty.com">'
                    + '<i>link in italics</i></a>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_italics_outside(self):
        paml = '__[link in italics](https://pokerfacowaty.com)__'
        expected = ('<i><a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link in italics</a></i>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_and_italics_inside(self):
        paml = '[**__link in bold and italics__**](https://pokerfacowaty.com)'
        expected = ('<a target="_blank" href="https://pokerfacowaty.com"><b>'
                    + '<i>link in bold and italics</i></b></a>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_and_italics_outside(self):
        paml = '**__[link in bold and italics](https://pokerfacowaty.com)__**'
        expected = ('<b><i><a target="_blank" href="https://pokerfacowaty.com"'
                    + '>link in bold and italics</a></i></b>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_and_italics_reversed_ending_inside(self):
        paml = '[**__link in bold and italics**__](https://pokerfacowaty.com)'
        expected = ('<a target="_blank" href="https://pokerfacowaty.com"><b>'
                    + '<i>link in bold and italics</b></i></a>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_and_italics_reversed_ending_outside(self):
        paml = '**__[link in bold and italics](https://pokerfacowaty.com)**__'
        expected = ('<b><i><a target="_blank" href="https://pokerfacowaty.com"'
                    + '>link in bold and italics</a></b></i>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_link_bold_and_italics_partially_overlapping_inside(self):
        '''See test_text_bold_and_italics_partially_overlapping(). Not making
        an outside version like **over[__lapp**ing__]() since that doesn't work
        on GitHub either and is madness that will never be used here.'''
        paml = '[**over__lap**ping__](https://pokerfacowaty.com)'
        expected = ('<a target="_blank" href="https://pokerfacowaty.com">'
                    + '<b>over<i>lap</b>ping</i></a>')
        result = paml2html.format_txt(paml)
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def header_with_link(self):
        paml = ['# [link](https://pokerfacowaty.com)\n', '']
        expected = ('<h1><a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></h1>')
        paml2html.add_header(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_header_in_italics(self):
        paml = ['# __Italics__\n', '']
        expected = ('<h1><i>Italics</i></h1>')
        paml2html.add_header(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_comment_link(self):
        paml = ['/Ctrl + E /* [link](https://pokerfacowaty.com) */\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><span class="same-line-comment"><a '
                    + 'target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></span></div>')
        paml2html.add_command(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_small_comment_link(self):
        paml = ['/Ctrl + E /** [link](https://pokerfacowaty.com) **/\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><div class="small-comment"><a '
                    + 'target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></div></div>')
        paml2html.add_command(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_comment_italics(self):
        paml = ['/Ctrl + E /* __Italics__ */\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><span class="same-line-comment"><i>Italics</i>'
                    + '</span></div>')
        paml2html.add_command(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_command_small_comment_italics(self):
        paml = ['/Ctrl + E /** __Italics__ **/\n', '']
        expected = ('<div class="command-box"><span class="command">Ctrl + E'
                    + '</span><div class="small-comment"><i>Italics</i></div>'
                    + '</div>')
        paml2html.add_command(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_comment_link(self):
        paml = ['```/* [link](https://pokerfacowaty.com) */\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-comment"'
                    + '><a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></div><code class="line-code">This is a code '
                    + 'line</code></div>')
        paml2html.add_code_line(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_small_comment_link(self):
        paml = ['```/** [link](https://pokerfacowaty.com) **/\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-small-'
                    + 'comment"><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></div><code class="line-code">This is a '
                    + 'code line</code></div>')
        paml2html.add_code_line(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_comment_italics(self):
        paml = ['```/* __Italics__ */\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-comment"'
                    + '><i>Italics</i></div><code class="line-code">This is a '
                    + 'code line</code></div>')
        paml2html.add_code_line(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_line_small_comment_italics(self):
        paml = ['```/** __Italics__ **/\n',
                'This is a code line\n',
                '```\n', '']
        expected = ('<div class="line-code-box"><div class="line-code-small-'
                    + 'comment"><i>Italics</i></div><code class="line-code">'
                    + 'This is a code line</code></div>')
        paml2html.add_code_line(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_comment_link(self):
        paml = ['```/* [link](https://pokerfacowaty.com) */\n',
                'This is\n',
                'a code block\n',
                '```\n', '']
        expected = ('<div class="block-code-box"><div class="block-code-'
                    + 'comment"><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></div><code class="block-code"><pre>This '
                    + 'is\na code block</pre></code></div>')
        paml2html.add_code_block(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_small_comment_link(self):
        paml = ['````/** [link](https://pokerfacowaty.com) **/\n',
                'This is\n',
                'a code block\n',
                '```\n', '']
        expected = ('<div class="block-code-box"><div class="block-code-small-'
                    + 'comment"><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></div><code class="block-code"><pre>This'
                    + ' is\na code block</pre></code></div>')
        paml2html.add_code_block(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_comment_italics(self):
        paml = ['```/* __Italics__ */\n',
                'This is\n',
                'a code block\n',
                '```\n', '']
        expected = ('<div class="block-code-box"><div class="block-code-'
                    + 'comment"><i>Italics</i></div><code class="block-code">'
                    + '<pre>This is\na code block</pre></code></div>')
        paml2html.add_code_block(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_code_block_small_comment_italics(self):
        paml = ['```/** __Italics__ **/\n',
                'This is\n',
                'a code block\n',
                '```\n', '']
        expected = ('<div class="block-code-box"><div class="block-code-small-'
                    + 'comment"><i>Italics</i></div><code class="block-code">'
                    + '<pre>This is\na code block</pre></code></div>')
        paml2html.add_code_block(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_paragraph_link(self):
        paml = ['```{\n',
                '[link](https://pokerfacowaty.com)\n',
                '}\n', '']
        expected = ('<div class="paragraph"><p><a target="_blank" '
                    + 'href="https://pokerfacowaty.com">link</a></p></div>')
        paml2html.add_paragraph(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_paragraph_italics(self):
        paml = ['{\n',
                '__Italics__\n',
                '}\n', '']
        expected = '<div class="paragraph"><p><i>Italics</i></p></div>'
        paml2html.add_paragraph(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_list_link(self):
        paml = ['- [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ul><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li></ul>')
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_nested_list_link(self):
        paml = ['- [link](https://pokerfacowaty.com)\n',
                '    - [link](https://pokerfacowaty.com)\n',
                '- [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ul><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li><ul><li><a target="_blank" href='
                    + '"https://pokerfacowaty.com">link</a></li></ul><li>'
                    + '<a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></li></ul>')
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_list_italics(self):
        paml = ['- __Italics__\n', '']
        expected = '<ul><li><i>Italics</i></li></ul>'
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_unordered_nested_list_italics(self):
        paml = ['- __Italics__\n',
                '    - __Italics__\n',
                '- __Italics__\n', '']
        expected = ('<ul><li><i>Italics</i></li>'
                    + '<ul><li><i>Italics</i></li></ul>'
                    + '<li><i>Italics</i></li></ul>')
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_list_link(self):
        paml = ['1. [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ol><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li></ol>')
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_nested_list_link(self):
        paml = ['1. [link](https://pokerfacowaty.com)\n',
                '    1. [link](https://pokerfacowaty.com)\n',
                '2. [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ol><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li><ol><li><a target="_blank" '
                    + 'href="https://pokerfacowaty.com">link</a></li></ol><li>'
                    + '<a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></li></ol>')
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_list_italics(self):
        paml = ['1. __Italics__\n', '']
        expected = '<ol><li><i>Italics</i></li></ol>'
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_ordered_nested_list_italics(self):
        paml = ['1. __Italics__\n',
                '    1. __Italics__\n',
                '2. __Italics__\n', '']
        expected = ('<ol><li><i>Italics</i></li>'
                    + '<ol><li><i>Italics</i></li></ol>'
                    + '<li><i>Italics</i></li></ol>')
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_links_starting_unordered(self):
        paml = ['- [link](https://pokerfacowaty.com)\n',
                '    1. [link](https://pokerfacowaty.com)\n',
                '- [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ul><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li><ol><li><a target="_blank" href="'
                    + 'https://pokerfacowaty.com">link</a></li></ol><li>'
                    + '<a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></li></ul>')
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_links_starting_ordered(self):
        paml = ['1. [link](https://pokerfacowaty.com)\n',
                '    - [link](https://pokerfacowaty.com)\n',
                '2. [link](https://pokerfacowaty.com)\n', '']
        expected = ('<ol><li><a target="_blank" href="https://pokerfacowaty'
                    + '.com">link</a></li><ul><li><a target="_blank" href="'
                    + 'https://pokerfacowaty.com">link</a></li></ul><li>'
                    + '<a target="_blank" href="https://pokerfacowaty.com">'
                    + 'link</a></li></ol>')
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_italics_starting_unordered(self):
        paml = ['- __Italics__\n',
                '    1. __Italics__\n',
                '- __Italics__\n', '']
        expected = ('<ul><li><i>Italics</i></li>'
                    + '<ol><li><i>Italics</i></li></ol>'
                    + '<li><i>Italics</i></li></ul>')
        paml2html.add_unordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_mixed_list_italics_starting_ordered(self):
        paml = ['1. __Italics__\n',
                '    - __Italics__\n',
                '2. __Italics__\n', '']
        expected = ('<ol><li><i>Italics</i></li>'
                    + '<ul><li><i>Italics</i></li>'
                    + '</ul><li><i>Italics</i></li></ol>')
        paml2html.add_ordered_list(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_table_with_headers_links(self):
        paml = ['| [link](example.com) | [link](example.com) |\n',
                '|         ---         |         ---         |\n',
                '| [link](example.com) | [link](example.com) |\n', '']
        expected = ('<table><tr><th><a target="_blank" href="example.com">'
                    + 'link</a></th><th><a target="_blank" href="example.com">'
                    + 'link</a></th></tr><tr><td><a target="_blank" href="'
                    + 'example.com">link</a></td><td><a target="_blank" '
                    + 'href="example.com">link</a></td></tr></table>')
        paml2html.add_table(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_table_with_headers_italics(self):
        paml = ['| __Italics__ | __Italics__ |\n',
                '|     ---     |     ---     |\n',
                '| __Italics__ | __Italics__ |\n', '']
        expected = ('<table><tr><th><i>Italics</i></th><th><i>Italics</i>'
                    + '</th></tr><tr><td><i>Italics</i></td><td><i>Italics</i>'
                    + '</td></tr></table>')
        paml2html.add_table(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_table_without_headers_links(self):
        paml = ['| [link](example.com) | [link](example.com) |\n',
                '| [link](example.com) | [link](example.com) |\n', '']
        expected = ('<table><tr><td><a target="_blank" href="example.com">link'
                    + '</a></td><td><a target="_blank" href="example.com">link'
                    + '</a></td></tr><tr><td><a target="_blank" href="example'
                    + '.com">link</a></td><td><a target="_blank" href="example'
                    + '.com">link</a></td></tr></table>')
        paml2html.add_table(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)

    def test_table_without_headers_italics(self):
        paml = ['| __Italics__ | __Italics__ |\n',
                '| __Italics__ | __Italics__ |\n', '']
        expected = ('<table><tr><td><i>Italics</i></td><td><i>Italics</i></td>'
                    + '</tr><tr><td><i>Italics</i></td><td><i>Italics</i></td>'
                    + '</tr></table>')
        paml2html.add_table(paml, 0)
        result = paml2html.doc.getvalue()
        (paml2html.doc, paml2html.tag,
         paml2html.text, paml2html.line) = paml2html.Doc().ttl()
        self.assertEqual(result, expected)
