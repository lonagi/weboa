import requests

class Downloader:

    @staticmethod
    def get(url):
        r = requests.get(url)
        return r.text

    @staticmethod
    def download(_to,_from):
        text = Downloader.get(_from)
        with open(_to,"w") as f:
            f.write(text)