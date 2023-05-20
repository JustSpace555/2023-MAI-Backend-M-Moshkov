up:
	docker-compose up -d

migrate:
	docker-compose run --rm django sh -c "python3 DjangoProject/manage.py makemigrations"
	docker-compose run --rm django sh -c "python3 DjangoProject/manage.py migrate"

test:
	docker-compose up -d && ./test.sh