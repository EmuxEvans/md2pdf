# coding=utf8

"""Usage:
  md2pdf <filepath> [-s <stylesheet>] [-o <output>]
  md2pdf [-h|-v]

Options:
  -h --help         show help
  -v --version      show version"""

import sys
from docopt import docopt

from md2pdf import __version__
from md2pdf.generator import generator


def main():
    args = docopt(__doc__, version=__version__)

    filepath = args['<filepath>']
    stylesheet = args['<stylesheet>']
    output = args['<output>']

    if not filepath:
        sys.exit(__doc__)

    try:
        results = generator.generate(
            filepath, stylesheet=stylesheet, output=output)
    except Exception, e:
        sys.exit(e)

    message = 'output to %s (%.2fs)\n' % results
    sys.stdout.write(message)
    sys.stdout.flush()
    sys.exit(0)


if __name__ == '__main__':
    main()
