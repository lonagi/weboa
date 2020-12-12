from PIL import Image
from shutil import copy2
from weboa.utils import *

import sys, os, io

class Proccessing:
    BUILDFOLDER = "build"

    def __init__(self):
        self.path = "../"
        self.os = sys.platform
        #Printer.info("Platform",sys.platform)
        if(self.os in ["Windows","win32","win64","win"]):
            self.os = "Windows"

    def Folder_Create(self, foldername):
        try:
            os.mkdir(os.path.join(self.path, foldername))
            return True
        except FileExistsError:
            Printer.warning(f"Folder {foldername} exists.")
            return False

    def File_Create(self, filename, text=""):
        # Creating a file at specified location
        with io.open(os.path.join(self.path, filename), 'w', encoding="utf-8") as f:
            f.write(text)

    def Trime(self, text):
        return text.replace("\t", "").replace("  ", "")

    def Delete_Lines(self, text):
        return text.replace("\n", "")

class General(Proccessing):
    def __init__(self, langs=("en","ru")):
        super().__init__()
        self.langs = langs

    def robots(self):
        copy2(self.path + 'res/misc/robots.txt', os.path.join(self.path, self.BUILDFOLDER) + "/robots.txt")

    def ico(self):
        img = Image.new('RGB', (64, 64))
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
        img.save(os.path.join(self.path, self.BUILDFOLDER)+'/favicon.ico', sizes=icon_sizes)

    def css(self):
        files = ("/css/styles.css", "/css/styles.min.css")
        for f in files:
            self.File_Create(self.BUILDFOLDER + f)

    def js(self):
        files = ("/js/script.js","/js/script.min.js")
        for f in files:
            self.File_Create(self.BUILDFOLDER + f)

    def img(self):
        img = Image.new('RGB', (128, 128))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/favicon.png')
        img = Image.new('RGB', (1024, 500))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/sn_share.png')

    def readme(self):
        copy2(self.path + 'res/misc/README.md', os.path.join(self.path, self.BUILDFOLDER) + "/README.md")

    def ico_langs(self):
        for l in self.langs:
            copy2(self.path + 'res/ico_langs/'+l+'.svg', os.path.join(self.path, self.BUILDFOLDER) + "/img/"+l+".svg")

class PHP(General):
    def __init__(self, langs=("en","ru")):
        super().__init__(langs=langs)
        Printer.log("Start PHP Project")
        Printer.info(f"Your system is {self.os}")

    def FS(self):
        # Creating folders for php project
        folders = ("","/css","/js","/img","/php","/php/api","/php/configs","/php/controller","/php/lib","/php/modules")
        for f in folders:
            self.Folder_Create(self.BUILDFOLDER + f)

    def index(self):
        copy2(self.path + 'res/phpfs/_index.php', os.path.join(self.path, self.BUILDFOLDER) + "/index.php")

    def language(self):
        # Language system
        copy2(self.path + 'res/phpfs/language.php',
              os.path.join(self.path, self.BUILDFOLDER) + "/php/controller/language.php")

        # Dicts
        _text = """
                            <?php
                            $__translations = [
                                "d0"=>"",
                            ];?>
                        """
        for l in self.langs:
            self.File_Create(self.BUILDFOLDER + f"/php/configs/{l}.php", self.Trime(_text))

    def controller(self):
        files = ("controller.php","index.php","router.php")
        for f in files:
            copy2(self.path + 'res/phpfs/controller.php',
                  os.path.join(self.path, self.BUILDFOLDER) + "/php/controller/controller.php")

        # .htaccess
        copy2(self.path + 'res/phpfs/.htaccess', os.path.join(self.path, self.BUILDFOLDER) + "/.htaccess")

    def project(self):
        # DATABASE
        copy2(self.path + 'res/phpfs/db.php',os.path.join(self.path, self.BUILDFOLDER) + "/php/db.php")

        # API
        copy2(self.path + 'res/phpfs/test.php', os.path.join(self.path, self.BUILDFOLDER) + "/php/api/test.php")

        # Consts
        copy2(self.path + 'res/phpfs/consts.php', os.path.join(self.path, self.BUILDFOLDER) + "/php/configs/consts.php")

    def libs(self):
        files = ("nvg-data.php", "nvg-oau.php", "nvg-pag.php", "nvg-pag-nav.php", "rb.php")
        for f in files:
            copy2(self.path + 'res/phpfs/controller.php',
                  os.path.join(self.path, self.BUILDFOLDER) + "/php/controller/controller.php")




site = PHP(langs=("en","ru","ro"))
site.FS()
site.index()
site.robots()
site.ico()
site.css()
site.js()
site.img()
site.language()
site.controller()
site.project()
site.readme()
site.ico_langs()