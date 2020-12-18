import sys, io
from shutil import copy2
from shutil import copytree as copytree2
from weboa import os, json
from weboa import __VERSION__
from .Printer import *

class Processing:
    def __init__(self, path = "../"):
        self.path = path
        self.BUILDFOLDER = "build"
        self.os = sys.platform
        #Printer.info("Platform",sys.platform)
        if(self.os in ["Windows","win32","win64","win"]):
            self.os = "Windows"

    @staticmethod
    def Weboa_Init():
        return {"version": __VERSION__}

    @staticmethod
    def Weboa_Open():
        try:
            with open(".weboa", "r") as f:
                wf = json.loads(f.read())
            return wf
        except FileNotFoundError:
            Printer.error("Weboa project doesn't exist")
            return False
    @staticmethod
    def Weboa_Save(fweboa):
        with open(".weboa", "w") as f:
            fweboa = json.dumps(fweboa)
            f.write(fweboa)

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