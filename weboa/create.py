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
        img.save(os.path.join(self.path, self.BUILDFOLDER)+'/favicon.ico', sizes=icon_sizes)

    def css(self):
        self.File_Create(self.BUILDFOLDER + "/css/styles.css")
        self.File_Create(self.BUILDFOLDER + "/css/styles.min.css")

    def js(self):
        self.File_Create(self.BUILDFOLDER + "/js/script.js")
        self.File_Create(self.BUILDFOLDER + "/js/script.min.js")

    def img(self):
        img = Image.new('RGB', (128, 128))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/favicon.png')
        img = Image.new('RGB', (1024, 500))
        img.save(os.path.join(self.path, self.BUILDFOLDER) + '/img/sn_share.png')

    def readme(self):
        _text = """
        Change ToDo:
        1. >>> php/configs/(en|*).php
        2. >>> php/db.php
        3. >>> /favicon.ico/
        4. >>> /img/favicon.png
        5. >>> /img/sn_share.png
        
        """
        self.File_Create(self.BUILDFOLDER + "/README.md",_text)

    def ico_langs(self):
        for l in self.langs:
            copy2(self.path + 'res/'+l+'.svg', os.path.join(self.path, self.BUILDFOLDER) + "/img/"+l+".svg")

class PHP(General):
    def __init__(self, langs=("en","ru")):
        super().__init__(langs=langs)
        Printer.log("Start PHP Project")
        Printer.info(f"Your system is {self.os}")

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
        _text = """
                <?php
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

        # Consts
        _text = """
                    <?php
                    $DOMAIN = '';
                    $_DOMAIN = "https://".$DOMAIN;
                    $SITE_TITLE = '';
                    $DESCRIPTION = $__translations['d0'];
                    $KEYWORDS = 'NVG, ';
                    $MAIN_COLOR = "#";
                    $CACHE = "7";
                    $SN_BANNER = "img/sn_share.png?".$CACHE;
                    ?>
               """
        self.File_Create(self.BUILDFOLDER + "/php/configs/consts.php", self.Trime(_text))

        # Consts
        _text = """
                    <?php
                    $DOMAIN = '';
                    $_DOMAIN = "https://".$DOMAIN;
                    $SITE_TITLE = '';
                    $DESCRIPTION = $__translations['d0'];
                    $KEYWORDS = 'NVG, ';
                    $MAIN_COLOR = "#";
                    $CACHE = "7";
                    $SN_BANNER = "img/sn_share.png?".$CACHE;
                    ?>
               """
        self.File_Create(self.BUILDFOLDER + "/php/configs/consts.php", self.Trime(_text))

        # Dicts
        _text = """
                    <?php
                    $__translations = [
                        "d0"=>"",
                    ];?>
                """
        for l in self.langs:
            self.File_Create(self.BUILDFOLDER + f"/php/configs/{l}.php", self.Trime(_text))



site = PHP(langs=("en","ru","ro"))
site.FS()
site.index()
site.robots()
site.ico()
site.css()
site.js()
site.img()
site.project()
site.readme()
site.ico_langs()