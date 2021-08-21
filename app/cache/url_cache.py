from threading import Lock
from app.cache.url_mapping import URLMapping


class URLCache(object):
    '''
    A URL cache for storing URLMapping against shortURL generated. The cache is intended to be accessed asynchronously by multiple workers,
    therefore, locking is implemented for thread safety
    '''
    cache = None
    lock = None

    def __init__(self):
        self.cache = {}
        self.lock = Lock()
        
    def exists(self, url=None) -> bool:
        if url in self.cache:
            return True
        return False
    
    def addMapping(self, mapping:URLMapping)-> bool:
        isSuccessful=True
        self.lock.acquire()
        if self.exists(mapping.shortURL):
            isSuccessful=False
        else:
            self.cache[mapping.shortURL] = mapping
        self.lock.release()
        return isSuccessful
    
    def getMapping(self, shortUrl) -> URLMapping:
        self.lock.acquire()
        if shortUrl in self.cache:
            res = self.cache[shortUrl]
        else:
            res = None
        self.lock.release()
        return res;
