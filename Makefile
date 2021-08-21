.PHONY: start install test

start:
	@bash bin/run.sh

install:
	python -m pip install -r requirements.txt

test:
	@pytest tests