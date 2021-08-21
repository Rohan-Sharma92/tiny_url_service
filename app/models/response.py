from flask import Response


class CustomResponse(Response):
    '''
    Response object with content-type json
    '''
    default_mimetype = 'application/json'

    def createResponse(self, message, status=200):
        return CustomResponse(message, status)
