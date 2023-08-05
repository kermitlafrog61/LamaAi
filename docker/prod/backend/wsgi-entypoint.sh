#!/bin/sh

python manage.py makemigrations
python manage.py collectstatic --noinput

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
