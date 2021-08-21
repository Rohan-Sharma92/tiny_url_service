import pytest
from app.models.encode_request import URLEncodeRequest
from app.models.decode_request import URLDecodeRequest


def test_encode_repr():
    request_details = {"url":"https://www.stackoverflow.com", "alias":"stack"}
    request = URLEncodeRequest(request_details)
    assert request.__repr__() == "EncodingRequest[URL[https://www.stackoverflow.com]:Alias[stack]]"


def test_decode_repr():
    request = URLDecodeRequest("https://www.stackoverflow.com")
    assert request.__repr__() == "DecodingRequest[URL[https://www.stackoverflow.com]]"
