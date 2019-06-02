FROM drend-ms-base as base

WORKDIR /service

COPY setup.py .

RUN pip wheel . -w /wheelhouse



FROM base as dev

WORKDIR /service

COPY . .
COPY --from=base /wheelhouse ./wheelhouse

RUN pip install --no-index -f ./wheelhouse .

ENV ENV development

EXPOSE ${PORT}

CMD sh entrypoint.sh



FROM base as prod

WORKDIR /service

COPY . .
COPY --from=base /wheelhouse ./wheelhouse

RUN pip install --no-index -f ./wheelhouse .

ENV ENV production

EXPOSE ${PORT}

CMD sh entrypoint.sh
