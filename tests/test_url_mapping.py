import pytest
from app.cache.url_mapping import URLMapping


def test_repr():
    mapping = URLMapping("LongURL", "ShortURL", alias="alias")
    assert mapping.__repr__() == "DecodingRequest[LongURL[LongURL]:ShortURL[ShortURL]:Alias[alias]]"

    
def test_repr_without_alias():
    mapping = URLMapping("LongURL", "ShortURL")
    assert mapping.__repr__() == "DecodingRequest[LongURL[LongURL]:ShortURL[ShortURL]:Alias[None]]"
