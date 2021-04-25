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