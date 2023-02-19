from html import escape
from yattag import Doc, indent
import argparse


def main():
    '''Used when calling the converter directly'''
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file",
                        help="Provide a .paml file used for conversion")
    parser.add_argument("destination_file",
                        help="Provide an .html destination file. It will be"
                        + "appended if it exists and created if it doesn't")
    parser.add_argument("--indent",
                        help="Provide the amount of spaces used for"
                        + "indentation. Indentation is disabled by default",
                        type=int, default=None)
    args = parser.parse_args()
    source_file = args.source_file
    destination_file = args.destination_file
    if args.indent is not None:
        indnt = ' ' * args.indent

    convert_from_file(source_file)

    with open(destination_file, 'a+', encoding='utf-8') as f:
        if args.indent is not None:
            f.write(indent(doc.getvalue(), indentation=indnt))
        elif args.indent is None:
            f.write(doc.getvalue())


def convert_from_file(filepath):
    '''Used when the converter is imported'''

    global doc, tag, text, line
    doc, tag, text, line = Doc().ttl()

    with open(filepath, 'r', encoding='utf-8') as p:
        paml_lines = p.readlines()
        if not paml_lines:
            return ''
        elif paml_lines[-1] != '':
            paml_lines[-1] += '\n'
            paml_lines.append('')

    i = 0
    while i < len(paml_lines):
        i = identify_element(paml_lines, i)

    return doc.getvalue()


def convert_from_text(paml_text):
    '''Used when the converter is imported'''

    global doc, tag, text, line
    doc, tag, text, line = Doc().ttl()

    paml_lines = paml_text.splitlines()
    if not paml_lines:
        return ''
    elif paml_lines[-1] != '':
        paml_lines[-1] += '\n'
        paml_lines.append('')

    i = 0
    while i < len(paml_lines):
        i = identify_element(paml_lines, i)

    return doc.getvalue()


def identify_element(paml_lines, i):
    # Wanted to switch it into a dict of identifiers, but the solution that
    # works for different lengths of starting points (e.x. '#' vs '```') that
    # I came up with was over 4 times slower than these elifs
    if paml_lines[i].strip() == '':
        # only spaces and \n on the line
        i += 1
    elif paml_lines[i].lstrip().startswith('#'):
        i = add_header(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('>'):
        i = add_collapsible_box(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('/'):
        i = add_command(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('```'):
        # inline code is handled as part of format_txt
        i = add_code(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('!['):
        i = add_image(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('{'):
        i = add_paragraph(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('-'):
        i = add_unordered_list(paml_lines, i)
    elif paml_lines[i].lstrip()[0] in '0123456789':
        i = add_ordered_list(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('|'):
        i = add_table(paml_lines, i)
    elif paml_lines[i].lstrip().startswith('<'):
        i = add_raw_html(paml_lines, i)
    else:
        print('Unsupported line, skipping: ', paml_lines[i])
        i += 1  # fail-safe in case something is not recognized
    return i


def add_header(paml_lines, i):
    if paml_lines[i].rstrip().startswith('# '):
        with tag('h1'):
            doc.asis(format_txt(paml_lines[i][2:-1]))
        i += 1
    elif paml_lines[i].rstrip().startswith('## '):
        with tag('h2'):
            doc.asis(format_txt(paml_lines[i][3:-1]))
        i += 1
    elif paml_lines[i].rstrip().startswith('### '):
        with tag('h3'):
            doc.asis(format_txt(paml_lines[i][4:-1]))
        i += 1
    elif paml_lines[i].rstrip().startswith('#### '):
        with tag('h4'):
            doc.asis(format_txt(paml_lines[i][5:-1]))
        i += 1
    elif paml_lines[i].rstrip().startswith('##### '):
        with tag('h5'):
            doc.asis(format_txt(paml_lines[i][6:-1]))
        i += 1
    elif paml_lines[i].rstrip().startswith('###### '):
        with tag('h6'):
            doc.asis(format_txt(paml_lines[i][7:-1]))
        i += 1
    return i


def add_collapsible_box(paml_lines, i):
    tag_class = ''
    position = ''
    if paml_lines[i][1] == "l":
        position = "l"
        tag_class = "collapsible-box-half-left"
    elif paml_lines[i][1] == "r":
        position = "r"
        tag_class = "collapsible-box-half-right"
    elif paml_lines[i][1] == "f":
        position = "f"
        tag_class = "collapsible-box-full"

    with tag('div', klass=tag_class):
        while i < len(paml_lines):
            if (paml_lines[i] == ''
               or paml_lines[i].lstrip()[0] != '>'
               or paml_lines[i][0].lstrip() == '>'
               and paml_lines[i].lstrip()[1] != position):
                break
            with tag('details'):
                with tag('summary', klass='header'):
                    with tag('span', klass='icon'):
                        text(paml_lines[i].lstrip()[2])
                    text(paml_lines[i].lstrip()[3:].rstrip())
                    i += 1
                i = add_collapsible(paml_lines, i)
    return i


def add_collapsible(paml_lines, i, offset=0):
    while i < len(paml_lines):
        if paml_lines[i] == '\n':
            i += 1
            continue

        spaces = 0
        for char in paml_lines[i]:
            if char == ' ':
                spaces += 1
            else:
                break

        if spaces == 0:
            break
        elif spaces != offset:
            offset = spaces
        elif spaces == offset:
            with tag('div', klass='entry'):
                i = identify_element(paml_lines, i)
    return i


def add_command(paml_lines, i):
    with tag('span', klass='command'):
        doc.asis(format_txt(paml_lines[i].lstrip()
                            [1:paml_lines[i].lstrip().find('/*')]).rstrip())

    if '/*' in paml_lines[i]:
        with tag('span', klass='same-line-comment'):
            doc.asis(format_txt(paml_lines[i]
                                [paml_lines[i].find('/*') + 2:
                                 paml_lines[i].find('*/')]))
    if '/**' in paml_lines[i]:
        with tag('div', klass='small-comment'):
            doc.asis(format_txt(paml_lines[i]
                                [paml_lines[i].find('/**') + 3:
                                 paml_lines[i].find('**/')]))

    i += 1
    return i


def add_code(paml_lines, i):
    if paml_lines[i + 2].rstrip().endswith('```'):
        # code line
        i = add_code_line(paml_lines, i)
    else:
        # code block
        i = add_code_block(paml_lines, i)

    return i


def add_code_line(paml_lines, i):
    if ('/*' in paml_lines[i]
       and paml_lines[i][paml_lines[i].find('/*') + 2] != '*'):
        # making sure '/**' isn't recognized as '/*' when '/*' is not there
        with tag('div', klass='line-code-comment'):
            doc.asis(format_txt(paml_lines[i]
                     [paml_lines[i].find('/*') + 2:
                     paml_lines[i].find('*/')].strip()))

    if '/**' in paml_lines[i]:
        with tag('div', klass='line-code-small-comment'):
            doc.asis(format_txt(paml_lines[i]
                     [paml_lines[i].find('/**') + 3:
                     paml_lines[i].find('**/')].strip()))
    i += 1
    with tag('code', klass='line-code'):
        text(paml_lines[i].lstrip())
    i += 2
    return i


def add_code_block(paml_lines, i):
    if ('/*' in paml_lines[i]
       and paml_lines[i][paml_lines[i].find('/*') + 2] != '*'):
        # making sure '/**' isn't recognized as '/*' when '/*' is not there
        with tag('div', klass='block-code-comment'):
            doc.asis(format_txt(paml_lines[i]
                     [paml_lines[i].find('/*') + 2:
                     paml_lines[i].find('*/')].strip()))

    if '/**' in paml_lines[i]:
        with tag('div', klass='block-code-small-comment'):
            doc.asis(format_txt(paml_lines[i]
                     [paml_lines[i].find('/**') + 3:
                     paml_lines[i].find('**/')].strip()))
    i += 1
    code_to_add = []
    while i < len(paml_lines):
        if paml_lines[i].strip() == '```':
            # code_to_add.append(paml_lines[i][:paml_lines[i].find('```')])
            with tag('code', klass='block-code'):
                with tag('pre'):
                    text(''.join(code_to_add))
            i += 1
            break
        else:
            code_to_add.append(paml_lines[i])
        i += 1
    return i


def add_image(paml_lines, i):
    if paml_lines[i][0] == '{':
        line = paml_lines[i][1:]
    else:
        line = paml_lines[i]

    if line.lstrip().startswith('!l'):
        kls = 'img-half-left'
    elif line.lstrip().startswith('!r'):
        kls = 'img-half-right'
    else:
        kls = None

    if kls is not None:
        doc.stag('img', alt=line[line.find('[') + 1:line.find(']')],
                 src=line[line.find('(') + 1:line.find(')')], klass=kls)
    else:
        doc.stag('img', alt=line[line.find('[') + 1:line.find(']')],
                 src=line[line.find('(') + 1:line.find(')')])
    i += 1
    return i


def add_paragraph(paml_lines, i):
    with tag('div', klass='paragraph'):
        if paml_lines[i].lstrip()[1] == '!':
            i = add_image(paml_lines, i)
        else:
            i += 1
        with tag('p'):
            text_to_add = ""
            while i < len(paml_lines):
                if paml_lines[i].strip() == "}":
                    break
                else:
                    text_to_add += paml_lines[i]
                i += 1
            text_to_add = '<br>'.join(text_to_add.splitlines())
            doc.asis(format_txt(text_to_add))
    i += 1
    return i


def add_unordered_list(paml_lines, i, offset=None):
    if offset is None:
        # check where the list is positioned if it's not explicitly stated
        # this helps with e.x. lists inside collapsibles
        offset = 0
        for char in paml_lines[i]:
            if char == ' ':
                offset += 1
            else:
                break

    with tag('ul'):
        while i < len(paml_lines):
            if paml_lines[i].strip() == '':
                break
            elif (paml_lines[i].lstrip()[0] != '-'
                  and not paml_lines[i].lstrip()[0].isnumeric()):
                break

            spaces = 0
            for char in paml_lines[i]:
                if char == ' ':
                    spaces += 1
                else:
                    break
            if offset > 0 and spaces < offset:
                # going back
                offset = spaces
                break
            elif paml_lines[i][offset] == '-':
                # line('li', format_txt(paml_lines[i][offset + 2:-1]))
                with tag('li'):
                    doc.asis(format_txt(paml_lines[i][offset + 2:-1]))
                i += 1
            elif paml_lines[i][offset].isnumeric():
                i = add_ordered_list(paml_lines, i)
            elif paml_lines[i][spaces] == '-':
                i = add_unordered_list(paml_lines, i, spaces)
            elif paml_lines[i][spaces].isnumeric():
                i = add_ordered_list(paml_lines, i, spaces)
    return i


def add_ordered_list(paml_lines, i, offset=None):
    numbers = '0123456789'

    if offset is None:
        # check where the list is positioned if it's not explicitly stated
        # this helps with e.x. lists inside collapsibles
        offset = 0
        for char in paml_lines[i]:
            if char == ' ':
                offset += 1
            else:
                break

    with tag('ol'):
        while i < len(paml_lines):
            if paml_lines[i] == '\n':
                break
            elif (paml_lines[i].lstrip()[0] not in numbers
                  and paml_lines[i].lstrip()[0] != '-'):
                break

            spaces = 0
            for char in paml_lines[i]:
                if char == ' ':
                    spaces += 1
                else:
                    break

            if offset > 0 and spaces < offset:
                offset = spaces
                break
            elif paml_lines[i][offset] in numbers:
                line('li', format_txt(paml_lines[i][offset + 2:-1]))
                i += 1
            elif paml_lines[i][offset] == '-':
                i = add_unordered_list(paml_lines, i)
            elif paml_lines[i][spaces] in numbers:
                i = add_ordered_list(paml_lines, i, spaces)
            elif paml_lines[i][spaces] == '-':
                i = add_unordered_list(paml_lines, i, spaces)
    return i


def add_table(paml_lines, i):
    table_with_headers = True
    for cell in paml_lines[i + 1].split()[1:-1:2]:
        # [1:-1:2] - before first and after last not needed
        # every other to skip the dividers
        for char in cell:
            if char not in [' ', '-']:
                table_with_headers = False
                break
        break

    with tag('table'):
        if table_with_headers:
            with tag('tr'):
                for x in paml_lines[i].split('|')[1:-1]:
                    # [1:-1] - before first and after last not needed
                    with tag('th'):
                        doc.asis(format_txt(x.strip()))
                i += 2

        while i < len(paml_lines):
            if not paml_lines[i].lstrip().startswith('|'):
                break
            else:
                with tag('tr'):
                    for x in paml_lines[i].split('|')[1:-1]:
                        # [1:-1] - before first and after last not needed
                        with tag('td'):
                            doc.asis(format_txt(x.strip()))
                    i += 1
    return i


def add_raw_html(paml_lines, i):
    doc.asis('\n')
    i += 1
    while i < len(paml_lines):
        if paml_lines[i].strip() == '>':
            i += 1
            break
        else:
            doc.asis(paml_lines[i])
            i += 1
    return i


# using "txt" to not mix it with yattag's text by accident
def format_txt(txt):
    # always send asis
    txt = txt.strip()
    result = ''
    txt_components = []
    j = 0
    buffer = ''
    while j < len(txt):
        if txt[j:j+2] == '``':
            if buffer:
                txt_components.append(buffer)
                buffer = ''
            txt_components.append(txt[j:j + 1 + txt[j + 1:].find('``') + 2])
            j += len(txt_components[-1])
        elif txt[j] == '[' and txt[j:].find('](') != -1:
            if buffer:
                txt_components.append(buffer)
                buffer = ''
            link_component = ''
            # link_start and link_end refer to the actual link inside ()
            link_start = j + txt[j:].find('](')
            link_end = link_start + txt[link_start:].find(')')
            link_component = txt[j:link_end + 1]
            txt_components.append(link_component)
            j += len(txt_components[-1])
        elif j == len(txt) - 1:
            buffer += txt[j]
            txt_components.append(buffer)
            j += 1
            break
        else:
            buffer += txt[j]
            j += 1

    for t in txt_components:
        if t.startswith('``'):
            result += add_inline_code(t)
        elif t.startswith('[') and t.find('](') != -1:
            result += add_link(t)
        else:
            result += decorate_txt(t)

    return result


def add_inline_code(txt):
    result = ('<span class="inline-code">' + escape(txt[2:-2]) + "</span>")
    return result


def add_link(txt):
    result = ("<a class=\"links\" target=\"_blank\" href="
              + f"\"{txt[txt.find('(') + 1:txt.find(')')]}\">"
              + f"{format_txt(txt[txt.find('[') + 1:txt.find(']')])}</a>")
    return result


def decorate_txt(txt):
    tags = {"**": ("<b>", "</b>"), "__": ("<i>", "</i>"),
            "~~": ("<s>", "</s>")}
    result = txt
    i = 0
    while any((x in result for x in tags.keys())) and i < len(result):
        if result[i:i + 2] == "``":
            # special case for inline code since then any other styling needs
            # to be ignored
            tag_end = result.rfind("``")
            result = (result[:i] + tags[result[i:i + 2]][0]
                      + result[i + 2:tag_end] + tags[result[i:i + 2]][1]
                      + result[tag_end + 2:])
            i += result.rfind("</span>")
            continue
        elif result[i:i + 2] in tags.keys():
            # tag_start = result.find(result[i + 2])
            tag_end = result.rfind(result[i:i + 2])
            result = (result[:i] + tags[result[i:i + 2]][0]
                      + result[i + 2:tag_end] + tags[result[i:i + 2]][1]
                      + result[tag_end + 2:])
            # + 2 because of the length of **, __, ~~ etc might need rewriting,
            # but will work for now
        i += 1
    return result


if __name__ == '__main__':
    main()
