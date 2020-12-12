from PIL import Image
from weboa.utils import Processing

import os

class General(Processing):
    def __init__(self, langs=("en","ru"), version="0"):
        super().__init__()
        self.langs = langs
        self.File_Create("./.weboa",version)

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
        self.copy('res/misc/README.md',"/README.md")

    def ico_langs(self):
        for l in self.langs:
            self.copy('res/ico_langs/'+l+'.svg',"/img/"+l+".svg")