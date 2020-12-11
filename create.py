import sys, os

class General:
    BUILDFOLDER = "build"

    def __init__(self):
        self.path = "./"

    def Folder_Create(self,foldername):
        try:
            os.mkdir(os.path.join(self.path,foldername))
            return True
        except FileExistsError:
            print(f"Folder {foldername} exists.")
            return False

    def File_Create(self,filename,text=""):
        # Creating a file at specified location
        with open(os.path.join(self.path, filename), 'w') as f:
            f.write(text)

    def trim(self, text):
        return text.replace("\t","").replace("  ","")

    def del_nl(self,text):
        return text.replace("\n","")

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
