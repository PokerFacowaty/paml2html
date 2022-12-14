paml2html is a proof-of-concept converter making HTML from [P]oker's M[a]de-up [M]arkup [L]anguage. PaML docs can be found [here](https://paml.pokerfacowaty.com/)

# Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [yattag](https://www.yattag.org/) (`pip install yattag`)

# Installation
Download the files
- Clone the repo:
```
git clone https://github.com/PokerFacowaty/paml2html
```
- ... or simply download `paml2html.py`

# Usage
To use paml2html by itself, simply start it when in the same directory:

```
python paml2html.py
```
(or if you have Python 2 installed)
```
python3 paml2html.py
```

...or you can also import it and use in a different file with `import paml2html` by calling the `paml2html.convert_from_file()` function and providing a filepath


## Arguments
`paml2html.py [-h] [--indent INDENT] source_file destination_file`

- `-h, --help` - show help
- `--indent <number>` - the optional amount of spaces used to indent the HTML file, indentation is off by default
- `source_file` - source text file containing PaML content
- `destination_file` - file for the resulting HTML content
