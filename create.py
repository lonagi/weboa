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

