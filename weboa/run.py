#!/usr/bin/env python
from weboa import *
from weboa import __VERSION__
import sys

def runcli():
    print("Welcome to Weboa!")
    commands = {
        "version": ("--version", "-v"),
        "init": ("--init","-i"),
    }

    for arg in sys.argv:
        if arg in commands["version"]:
            print(f"Weboa version is {__VERSION__}")
        elif arg in commands["init"]:
            php=PHP()
            php.FS()
            php.index()
            php.language()
            php.ico()
            php.css()

if(__name__=="__main__"):
    runcli()