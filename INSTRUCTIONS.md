

# Short Link

ShortLink is a URL shortening service where you enter a URL such as https://codesubmit.io/library/react and it returns a short URL such as http://short.est/GeAi9K.

## Overview
ShortLink is a python based URL Shortening service developed using Flask framework. 
The service exposes the following end points:

1. /encode
	
    This is intended to encode a URL to a shortened URL. This end point supports requests with HTTP POST method and 	expects the request to have data in JSON format. 
    The request data consists of two arguments:
	i)  URL: The long URL to be shortened
    
    ii) Alias: Alias to be used if available for encoding. This is an optional argument.
    
    Following is an example request body:
    
    {
     "url":"https://stackoverflow.com/questions/3610272/",
	  "alias":"py_ques"
    }
    
    The response is in the JSON format consisting of longURL, shortURL and alias. Following is a sample response:
    
    {
	      "longURL": "https://stackoverflow.com/questions/3610272/",
		   "shortURL": "http://short.est/py_ques/",
		   "alias": "py_ques"
    }
2. /decode
    
	This is intended to decode a short URL to its original long URL.
	This end point supports requests with HTTP GET method and expects short URL to be provided using a parameter named 'shortURL' in the request.
	The response is in the JSON format consisting of long URL. 
	Following is a sample response:
    
    {
	      "url": "https://stackoverflow.com/questions/3610272/"
    }
### Error Codes and Messages
1. 400: Invalid Request
    This will be returned when a request with invalid parameters is made.
2. 400: Bad Request
    This will be returned when a request is malformed and does not have required data or parameters.
## Installation and Deployment
### Prerequisites
1. Python >=3.7
2. Docker

### Local Installation

1. Install dependencies/requirements using any of the following command in the project directory:

	Using pip
	```
	pip install -r requirements.txt
	```

	Using Makefile:
	```
	make install
	```
2. Start the server by running following script:  

	For unix systems:
	```
	bash bin/run.sh
	```
	
	For Windows:
	```
	python -m wsgi
	```
	
	Using Makefile:
	```
	make start
	```

This will start a [Gunicorn](https://gunicorn.org/) server that wraps the Flask app 
defined in `app/application.py`.
The server shipped with Flask is [intended for development purposes only](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).  

3. To verify if application is started, send the following requests:

	Using curl:
	```bash
	curl localhost:8080/
	```
	Using browser/postman:
	http://localhost:8080/

If application started successfully, the received response will be `Application Started` and status code `200`.

### Running with `docker`

For running this service in a docker container, [Docker](https://www.docker.com/products/docker-desktop) is expected to be already
installed to run this project. 

1. To build a docker image, run:

```bash
docker build . -t short_link:latest
```

2. To launch the docker container, run:

```bash
docker run -p 8081:8080 short_link:latest
```
3. To verify if application is started, send the following requests:

	Using curl:
	```bash
	curl localhost:8081/
	```
	Using browser/postman:
	http://localhost:8081/
	
If application started successfully, the received response will be `Application Started` and status code `200`.

## Testing
API and UnitTests are present under `tests/` directory. For running the tests, run the following command in a python virtual environment

	```
	make install
	make test
	```
