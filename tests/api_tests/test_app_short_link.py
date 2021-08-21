import pytest,json
from app.application import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def encode_setup(client):
    res=client.post("/encode", json={
        'url': 'https://www.stackoverflow.com'
    })
    return res

def test_start(client):
    assert client.get("/").status_code == 200
    
def test_blueprint(client):
    blueprints=client.application.blueprints
    assert "short_link" in blueprints
    assert "errors" in blueprints

def test_decode_without_payload(client):
    res=client.get("/decode")
    assert res.status_code == 400
    res_str=json.dumps(res.get_json())
    assert res_str == '{"url": null, "data": "Bad Request"}'

def test_decode_with_invalid_payload(client):
    res=client.get("/decode?shortURL=test")
    assert res.status_code == 400
    res_str=json.dumps(res.get_json())
    assert res_str == '{"url": "test", "data": "Invalid URL"}'

def test_decode_with_valid_payload(encode_setup,client):
    encodeResponse=json.dumps(encode_setup.get_json())
    encoding_response_dict = json.loads(encodeResponse)
    shortUrl=encoding_response_dict['shortURL']
    decodeRes=client.get(f"/decode?shortURL={shortUrl}")
    assert decodeRes.status_code == 200
    decodeResStr=json.dumps(decodeRes.get_json())
    assert decodeResStr =='{"url": "https://www.stackoverflow.com"}'
    
def test_encode_without_payload(client):
    res=client.post("/encode")
    assert res.status_code == 400
    res_str=json.dumps(res.get_json())
    assert res_str == '{"url": null, "data": "Bad Request"}'

def test_encode_with_invalid_payload(client):
    res=client.post("/encode",json={'url':'test'})
    assert res.status_code == 400
    res_str=json.dumps(res.get_json())
    assert res_str == '{"url": "test", "data": "Invalid URL"}'

def test_encode_with_valid_payload(client):
    res=client.post("/encode", json={
        'url': 'https://www.stackoverflow.com'
    })
    assert res.status_code == 200
    res_str=json.dumps(res.get_json())
    encoding_response_dict = json.loads(res_str)
    shortUrl=encoding_response_dict['shortURL']
    assert encoding_response_dict['longURL']=='https://www.stackoverflow.com'
    assert shortUrl.startswith("http://short.est/")

def test_encode_with_valid_payload_and_alias(client):
    res=client.post("/encode", json={
        'url': 'https://www.stackoverflow.com',
        'alias':'stack'
    })
    assert res.status_code == 200
    res_str=json.dumps(res.get_json())
    encoding_response_dict = json.loads(res_str)
    assert encoding_response_dict['longURL']=='https://www.stackoverflow.com'
    assert encoding_response_dict['shortURL']=="http://short.est/stack/"
    assert encoding_response_dict['alias']=='stack'

def test_api_with_exception(client):
    res=client.post("/test")
    assert res.status_code==500