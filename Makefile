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

test:
	pytest test --cov=cognito_login --cov-report term
test-html:
	pytest test --cov=cognito_login --cov-report html:coverage/html
test-only:
	pytest test
