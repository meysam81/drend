.PHONY: startapp

REQUIRED=$(if $(value $(1)),,$(error $(1) not set))

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

logs:
	docker-compose -f docker/drend-dev.yml \
					-f docker/gateway.yml \
					-f docker/api.yml \
					-f docker/analytic.yml \
					logs --follow

base:
	docker build -t drend-ms-base docker/base

test:

collect-static:
	docker exec -it drend-ms-drend python manage.py collectstatic

create-super-user:
	docker exec -it drend-ms-drend python manage.py createsuperuser

shell:
	docker exec -it drend-ms-drend python manage.py shell

make-migrations:
	docker exec drend-ms-drend python manage.py makemigrations

migrate:
	docker exec drend-ms-drend python manage.py migrate

not-up:
	docker ps -a | grep -v Up | grep drend-ms

ps:
	docker ps | grep drend-ms

purge-containers:
	docker ps -a | grep drend-ms | awk 'NR>1 {print $1}' | xargs docker stop | xargs docker rm

startapp:
	$(call REQUIRED,APP)
	cd drend && \
	ENV=management \
	python3 manage.py startapp ${APP}
