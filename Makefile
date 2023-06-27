

init:
	pip install -r requirements.txt

start:
	python src/manage.py migrate
	python src/manage.py runserver

migrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

superuser:
	python src/manage.py createsuperuser

shell:
	python src/manage.py shell_plus

refresh_db:
	rm -f src/data/db.sqlite3
	python src/manage.py migrate
