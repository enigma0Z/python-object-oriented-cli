#!/usr/bin/env python3

import sys
import argparse
from .. import *

class EchoCommand(BaseCommand):
    """
    Simple echo command (for demonstration purposes)
    """

    def __init__(self, *args):
        super().__init__(
            name="Echo", 
            description="Print the input to the terminal")
        
    def init_parser(self):
        super().init_parser()
        self._parser.add_argument("args", nargs='*', help="Things to be echoed")
    
    def do(self, *args):
        opts = self.parse(*args)
        print(*opts.args)

