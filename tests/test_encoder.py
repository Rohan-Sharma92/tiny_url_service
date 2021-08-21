import pytest
from unittest.mock import Mock
from app.models.encode_request import URLEncodeRequest
from app.encoders.encoder import Encoder 


@pytest.fixture
def encoder_setup():
    cache = Mock()
    strategy = Mock()
    encoder = Encoder(strategy, cache, "http://www.test.com/")
    return encoder


def test_encoding_with_alias(encoder_setup):
    request_details = {"url":"https://www.stackoverflow.com", "alias":"stack"}
    request = URLEncodeRequest(request_details)
    encoder_setup.cache.exists.return_value = False
    response = encoder_setup.encode(request)
    assert response == '{"longURL": "https://www.stackoverflow.com", "shortURL": "http://www.test.com/stack/", "alias": "stack"}'

    
def test_encoding_with_alias_already_exists(encoder_setup):
    request_details = {"url":"https://www.stackoverflow.com", "alias":"stack"}
    request = URLEncodeRequest(request_details)
    encoder_setup.cache.exists.return_value = True
    response = encoder_setup.encode(request)
    assert response == "Not Available"

    
def test_encoding_without_alias(encoder_setup):
    request_details = {"url":"https://www.stackoverflow.com"}
    request = URLEncodeRequest(request_details)
    encoder_setup.cache.exists.return_value = False
    encoder_setup.strategy.generateEncodedString.return_value = "random"
    response = encoder_setup.encode(request)
    assert response == '{"longURL": "https://www.stackoverflow.com", "shortURL": "http://www.test.com/random/", "alias": null}'


def test_encoding_without_alias_already_exists(encoder_setup):
    request_details = {"url":"https://www.stackoverflow.com"}
    request = URLEncodeRequest(request_details)
    encoder_setup.cache.exists.side_effect = [True, False]
    encoder_setup.strategy.generateEncodedString.side_effect = ["random1", "random2"]
    response = encoder_setup.encode(request)
    assert response == '{"longURL": "https://www.stackoverflow.com", "shortURL": "http://www.test.com/random2/", "alias": null}'
