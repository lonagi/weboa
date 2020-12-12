from PIL import Image
from weboa.utils import Processing
from weboa.utils import Printer

import os

class Library:
    def __init__(self):
        self.name = ""

    def load_script(self):
        return self.js

    def load_script(self):
        return self.js

    def load_link(self):
        return self.css

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return other+self.__str__()

    def __radd__(self, other):
        return other+self.__str__()


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
            self.File_Create(f)

    def js(self):
        files = ("/js/script.js","/js/script.min.js")
        for f in files:
            self.File_Create(f)

    def img(self):
        img = Image.new('RGB', (128, 128))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/favicon.png')
        img = Image.new('RGB', (1024, 500))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/sn_share.png')

    def readme(self):
        self.copy('res/misc/README.md', "/README.md")

    def gitignore(self):
        self.copy('res/misc/gitignore',"/.gitignore")

    def ico_langs(self):
        for l in self.langs:
            self.copy('res/ico_langs/'+l+'.svg',"/img/"+l+".svg")

    def script(self, jscript):
        with open(self.path+self.BUILDFOLDER+"/php/modules/footer.phtml","r") as f:
            scripts = f.read()
        scripts = scripts.split("\n")
        scripts.insert(-1, "<script src='"+jscript.load()+"'></script>")
        Printer.log("Loading "+jscript)
        with open(self.path+self.BUILDFOLDER+"/php/modules/footer.phtml","w") as f:
            f.write("\n".join(scripts))