from flask import Blueprint, request
import json, logging, validators
from app.settings import config
from app.models.encode_request import URLEncodeRequest
from app.models.decode_request import URLDecodeRequest
from app.models.response import CustomResponse

'''
    URL shortener service exposing two end points : /encode and /decode
    
    The /encode API encodes a long URL to a short URL using EncodingStrategy specified or using alias if possible. 
    The result is a JSON object with URLMapping details
     
    The /encode API retrieves a long URL mapped to short URL specified. 
    The result is a JSON object with URLMapping details
'''

short_link = Blueprint("short_link", __name__)
logger = logging.getLogger(__name__)
shortUrlKey = 'shortURL'


@short_link.route("/encode", methods=['POST'])
def encode():
    res = CustomResponse()
    payload = request.get_json()
    if payload is None:
        return badRequest(res)
    encoding_request = createEncodingRequest(payload)
    logger.info("Received encoding request: %s", encoding_request)
    if not validators.url(encoding_request.url):
        return invalidRequest(res, encoding_request.url)
    response = config.encoder.encode(encoding_request)
    logger.info("Sending response: %s", response)
    return res.createResponse(response)


@short_link.route("/decode", methods=['GET'])
def decode():
    res = CustomResponse()
    if shortUrlKey not in request.args:
        return badRequest(res)
    decoding_request = createDecodingRequest()
    logger.info("Received encoding request: %s", decoding_request)
    if not validators.url(decoding_request.url):
        return invalidRequest(res, decoding_request.url)
    response = config.decoder.decode(decoding_request)
    logger.info("Sending response: %s", response)
    return res.createResponse(response)


def createEncodingRequest(payload):
    encoding_request_str = json.dumps(payload)
    encoding_request_dict = json.loads(encoding_request_str)
    encoding_request = URLEncodeRequest(encoding_request_dict)
    return encoding_request


def createDecodingRequest():
    payload = request.args[shortUrlKey]
    decoding_request = URLDecodeRequest(payload)
    return decoding_request


def createPayload(url, message):
    payload = {"url":url, "data":message}
    return payload


def invalidRequest(res, url):
    payload = createPayload(url, "Invalid URL")
    data = json.dumps(payload)
    response = res.createResponse(data, status=400)
    logger.info("Sending response: %s", response)
    return response


def badRequest(res, url=None):
    payload = createPayload(url, "Bad Request")
    data = json.dumps(payload)
    response = res.createResponse(data, status=400)
    logger.info("Sending response: %s", response)
    return response
