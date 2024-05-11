dependencies:
	pip freeze > requirements.txt

environment:
	python3 -m venv surveyenv

venv:
	cd surveyenv/bin && source ./activate

install:
	pip install -r requirements.txt 