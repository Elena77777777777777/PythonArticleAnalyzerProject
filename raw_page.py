# raw_page.py
import requests
from url_error import UrlError

class RawPage:
    \
    def __init__(self, url):
        self.url = url
        self._data = None
        self._headline = None

    @property
    def data(self):
        
        if not self._data:
            self._download_page()
        return self._data

    @property
    def headline(self):
        
        if not self._headline:
            self._download_page()
        return self._headline

    def _download_page(self):
        
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self._data = response.text
            self._headline = response.headers['Wikipedia-Page-Title']
        except requests.RequestException as e:
            raise UrlError(self.url)
