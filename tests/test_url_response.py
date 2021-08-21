import pytest
from app.models.response import CustomResponse


def test_response_mime_type():
    res = CustomResponse().createResponse("test")
    assert res.mimetype == 'application/json'
