import sys, io, lesscpy, sass
from shutil import copy2
from shutil import copytree as copytree2
from weboa import os, json
from weboa.utils import Meta, FileSystem

from .Printer import *
from six import StringIO


class Processing(Meta,FileSystem):
    def __init__(self, path = "../"):
        self.path = path
        self.BUILDFOLDER = "build"
        self.os = sys.platform
        if(self.os in ["Windows","win32","win64","win"]):
            self.os = "Windows"

    @staticmethod
    def pre_css(_weboa, i, precss="less"):
        with open(i, "r") as f:
            prep = f.read()
            if precss=="less":
                css = lesscpy.compile(StringIO(prep), minify=True)
            elif precss in ("sass","scss"):
                css = sass.compile(string=prep, output_style="compressed")

        with open(i[:-4] + "css", "w") as f:
            f.write(css)

        _weboa[precss][i] = os.stat(i).st_mtime
        Processing.Weboa_Save(_weboa)


    @staticmethod
    def Save_Path(_path):
        try:
            with open(".weboa", "r") as f:
                try:
                    dweboa = json.loads(f.read())
                except json.decoder.JSONDecodeError:
                    Printer.warning("json .weboa file is empty!")
                    dweboa = Processing.Weboa_Init()
        except FileNotFoundError:
            Printer.log("Add .weboa file")
            dweboa = Processing.Weboa_Init()

        dweboa["path"] = _path
        Processing.Weboa_Save(dweboa)
        Printer.log("Save the project path")

    def Folder_Create(self, foldername):
        try:
            os.mkdir(self.path+self.BUILDFOLDER+foldername)
            return True
        except FileExistsError:
            Printer.warning(f"Folder {foldername} exists.")
            return False

    def File_Create(self, filename, text=""):
        # Creating a file at specified location
        with io.open(os.path.join(self.path, self.BUILDFOLDER)+filename, 'w', encoding="utf-8") as f:
            f.write(text)

    def copy(self, src, dst):
        copy2(self.path + src, os.path.join(self.path, self.BUILDFOLDER) + dst)

    def copytree(self, src, dst):
        try:
            copytree2(self.path + src, os.path.join(self.path, self.BUILDFOLDER) + dst)
        except FileExistsError:
            pass

    def Trime(self, text):
        return text.replace("\t", "").replace("  ", "")

    def Delete_Lines(self, text):
        return text.replace("\n", "")