#!/usr/bin/python
from .frontend.cli import commands
import sys

if __name__ == '__main__':
    commands.process_command(sys.argv)
