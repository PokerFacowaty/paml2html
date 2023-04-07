paml2html is a converter making HTML from [P]oker's M[a]de-up [M]arkup [L]anguage that's designed to be used [on my website](https://pokerfacowaty.com/) as well as being a fun little learning experience. PaML's docs can be found [here](https://paml.pokerfacowaty.com/). You can also track PaML's & paml2html's development on my [Vikunja list!](https://vikunja.pokerfacowaty.com/share/xSbQeLXtVLmTpqdniQhIjmzLUgdxJwtpUStgIbya/auth)

# Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [yattag](https://www.yattag.org/) (`pip install yattag`)

# Installation
Download the files
- Grab the [latest release](https://github.com/PokerFacowaty/paml2html/releases)
- Alternatively, since paml2html is [available on PyPI](https://pypi.org/project/paml2html/), if you intend to only use it as as an imported package, you can install it with pip
```
pip install paml2html
```

# Usage
To use paml2html by itself, simply start it when in the same directory:
```
python paml2html.py <source_file> <destination_file>
```
(remember to use the relevant Python installation, which might be `python3` or other on your system)

...or you can also import it and use in a different file with `import paml2html` by calling the `paml2html.convert_from_file()` or `paml2html.convert_from_text()` function and providing a filepath or text accordingly


## Arguments
`paml2html.py [-h] [--indent INDENT] source_file destination_file`

- `-h, --help` - show help
- `--indent <number>` - the optional amount of spaces used to indent the HTML file, indentation is off by default
- `source_file` - source text file containing PaML content
- `destination_file` - file for the resulting HTML content
