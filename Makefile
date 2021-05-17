lint:
	poetry run flake8 task_manager
test:
	poetry run coverage run --source 'task_manager' manage.py test task_manager --noinput
runserver:
	poetry run python manage.py runserver
install:
	poetry install
build: check
	poetry build
test-coverage-report-xml: test
	poetry run coverage xml
requirements.txt: poetry.lock
	poetry export --format requirements.txt --output requirements.txt --extras psycopg2
check: lint test requirements.txt
makemigrations:
	poetry run python manage.py makemigrations
migrate:
	poetry run python manage.py migrate
