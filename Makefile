# Simple scripts for building and running the project

freeze:
	pip freeze > requirements.txt

install:
	pip install --requirement requirements.txt

test:
	pytest --pretty

venv-init: 
	python -m venv .venv

venv-windows:
	./.venv/Scripts/activate.ps1

