#!/usr/bin/env python3
"""
simpleCli.interpreter
"""

import sys
import argparse
from .base import BaseCommand
from .exceptions import CliException

class InterpreterCommand(BaseCommand):
    """
    Interprets commands given (by, for example, sys.argv[]) into running subcommands in classes
    """

    def __init__(self, name, *args, **kwargs):
        if name is None:
            name = sys.argv[0].split("/")[-1]

        super().__init__(
            name=name,
            description="Run subcommands...")

        self.commands = {}
        for item in args:
            if isinstance(item, BaseCommand):
                item.stackAppendleft(self.cmd) # Insert the interpreter into the command's stack
                self.commands.update({item.cmd: item})

    def initParser(self):
        super().initParser()
        self._parser.add_argument(
            "-l", "--list",
            action="store_const",
            default=False,
            const=True,
            help="List commands that can be run")
        self._parser.add_argument(
            "cmd",
            nargs='?',
            help="The command to run")
        self._parser.add_argument(
            "args",
            nargs=argparse.REMAINDER,
            help="Arguments to <command>")

    def call(self, cmd, *args):
        """
        Call member command <cmd> with *args
        """
        try:
            assert cmd != None
            self.commands[cmd].do(*args)
        except AssertionError:
            raise CliException("You must specify a command to run")
        except KeyError:
            raise CliException("{}: Command not found".format(cmd))

    def printList(self, prefix=""):
        """
        Print the list of commands that the interpreter has
        """
        for cmd, obj in self.commands.items():
            if isinstance(obj, self.__class__):
                print(prefix + obj.cmd + ": " + obj.description)
                if prefix == "":
                    newprefix = "- "
                else:
                    newprefix = "  " + prefix

                obj.printList(prefix=newprefix)

            else:
                print("{}{}: {}".format(prefix, cmd, obj.description))

    def do(self, *args):
        opts = self.parse(*args)
        if opts.list:
            self.printList()

        else:
            try:
                self.call(opts.cmd, *opts.args)
            except CliException as exception:
                print(exception)
                self._parser.print_help()
                sys.exit(1)
