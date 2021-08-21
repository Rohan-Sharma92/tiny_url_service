class URLEncodeRequest(object):
    '''
    Encoding Request details includes URL and Alias
    '''
    url = None
    alias = None
    
    # The class "constructor" - It's actually an initializer 
    def __init__(self, request_details):
        self.url = request_details['url']
        if 'alias' in request_details:
            self.alias = request_details['alias']
    
    def __repr__(self):
        return f"EncodingRequest[URL[{self.url}]:Alias[{self.alias}]]"
    
