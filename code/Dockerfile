FROM docker.io/bitnami/python:3.11

LABEL org.opencontainers.image.authors="F." \
    org.opencontainers.image.vendor="hyp3rd" \
    org.opencontainers.image.description="OWASP-API-Security " \
    org.opencontainers.image.source="https://github.com/hyp3rd/OWASP-API-Security/" \
    org.opencontainers.image.title="OWASP-API-Security"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
