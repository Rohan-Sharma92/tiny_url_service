import urllib.parse, string, logging
from app.cache.url_cache import URLCache
from app.models.decode_request import URLDecodeRequest
from app.models.decode_response import DecodeResponse

logger = logging.getLogger(__name__)


class Decoder(object):
    '''
    Decoder implementation to fetch URL using encoded/plain URI provided in request
    '''
    cache = None

    def __init__(self, cache:URLCache):
        self.cache = cache
        
    def decode(self, urlRequest:URLDecodeRequest) -> string:
        decodedStr = urllib.parse.unquote(urlRequest.url)
        logger.info("Decoded short URL: %s", decodedStr)
        mappedResult = self.cache.getMapping(decodedStr)
        if mappedResult is None:
            return "Not Found"
        response = DecodeResponse(mappedResult.longURL).toJson()
        return response
