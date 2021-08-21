import pytest
from app.cache.url_cache import URLCache
from app.cache.url_mapping import URLMapping


@pytest.fixture
def cache():
    return URLCache()


@pytest.fixture
def encoded_mapping():
    mapping = URLMapping("https://www.stackoverflow.com", "https://www.stack.com/")
    return mapping


def test_cache_find_when_empty(cache):
    assert cache.exists(url="abc") is False


def test_cache_add_entry(cache, encoded_mapping):
    cache.addMapping(encoded_mapping)
    assert cache.getMapping(encoded_mapping.shortURL) == encoded_mapping
