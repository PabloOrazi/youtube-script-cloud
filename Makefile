install-python:
	sudo apt install python3

create-env:
	python3 -m venv .venv

setup-env: install-python create-env

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

update-linux:
	sudo apt update && sudo apt upgrade

format:
	black *.py
	
lint:
	pylint --disable=R,C app.py functions.py main.py
	
test:
	python -m pytest -vv --cov=functions --cov=app --cov=yt_transcript_cli --cov-report=html:test_coverage_report tests/

build:
	docker build -t my-flask-app .

run-daemon:
	docker run -d -p 5000:5000 my-flask-app

run:
	docker run -p 5000:5000 my-flask-app

run-flask:
	python3 app.py

all: install lint test