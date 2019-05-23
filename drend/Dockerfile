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

RUN chmod u+x ./entrypoint.sh

EXPOSE 6000

CMD './entrypoint.sh'



FROM base as prod

WORKDIR /service

COPY . .
COPY --from=base /wheelhouse ./wheelhouse

RUN pip install --no-index -f ./wheelhouse .

ENV ENV production

RUN chmod u+x ./entrypoint.sh

EXPOSE 6000

CMD './entrypoint.sh'
