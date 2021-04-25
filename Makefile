lint:
	poetry run flake8
test:
	poetry run ./manage.py test task_manager
runserver:
	poetry run python manage.py runserverm