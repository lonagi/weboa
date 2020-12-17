from weboa.project import *
from weboa import json
from weboa import __VERSION__

class PHP(General):
    def __init__(self, langs=("en","ru"), path = "../"):
        super().__init__(langs=langs,path=path)
        Printer.log("Start PHP Project")
        Printer.info(f"Your system is {self.os}")
        Printer.info(f"Weboa version is {__VERSION__}")

    def FS(self):
        # Creating folders for php project
        folders = ("","/css","/js","/img","/php","/php/api","/php/configs","/php/controller","/php/lib","/php/modules")
        for f in folders:
            self.Folder_Create(f)
        self.File_Create("/.weboa", json.dumps(Processing.Weboa_Create()))

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
        self.copy('res/phpfs/footer', "/php/modules/footer.phtml")  # SCRIPTS

    def libs(self):
        self.copy('res/phpfs/autoload.php', "/php/lib/autoload.php")
        _path = os.path.join(self.path,'res/phplib/')

        with open(_path+'libs.json') as json_file:
            data = json.load(json_file)
            data = json.dumps(data,indent=2)

        Printer.info("Libs versions:\n"+data)
        for f in os.listdir(_path):
            if(os.path.isdir(_path+f)):
                self.copytree('res/phplib/'+f,"/php/lib/"+f)
            else:
                self.copy('res/phplib/' + f, "/php/lib/" + f)