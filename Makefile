dependencies:
	pipenv install --dev

lint:
	pipenv run pylint cognito_login
build:
	python setup.py sdist
deploy:
	twine upload dist/*

clean:
	pipenv --rm
