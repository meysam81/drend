#!/bin/sh


gunicorn -b ${ADDRESS} \
         --backlog ${BACKLOG} \
		 -w ${WORKERS} \
         --threads ${THREADS} \
         --max-requests ${MAX_REQUESTS} \
         -t ${TIMEOUT} \
         --keep-alive ${KEEP_ALIVE} \
         --limit-request-line ${LIMIT_REQUEST_LINE} \
         ${RELOAD} \
         ${NO_SENDFILE} \
         ${DAEMON} \
         --log-level ${LOG_LEVEL} \
         -n ${NAME} \
         drend.drend.wsgi
