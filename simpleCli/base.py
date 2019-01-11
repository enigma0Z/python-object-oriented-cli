#!/usr/bin/env python3
"""
simpleCli.base
"""

from argparse import ArgumentParser
from collections import deque
from .exceptions import NotImplementedException

class BaseCommand:
    """
    Base class for CLI classes.  Realistically, this really doesn't do anything other than
    establish basic metadata for the class and provide structure for subclasses to follow

    :param str name: The name of the command
    :param str cmd: The command text of the command.  If absent, it defaults to name.lower()

    .. testsetup:: *

        from collections import deque
        from simpleCli.base import BaseCommand
        from simpleCli.exceptions import *
        baseCommand = BaseCommand(
            name="Test",
            description="Description")

    .. testcode::
        :hide:

        # Check that name / cmd are set correctly
        assert baseCommand.name == "Test"
        assert baseCommand.cmd == "test"
        assert baseCommand.description == "Description"
        assert baseCommand.stack == deque(["test"])

    """

    def __init__(self, *args, **kwargs):
        #pylint: disable=unused-argument

        self.name = kwargs['name']
        self.stack = deque([])

        if "stack" in kwargs:
            self.stack.append(kwargs['stack'])

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

        self.initParser()

    def initParser(self):
        """
        Initalize the argument parser.  Subclasses should define any arguments for the command
        in this method. If you subclass this class, define your parser args here so that if the
        stack gets changed, everything is updated correctly.
        """
        self._parser = ArgumentParser(
            prog=" ".join(self.stack),
            description=self.description)

    def stackAppendleft(self, value):
        """
        Updates self.stack by prepending value to the list and re-initalizing the parser
        If you create a subclass that contains other commands (like the Interpreter class)

        :param str value: The item to prepend (deque.appendleft()) to the stack
        """
        self.stack.appendleft(value)
        self.initParser()

    def parse(self, *args):
        """
        Parse arguments through self._parser

        :param args: Sequential arguments to pass through the parser
        """
        return self._parser.parse_args(args)

    def do(self, *args):
        #pylint: disable=unused-argument,invalid-name
        """
        Execute the command (not implemented in BaseCommand)

        :param args: Sequential arguments passed from the CLI

        .. testcode::
            :hide:

            try:
                baseCommand.do()
            except NotImplementedException:
                pass
        """
        raise NotImplementedException(self)
