# page_content.py

class PageContent:
    
    def __init__(self):
        self._sentences = []
        self._words = []

    @property
    def sentences(self):
       
        return self._sentences

    @property
    def words(self):
      
        return self._words

    @sentences.setter
    def sentences(self, value):
       
        self._sentences = value

    @words.setter
    def words(self, value):
      
        self._words = value
