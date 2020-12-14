FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11
WORKDIR /app
COPY . /app
RUN RUN apk add --no-cache gcc=9.3.0-r0 libc-dev=0.7.2-r0 g++=9.3.0-r0 libffi-dev=3.2.1-r6 libxml2=2.9.10-r4 unixodbc-dev=2.3.7-r2 libpq=12.5-r0 postgresql-dev=12.5-r0; \
    pip install -r requirements.txt; \
    pip install --upgrade meinheld

