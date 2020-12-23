import requests

class Downloader:

    @staticmethod
    def get(url):
        r = requests.get(url)
        return r.text

    @staticmethod
    def download(to,text):
        pass