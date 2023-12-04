#!/bin/bash -x
python manage.py runserver 0.0.0.0:8081 || exit 1
python manage.py migrate --noinput || exit 1
celery -A config worker -l info || exit 1
celery -A config beat -l info || exit 1
exec "$@"
