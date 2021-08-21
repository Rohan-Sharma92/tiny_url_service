import json


class URLMapping(object):
    '''
    A URLMapping for storing longURL,encoded shortURL and alias details
    '''
    longURL = None
    shortURL = None
    alias = None
    
    def __init__(self, longURL, shortURL, alias=None):
        self.longURL = longURL
        self.shortURL = shortURL
        self.alias = alias
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def __repr__(self):
        return f"DecodingRequest[LongURL[{self.longURL}]:ShortURL[{self.shortURL}]:Alias[{self.alias}]]"
