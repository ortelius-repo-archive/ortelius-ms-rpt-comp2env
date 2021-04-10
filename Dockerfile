FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11
ARG CYCLONE_OUTPUT=comp2env_bom.json
ARG TRIVY_OUTPUT=comp2env_trivy_scan.json
COPY requirements.txt .
WORKDIR /app
COPY main.py /app
RUN apk add --no-cache curl=7.67.0-r3 busybox=1.31.1-r10 musl-utils=1.1.24-r3 ssl_client=1.31.1-r10 gcc=9.3.0-r0 libc-dev=0.7.2-r0 g++=9.3.0-r0 libffi-dev=3.2.1-r6 libxml2=2.9.10-r4 unixodbc-dev=2.3.7-r2 libpq=12.6-r0 postgresql-dev=12.6-r0; \
    # Installing libraries present in requirements.txt
    pip install -r requirements.txt; \
    pip install --upgrade meinheld; \
    # Building bill-of-materials(bom) using cyclonedx
    pip freeze > requirements.txt; \
    pip install cyclonedx-bom==0.4.3; \
    cyclonedx-py -j -o ${CYCLONE_OUTPUT}; \
    # Uninstall pip to remove CVEs
    python -m pip uninstall -y pip setuptools; \
    # Scan for vulnerabilities using trivy
    curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin; \
    trivy fs -f json -o ${TRIVY_OUTPUT} --no-progress /; \
    rm -r /usr/local/bin/trivy;

