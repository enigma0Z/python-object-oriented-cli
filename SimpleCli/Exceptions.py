#!/usr/bin/env python3

class CliException(Exception):
    pass

class NotImplementedException(CliException):
    def __init__(self, *args, **kwargs):
        self.instance=args[0]

    def __str__(self):
        return "{}: Not implemented".format(self.args[0].cmd)
