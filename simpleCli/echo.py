#!/usr/bin/env python3
"""
simpleCli.echo
"""

from .base import BaseCommand

class EchoCommand(BaseCommand):
    """
    Simple echo command (for demonstration purposes)
    """

    def __init__(self, *args):
        super().__init__(
            name="Echo",
            description="Print the input to the terminal")

    def initParser(self):
        super().initParser()
        self._parser.add_argument("args", nargs='*', help="Things to be echoed")

    def do(self, *args):
        opts = self.parse(*args)
        print(*opts.args)
