import json


class DecodeResponse(object):
    '''
    A decode response
    '''
    url = None
    
    def __init__(self, url):
        self.url = url
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def __repr__(self):
        return f"DecodeResponse[longURL[{self.url}]]"
