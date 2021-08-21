from flask import Flask
from app.resources.short_link import short_link
from app.resources.errors import errors

'''
    Entry point for registering blueprints in flask application
'''

app = Flask(__name__)
app.register_blueprint(short_link)
app.register_blueprint(errors)


@app.route('/', methods=['GET'])
def start():
    return "Application Running"
