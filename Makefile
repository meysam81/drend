
build-dev:
	docker-compose -f docker/drend-dev.yml build

run-dev:
	docker-compose -f docker/drend-dev.yml \
					-f docker/gateway.yml \
					-f docker/api.yml \
					-f docker/analytic.yml \
					up

stop-dev:
	docker-compose -f docker/drend-dev.yml \
					-f docker/gateway.yml \
					-f docker/api.yml \
					-f docker/analytic.yml \
					down

base:
	docker build -t drend_ms_base docker/base

test:

collect-static:
	docker exec -it drend_ms_drend python manage.py collectstatic

create-super-user:
	docker exec -it drend_ms_drend python manage.py createsuperuser

shell:
	docker exec -it drend_ms_drend python manage.py shell

make-migrations:
	docker exec drend_ms_drend python manage.py makemigrations

migrate:
	docker exec drend_ms_drend python manage.py migrate

not-up:
	docker ps -a | grep -v Up | grep drend_ms

ps:
	docker ps | grep drend_ms

purge-containers:
	docker ps -a | grep drend_ms | awk 'NR>1 {print $1}' | xargs docker stop | xargs docker rm

