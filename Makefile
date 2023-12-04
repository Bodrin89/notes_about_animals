docker-compose:
	docker-compose --project-name reactive_phone -f ./docker/local/docker-compose.yaml --env-file .env up --build -d

install-tools:
	pip install poetry && poetry config virtualenvs.create false && poetry install --no-root --no-interaction

start-project:
	python3 manage.py runserver 8000


migrate:
	python3 manage.py makemigrations && python3 manage.py migrate

run-celery:
	celery -A config worker --detach && celery -A config beat --detach

run-test:
	pytest