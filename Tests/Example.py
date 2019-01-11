#!/usr/bin/env python3

import sys

sys.path.append(sys.path[0] + "/..")

from Command.Interpreter import *
from Command.Echo import *
from Command.Base import BaseCommand

cli = InterpreterCommand(None,
    EchoCommand(),
    InterpreterCommand("sub1",
        EchoCommand(),
        BaseCommand(name="Blue"),
        BaseCommand(name="Green")
    ),
    InterpreterCommand("sub2",
        EchoCommand(),
        BaseCommand(name="Orange"),
        BaseCommand(name="Brown"),
        InterpreterCommand("sub2-a",
            EchoCommand()
        )
    )
)

cli.do(*sys.argv[1:])
