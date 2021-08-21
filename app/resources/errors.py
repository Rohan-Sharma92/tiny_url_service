from flask import Blueprint, Response
'''
    Error handler configuration
'''

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def server_error(error):
    return Response(f"Internal Error {error}", status=500)
