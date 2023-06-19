FROM diliplakshya/python3.10.12-alpine3.18-poetry as requirements-stage

WORKDIR /tmp

COPY pyproject.toml /tmp
COPY poetry.lock* /tmp

RUN poetry export -f requirements.txt --only core --only dev --only aut-test --output requirements.txt --without-hashes

FROM diliplakshya/python3.10.12-alpine3.18-poetry

WORKDIR /app

# Copy requirements from host, to docker container in /app 
# COPY ./requirements.txt .
# Install the dependencies
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Copy everything from ./worker directory to /app in the container
COPY worker /app/worker

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
