#!/usr/bin/env python3
#pylint# disable=E1101,E1120,C0103,C0111
#pylint: disable=C0103,E1101,W0107
"""
Annotations example
-------------------

Code::

    import re
    import sys

    #pylint: disable=wrong-import-position
    sys.path.append("../")
    from oocli import base, interpreter, entrypoint, echo

    @interpreter.Command(description="My Command")
    class mainCmd(interpreter.Command):
        "Main Command for the program"
        pass

    @mainCmd.add
    @interpreter.Command(name="regex", description="Regex comparisons")
    class regexCmd(interpreter.Command):
        "Regex subcommand"
        pass

    @mainCmd.add
    @interpreter.Command(name="generic", description="Generic comparisons")
    class genericCmd(interpreter.Command):
        "Generic (comparions) subcommand"
        pass

    @mainCmd.add
    @echo.Command()
    class echoCmd(echo.Command):
        "Echo command"
        pass

    @mainCmd.regex.add
    @base.Command(name="match", description="Regex re.match() comparison")
    class reCmd(base.Command):
        "Regex comparison command"
        def initParser(self):
            super().initParser()
            self._parser.add_argument("regex")
            self._parser.add_argument("string")

        def do(self, *args):
            opts = self.parse(*args)
            return re.match(opts.regex, opts.string)

    @mainCmd.generic.add
    @base.Command(name="equals", description="Equals comparison")
    class equalsCmd(base.Command):
        "Equals comparison command"
        def initParser(self):
            super().initParser()
            self._parser.add_argument("left")
            self._parser.add_argument("right")

        def do(self, *args):
            opts = self.parse(*args)
            return opts.left == opts.right

    if __name__ == "__main__":
        entrypoint.Command("Annotation example", mainCmd).do()

"""
