
build-dev:
	docker-compose -f docker/drend-dev.yml build

run-dev:
	docker-compose -f docker/drend-dev.yml up

stop-dev:
	docker-compose -f docker/drend-dev.yml down

build-base:
	docker build -t drend-ms-base docker/base

test:
