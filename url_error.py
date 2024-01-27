# url_error.py

class UrlError(Exception):
   
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"Invalid URL: {self.url}"
