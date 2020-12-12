from weboa.utils import *
from weboa.project import *

import os

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
        self.copy('res/phpfs/_index.php',"/index.php")

    def language(self):
        # Language system
        self.copy('res/phpfs/language',"/php/controller/language.php")
        for l in self.langs:
            self.copy('res/phpfs/l', f"/php/configs/{l}.php")

    def controller(self):
        files = ("controller.php","index.php","router.php")
        for f in files:
            self.copy('res/phpfs/'+f,"/php/controller/"+f)

        # .htaccess
        self.copy('res/phpfs/.htaccess',"/.htaccess")

    def project(self):
        self.copy('res/phpfs/db',"/php/db.php")                     # DATABASE
        self.copy('res/phpfs/test',"/php/api/test.php")             # API
        self.copy('res/phpfs/consts',"/php/configs/consts.php")     # CONSTS
        self.copy('res/phpfs/header', "/php/modules/header.phtml")  # META

    def libs(self):
        self.copy('res/phpfs/autoload.php', "/php/lib/autoload.php")
        _path = os.path.join(self.path,'res/phplib/')
        Printer.info("Libs versions:")
        for f in os.listdir(_path):
            if(os.path.isdir(_path+f)):
                self.copytree('res/phplib/'+f,"/php/lib/"+f)
            else:
                self.copy('res/phplib/' + f, "/php/lib/" + f)

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
site.libs()
site.readme()
site.ico_langs()