#!/usr/bin/env python3
"""
Quick & simple example of the built in command classes:

    $ ./simple.py --help
    <help text>

    $ ./simple.py --list # Prints the output from the interpreter --list option
    echo: Print the input to the terminal
    outer: Interpret subcommands
    - echo: Print the input to the terminal
    - inner: Interpret subcommands
      - echo: Print the input to the terminal

    $ ./simple.py echo "test"
    test
"""

from oocli import interpreter, echo, entrypoint

entrypoint.Command(
    "oocli example",
    interpreter.Command(
        name=None,
        commands=[
            echo.Command(),
            interpreter.Command(
                name="Outer",
                commands=[
                    echo.Command(),
                    interpreter.Command(
                        name="Inner",
                        commands=[
                            echo.Command()
                        ]
                    )
                ]
            )
        ]
    )
).do()
