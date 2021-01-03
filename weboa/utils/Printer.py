from .Console_Color import *

class Printer:

    @staticmethod
    def _dolog(text):
        try:
            with open("log.txt","r") as f:
                log_txt = f.read()
        except:
            pass
        with open("log.txt","w") as f:
            f.write(log_txt+"\n"+text)

    @staticmethod
    def stext(text):
        color = Console_Color("text").color
        print(color, text)

    @staticmethod
    def warning(text):
        color = Console_Color("warning").color
        print(color, "[Warning]", text)
        Printer.stext("")

    @staticmethod
    def error(text):
        color = Console_Color("error").color
        print(color, "[Error]", text)
        Printer.stext("")

    @staticmethod
    def log(text):
        #color = Console_Color("log").color
        Printer._dolog("[Log] "+str(text))

    @staticmethod
    def info(text):
        #color = Console_Color("info").color
        Printer._dolog("[Info] "+str(text))