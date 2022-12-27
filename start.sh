#!/bin/bash -e

mkdir -p src/data

if [[ $1 = "c" ]]; then
    rm -f src/data/db.sqlite3
    rm -f src/**/migrations/0*.py
fi
python src/manage.py makemigrations
python src/manage.py migrate
if [[ $1 = "c" ]]; then
    python src/manage.py createsuperuser
fi
python src/manage.py runserver

# python manage.py check --deploy
