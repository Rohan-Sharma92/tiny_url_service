from app.cache.url_cache import URLCache
from app.models.encode_request import URLEncodeRequest
from app.cache.url_mapping import URLMapping
import string, logging

logger = logging.getLogger(__name__)


class Encoder(object):
    '''
    Encoder implementation to encode long URL to short URL using EncodingStrategy or alias if possible
    '''
    cache = None
    prefix = None

    def __init__(self, strategy, cache:URLCache, prefix:string):
        self.strategy = strategy
        self.cache = cache
        self.prefix = prefix

    def encode(self, request:URLEncodeRequest) -> string:
        if request.alias is not None:
            return self._processRequestWithAlias(request)
        return self._processRequestWithoutAlias(request)
    
    def _processRequestWithAlias(self, request:URLEncodeRequest) -> string:
        logger.info("Processing request with alias: %s", request)
        shortURL=self.createShortURL(request.alias)
        if self.cache.exists(shortURL):
            return "Not Available"
        return self._addShortURL(shortURL, request)
        

    def createShortURL(self, encoded_string):
        return self.prefix + encoded_string + "/"

    def _processRequestWithoutAlias(self, request:URLEncodeRequest) -> string:
        logger.info("Processing request: %s", request)
        encoded_string = self.strategy.generateEncodedString()
        while self.cache.exists(self.createShortURL(encoded_string)):
            encoded_string = self.strategy.generateEncodedString()
        return self._addShortURL(self.createShortURL(encoded_string), request)
        
    def _addShortURL(self, shortURL, request:URLEncodeRequest):
        mappedResult = URLMapping(request.url, shortURL, request.alias)
        logger.info("Adding URL mapping: %s", mappedResult)
        isSuccess=self.cache.addMapping(mappedResult)
        if isSuccess:
            response = mappedResult.toJson()
        else:
            response= "Not Available"
        return response
