from PIL import Image
import sys, os

#pip install pillow

class Proccessing:
    BUILDFOLDER = "build"

    def __init__(self):
        self.path = "./"

    def Folder_Create(self, foldername):
        try:
            os.mkdir(os.path.join(self.path, foldername))
            return True
        except FileExistsError:
            print(f"Folder {foldername} exists.")
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
        self.File_Create(self.BUILDFOLDER + "/robots.txt", self.Delete_Lines(_text))

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

class PHP(General):
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
            
                    //LIBS
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

php = PHP()
php.FS()
php.index()
php.robots()
php.ico()
php.css()
php.js()
php.img()