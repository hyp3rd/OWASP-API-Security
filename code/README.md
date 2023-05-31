# Code

## Synopsis

This directory contains the complementary code to showcase the [OWASP API Security Top 10 2023RC](https://owasp.org/www-project-api-security/announcements/2023/02/api-top10-2023rc.html).

Each vunerability is documentented and described in the [docs folder](../docs/README.md#owasp-api-security).

The code spins up a docker container with a vulnerable API.

## Build the Docker Image

```bash
chmod +x build.bash
./build.bash
```

## Run the Docker Image

```bash
docker compose up
```

Explore the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs).
