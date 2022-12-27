FROM python:3.9-slim

RUN pip install --no-cache-dir -U pip setuptools wheel
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY src /src
WORKDIR /src

ENTRYPOINT /src/entrypoint.sh
