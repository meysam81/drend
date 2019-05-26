
build-dev:
	docker-compose -f docker/drend-dev.yml build

run-dev:
	docker-compose -f docker/drend-dev.yml \
					-f docker/gateway.yml \
					-f analytic.yml \
					up

stop-dev:
	docker-compose -f docker/drend-dev.yml \
					-f docker/gateway.yml \
					-f analytic.yml \
					down

base:
	docker build -t drend-ms-base docker/base

test:

collect-static:
	docker exec -it drend-ms-drend python manage.py collectstatic

create-super-user:
	docker exec -it drend-ms-drend python manage.py createsuperuser

make-migrations:
	docker exec drend-ms-drend python manage.py makemigrations

migrate: make-migrations
	docker exec drend-ms-drend python manage.py migrate

