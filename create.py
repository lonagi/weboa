from PIL import Image
from shutil import copy2
import sys, os


class Proccessing:
    BUILDFOLDER = "build"

    def __init__(self):
        self.path = "./"
        self.os = sys.platform
        #print("Platform",sys.platform)
        if(self.os in ["Windows","win32","win64","win"]):
            self.os = "Windows"

    def Folder_Create(self, foldername):
        try:
            os.mkdir(os.path.join(self.path, foldername))
            return True
        except FileExistsError:
            print(f"[Warning] Folder {foldername} exists.")
            return False

    def File_Create(self, filename, text=""):
        # Creating a file at specified location
        with open(os.path.join(self.path, filename), 'w') as f:
            f.write(text)

    def Trime(self, text):
        return text.replace("\t", "").replace("  ", "")

    def Delete_Lines(self, text):
        return text.replace("\n", "")

class General(Proccessing):
    def __init__(self):
        super().__init__()

    def robots(self):
        _text = """
            User-agent: *
            Disallow: /php/
            Disallow: /test.html
            Host: https://
            Clean-param: lang /
            
            #NVG
            #NVGroup
            #New Vektor Group   
        """
        self.File_Create(self.BUILDFOLDER + "/robots.txt", self.Trime(_text))

    def ico(self):
        img = Image.new('RGB', (64, 64))
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
        img.save(self.BUILDFOLDER+'/favicon.ico', sizes=icon_sizes)

    def css(self):
        self.File_Create(self.BUILDFOLDER + "/css/styles.css")
        self.File_Create(self.BUILDFOLDER + "/css/styles.min.css")

    def js(self):
        self.File_Create(self.BUILDFOLDER + "/js/script.js")
        self.File_Create(self.BUILDFOLDER + "/js/script.min.js")

    def img(self):
        img = Image.new('RGB', (128, 128))
        img.save(self.BUILDFOLDER + '/img/favicon.png')
        img = Image.new('RGB', (1024, 500))
        img.save(self.BUILDFOLDER + '/img/sn_share.png')

    def readme(self):
        _text = """
        Change ToDo:
        1. >>> php/configs/dict.php
        2. >>> php/db.php
        3. >>> /favicon.ico/
        4. >>> /img/favicon.png
        5. >>> /img/sn_share.png
        
        """
        self.File_Create(self.BUILDFOLDER + "/README.md",_text)

    def ico_langs(self, langs=("en","ru")):
        for l in langs:
            copy2('res/'+l+'.svg', self.BUILDFOLDER + "/img/"+l+".svg")

class PHP(General):
    def __init__(self):
        super().__init__()
        print("[Log] Start PHP Project")
        print(f"[Log] Your system is {self.os}")

    def FS(self):
        # Creating folders for php project
        self.Folder_Create(self.BUILDFOLDER)
        self.Folder_Create(self.BUILDFOLDER+"/css")
        self.Folder_Create(self.BUILDFOLDER+"/js")
        self.Folder_Create(self.BUILDFOLDER+"/img")
        self.Folder_Create(self.BUILDFOLDER+"/php")
        self.Folder_Create(self.BUILDFOLDER+"/php/api")
        self.Folder_Create(self.BUILDFOLDER+"/php/configs")
        self.Folder_Create(self.BUILDFOLDER+"/php/controller")
        self.Folder_Create(self.BUILDFOLDER+"/php/lib")
        self.Folder_Create(self.BUILDFOLDER+"/php/modules")

    def index(self):
        _text = """ <?php
                    header("X-Frame-Options: SAMEORIGIN");
                    header("X-Content-Type-Options: nosniff");
                    header("X-XSS-Protection: 1; mode=block");
            
                    /*LIBS*/
                    require_once("php/lib/autoload.php");
                    require_once("php/db.php");
                    require_once("php/controller/controller.php");
                    ?>
                    <!DOCTYPE HTML>
                    <html lang='<?=$lang;?>'>
                    <head>
                        <?php include("php/modules/header.phtml");?>
                    </head>
                    <body>
                    <?php
                        include_once "php/controller/index.php";
                    ?>
                    </body>
                    </html>        
        """
        self.File_Create(self.BUILDFOLDER + "/index.php", self.Trime(_text))

    def project(self):
        # DATABASE
        _text = """
               <?php
               $db = "";
               $l = "root";
               $p = "";
               $setup = R::setup('mysql:host=localhost;dbname='.$db, $l, $p);
               R::addDatabase($db,'mysql:host=localhost;dbname='.$db, $l, $p);
               ?>
               """
        self.File_Create(self.BUILDFOLDER + "/php/db.php", self.Trime(_text))

        # API
        _text = """
               <?php
               header('Access-Control-Allow-Origin: localhost');
               header('Content-Type: application/json; charset=utf-8');
               $output = ["Hello"=>"World"];

               echo json_encode($output,JSON_PRETTY_PRINT);
               ?>
               """
        self.File_Create(self.BUILDFOLDER + "/php/api/test.php", self.Trime(_text))

site = PHP()
site.FS()
site.index()
site.robots()
site.ico()
site.css()
site.js()
site.img()
site.project()
site.readme()
site.ico_langs(langs=("en","ru","ro"))