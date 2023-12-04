docker-compose:
	docker-compose --project-name reactive_phone -f ./docker/local/docker-compose.yaml --env-file .env up
	--build -d

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

celery-worker:
	celery -A config worker -l info
celery-beat:
	celery -A config beat -l info
start-test:
	pytest