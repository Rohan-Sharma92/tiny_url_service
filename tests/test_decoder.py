import pytest
import urllib
from unittest.mock import Mock
from app.models.decode_request import URLDecodeRequest
from app.decoders.decoder import Decoder 
from app.cache.url_mapping import URLMapping


@pytest.fixture
def decoder_setup():
    cache = Mock()
    decoder = Decoder(cache)
    return decoder


def test_decoding_with_valid_url(decoder_setup):
    request = URLDecodeRequest("http://www.test.com/stack/")
    mapping = URLMapping("https://www.stackoverflow.com", "http://www.test.com/stack/", alias="stack")
    decoder_setup.cache.getMapping.return_value = mapping
    response = decoder_setup.decode(request)
    assert response == '{"url": "https://www.stackoverflow.com"}'

    
def test_decoding_with_invalid_url(decoder_setup):
    request = URLDecodeRequest("http://www.test.com/stack/")
    decoder_setup.cache.getMapping.return_value = None
    response = decoder_setup.decode(request)
    assert response == "Not Found"


def test_decoding_with_encoded_url(decoder_setup):
    encodedUrl = urllib.parse.quote("http://www.test.com/stack/")
    mapping = URLMapping("https://www.stackoverflow.com", "http://www.test.com/stack/", alias="stack")
    decoder_setup.cache.getMapping.return_value = mapping
    request = URLDecodeRequest(encodedUrl)
    response = decoder_setup.decode(request)
    assert response == '{"url": "https://www.stackoverflow.com"}'
