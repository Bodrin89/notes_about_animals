docker-compose:
	#docker-compose -f ./docker/local/docker-compose.yaml --env-file .env up --build -d
	docker-compose --project-name reactive_phone -f ./docker/local/docker-compose.yaml --env-file .env up
	--build -d

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
