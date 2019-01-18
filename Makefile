# Commands

up:
	pipenv shell

start:
	pipenv run python3 ./mysite/manage.py runserver

shell:
	python3 ./mysite/manage.py shell

test:
	python3 ./mysite/manage.py test polls

migrate:
	python3 ./mysite/manage.py migrate

migration:
	python3 ./mysite/manage.py makemigrations

super:
	python3 ./mysite/manage.py createsuperuser


