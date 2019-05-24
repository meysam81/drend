FROM python:3.8.0a4-alpine3.9

RUN apk update
RUN apk add libffi-dev openssl-dev
RUN pip install -U pip

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod u+x /usr/local/bin/entrypoint.sh
