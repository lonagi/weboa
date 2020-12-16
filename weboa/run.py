#!/usr/bin/env python
from weboa import *
from weboa import __VERSION__
import sys

def runcli():
    print("Welcome to Weboa!")
    commands = {
        "version": ("--version", "-v"),
        "init": ("--init","-i"),
        "langs": ("--langs", "-l")
    }

    args = sys.argv
    for i in range(len(args)):
        if args[i] in commands["version"]:
            print(f"Weboa version is {__VERSION__}")
        elif args[i] in commands["init"]:
            php=PHP()
            php.FS()
            php.index()
            php.language()
            php.ico()
            php.css()
            print(f"Langs {args[i+1]}")

if(__name__=="__main__"):
    runcli()