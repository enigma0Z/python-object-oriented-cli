#!/usr/bin/env python3

import sys
import argparse
from .. import *

class InterpreterCommand(BaseCommand):
    """
    Interprets commands given (by, for example, sys.argv[]) into running subcommands in classes
    """

    def __init__(self, name, *args, **kwargs):
        if name == None:
            name = sys.argv[0].split("/")[-1]

        super().__init__(
            name=name, 
            description="Run subcommands...")

        self.commands = {}
        for item in args:
            if isinstance(item, BaseCommand):
                item.stack_appendleft(self.cmd) # Insert the interpreter into the command's stack
                self.commands.update({item.cmd: item})
    
    def init_parser(self):
        super().init_parser()
        self._parser.add_argument("-l", "--list", 
            action="store_const",
            default=False,
            const=True,
            help="List commands that can be run")
        self._parser.add_argument("cmd", 
            nargs='?',
            help="The command to run")
        self._parser.add_argument("args", 
            nargs=argparse.REMAINDER, 
            help="Arguments to <command>")

    def call(self, cmd, *args):
        try:
            assert cmd != None
            self.commands[cmd].do(*args)
        except AssertionError:
            raise CliException("You must specify a command to run")
        except KeyError:
            raise CliException("{}: Command not found".format(cmd))
    
    def print_list(self, prefix=""):
        for cmd, obj in self.commands.items():
            if isinstance(obj, self.__class__):
                print(prefix + obj.cmd + ": " + obj.description)
                if prefix == "":
                    newprefix = "- "
                else:
                    newprefix = "  " + prefix

                obj.print_list(prefix=newprefix)
                
            else:
                print("{}{}: {}".format(prefix, cmd, obj.description))

    def do(self, *args):
        opts = self.parse(*args)
        if opts.list:
            self.print_list()

        else:
            try: 
                self.call(opts.cmd, *opts.args)
            except CliException as e:
                print(e)
                self._parser.print_help()
                sys.exit(1)

