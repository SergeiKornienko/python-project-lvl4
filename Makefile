lint:
	poetry run flake8
test:
	poetry run ./manage.py test task_manager
runserver:
	poetry run python manage.py runserverm
install:
	poetry install
build:
	poetry build
test-coverage-report-xml:
	@poetry run coverage xml
test-coverage-report: test
	@poetry run coverage report -m $(ARGS)
	@poetry run coverage erase
requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt --extras psycopg2
check: lint test requirements.txt