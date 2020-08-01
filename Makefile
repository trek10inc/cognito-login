dependencies:
	pipenv install --dev

lint:
	pipenv run pylint cognito_login
build: setup.py cognito_login
	pipenv run python setup.py sdist
deploy: build
	pipenv run twine upload dist/*

clean:
	pipenv --rm
