#!/usr/bin/env python
from weboa import *
from weboa import __VERSION__
import sys

print("Welcome to Weboa!")
commands = {
        "version":("--version","-v")
}

for arg in sys.argv:
    if arg in commands["version"]:
        print(f"Weboa version is {__VERSION__}")