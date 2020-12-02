"""
Python English Parser
  A Python library for parsing English text.

Usage:
  python-english [file]
  python-english [options]

Options:
  -h, --help     Show this help message and exit
  -v, --version  Show the version and exit
"""


from docopt import docopt

from __init__ import __version__
from yacc import parser


def main():
    args = docopt(__doc__, version=f'Python English Parser {__version__}')
    if args['[file]']:
        path = args['[file]']
        # parser.parse()
    else:
        pass


if __name__ == '__main__':
    main()
