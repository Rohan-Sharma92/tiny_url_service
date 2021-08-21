class URLDecodeRequest(object):
    '''
    Decoding Request details includes short URL
    '''
    url = None
    
    # The class "constructor" - It's actually an initializer 
    def __init__(self, url):
        self.url = url
    
    def __repr__(self):
        return f"DecodingRequest[URL[{self.url}]]"
