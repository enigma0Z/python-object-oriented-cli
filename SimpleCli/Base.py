#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import deque
from .Exceptions import *

class BaseCommand:
    """
    Base class for CLI classes.  Realistically, this really doesn't do anything other than
    establish basic metadata for the class and provide structure for subclasses to follow
    """
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']

        if "stack" in kwargs:
            self.stack = deque(kwargs['stack'])
        else:
            self.stack = deque([])
           
        if "cmd" not in kwargs:
            self.cmd = kwargs['name'].lower()
        else: 
            self.cmd = kwargs['cmd']

        if self.cmd != None:
            self.stack.append(self.cmd)

        if "description" in kwargs:
            self.description = kwargs['description']
        else:
            self.description = None

        self.init_parser()

    def init_parser(self):
        """
        Initalize the argument parser.  Subclasses should define any arguments for the command
        in this method.
        """
        self._parser = ArgumentParser(
            prog=" ".join(self.stack),
            description=self.description)

    def stack_appendleft(self, value):
        """
        Updates self.stack by prepending value to the list and re-initalizing the parser
        If you create a subclass that contains other commands (like the Interpreter class)
        """
        self.stack.appendleft(value)
        self.init_parser()

    def parse(self, *args):
        """
        Parse arguments
        :param: *args - Arguments to parse
        """
        return self._parser.parse_args(args)

    def do(self, *args):
        """
        Execute the command (stub)
        :param: *args - Sequential arguments
        :param: **kwargs - Keyword arguments
        """
        raise NotImplementedException(self)
