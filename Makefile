dependencies:
	pipenv install --dev

lint:
	pipenv run pylint cognito_login
dist: setup.py cognito_login
	pipenv run python setup.py sdist
deploy: dist
	pipenv run twine upload dist/*

clean:
	pipenv --rm
