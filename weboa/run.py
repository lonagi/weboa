#!/usr/bin/env python
from weboa import *
from weboa import __VERSION__
import sys

def runcli():
    print("Welcome to Weboa!")
    commands = {
        "version": ("--version", "-v"),
        "init": ("--init","-i"),
        "langs": ("--langs", "-l"),
        "start": ("--start", "-s")
    }

    args = sys.argv
    for i in range(len(args)):
        if args[i] in commands["version"]:
            print(f"Weboa version is {__VERSION__}")
        elif args[i] in commands["start"]:
            _path = os.getcwd()
            try:
                with open(".weboa", "r") as f:
                    try:
                        dweboa = json.loads(f.read())
                    except json.decoder.JSONDecodeError:
                        Printer.warning("json .weboa file is empty!")
                        dweboa = {"version": __VERSION__}
            except FileNotFoundError:
                Printer.log("Add .weboa file")
                dweboa = {"version":__VERSION__}

            with open(".weboa", "w") as f:
                dweboa["path"] = _path
                dweboa = json.dumps(dweboa)
                f.write(dweboa)

        elif args[i] in commands["init"]:
            php=PHP(path="./")
            php.BUILDFOLDER = ""
            php.FS()
            php.index()
            php.language()
            php.project()
            php.libs()
            php.ico()
            php.css()
            php.robots()
            php.js()
            php.img()
            php.readme()
            php.gitignore()
            php.ico_langs()
            print(f"Langs {args[i+1]}")

if(__name__=="__main__"):
    runcli()