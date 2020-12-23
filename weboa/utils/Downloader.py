import requests
import json

class Downloader:

    @staticmethod
    def get(url):
        r = requests.get(url)
        return r.text

    @staticmethod
    def download(_to,_from,_what,_back):
        result = json.loads(Downloader.get("https://raw.githubusercontent.com/New-Vektor-Group/pkg-repo/main/"+_back+"/libs.json"))

        if(_what not in result.keys()):
            return False

        pkg = result[_what]
        text = Downloader.get(_from+pkg["package"]+".php")

        if(pkg["isfile"]):
            with open(_to + pkg["package"] + "." + _back, "w") as f:
                f.write(text)
        if(len(pkg["dep"]) > 0):
            for d in pkg["dep"].values():
                with open(_to + d + "." + _back, "w") as f:
                    textd = Downloader.get(_from + d + ".php")
                    f.write(textd)