#!/usr/bin/env python3
"""
Example using inheritance
"""

import sys
import re

#pylint: disable=wrong-import-position
sys.path.append("../")
from oocli import interpreter, base, entrypoint

class Re(base.Command):
    """
    Given a regex, matches it (re.match()) against the input text
    """

    def __init__(self):
        super().__init__(
            name="re",
            description="Match regexes")

    def initParser(self):
        super().initParser()
        self._parser.add_argument("regex", help="The regex")
        self._parser.add_argument("string", help="The thing to compare against")

    def do(self, *args):
        opts = self.parse(*args)
        return re.match(opts.regex, opts.string)

class Cmp(base.Command):
    """
    Given a string, compares it against the input text
    """

    def __init__(self):
        super().__init__(
            name="cmp",
            description="Match string literal")

    def initParser(self):
        super().initParser()
        self._parser.add_argument("compare", help="The string to compare")
        self._parser.add_argument("string", help="The thing to compare against")

    def do(self, *args):
        opts = self.parse(*args)
        return opts.compare == opts.string

class Entrypoint(entrypoint.Command):
    """
    Entrypoint for Re
    """

    def __init__(self):
        super().__init__(
            description="OO CLI Example",
            command=interpreter.Command(
                description="Run comparisons (re or cmp)",
                commands=[
                    Re(),
                    Cmp()
                ]
            )
        )

Entrypoint().do()
