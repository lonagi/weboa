from PIL import Image
from weboa.utils import *

import os

class General(Processing):
    def __init__(self, langs=("en","ru")):
        super().__init__()
        self.langs = langs

    def robots(self):
        self.copy('res/misc/robots.txt',"/robots.txt")

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
        self.copy('res/misc/README.md',"/README.md")

    def ico_langs(self):
        for l in self.langs:
            self.copy('res/ico_langs/'+l+'.svg',"/img/"+l+".svg")

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
        self.copy('res/phpfs/language.php',"/php/controller/language.php")
        for l in self.langs:
            self.copy('res/phpfs/l.php', f"/php/configs/{l}.php")

    def controller(self):
        files = ("controller.php","index.php","router.php")
        for f in files:
            self.copy('res/phpfs/controller.php',"/php/controller/controller.php")

        # .htaccess
        self.copy('res/phpfs/.htaccess',"/.htaccess")

    def project(self):
        self.copy('res/phpfs/db.php',"/php/db.php")                     # DATABASE
        self.copy('res/phpfs/test.php',"/php/api/test.php")             # API
        self.copy('res/phpfs/consts.php',"/php/configs/consts.php")     # Consts

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