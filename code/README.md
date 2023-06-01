# Code

## Synopsis

Inside this directory, you can find the code that complements the demonstration of the [OWASP API Security Top 10 2023RC](https://owasp.org/www-project-api-security/announcements/2023/02/api-top10-2023rc.html). The code generates a docker container that runs an API called `VunlAPI` with several vulnerabilities. Each vulnerability is thoroughly explained in the [docs folder](../docs/README.md#owasp-api-security).

## Build and run the Docker Image

```bash
docker compose up --build
```

## Run the Docker Image

```bash
docker compose up
```

The API runs on port `8000` by default. You can change this behaviour by editing the [`docker-compose.yml`](./docker-compose.yml) file.

Once it's running, explore the **Swagger UI** at [http://localhost:8000/docs](http://localhost:8000/docs).

## Endpoints

The following endpoints are available:

| Endpoint | Description |
| --- | --- |
| `GET /` | The root endpoint. |
| `GET /docs` | [The Swagger UI.](http://localhost:8000/docs) |
| `GET /redoc` | [The ReDoc UI.](http://localhost:8000/redocs) |
| `GET /api/v1/shops` | The `shops` endpoint is part of the [API1:2023 Broken Object Level Authorization](../docs/API-Security/0xa1-broken-object-level-authorization.md) demonstration |
| `GET /api/v1/shops/{shop_name}` | The `shops/{shop_name}` endpoint demonstrates [API1:2023 Broken Object Level Authorization](../docs/API-Security/0xa1-broken-object-level-authorization.md) |
| `PUT /api/v1/account` | The `account` endpoint demonstrates [API2:2023 Broken Authentication](../docs/API-Security/0xa2-broken-authentication.md) |
| `PUT /api/v1/videos/{video_id}` | The `videos/{video_id}` endpoint demonstrates [API3:2023 Broken Object Property Level Authorization](../docs/API-Security/0xa3-broken-object-property-level-authorization.md) |
| `GET /api/v1/invites/{{invite_id}}` | The `invites/{{invite_id}}` endpoint is part of the [API5:2023 Broken Function Level Authorization](../docs/API-Security/0xa5-broken-function-level-authorization.md) demonstration |
| `POST /api/v1/invites` | The `invites` endpoint demonstrates [API5:2023 Broken Function Level Authorization](../docs/API-Security/0xa5-broken-function-level-authorization.md) |
| `POST /api/v1/profile/picture` | The `profile/picture` endpoint demonstrates [API6:2023 Server Side Request Forgery](../docs/API-Security/0xa6-server-side-request-forgery.md) |
| `GET /api/v1/dm/user_updates.json` | The `dm/user_updates.json` endpoint demonstrates [API7:2023 Security Misconfiguration](../docs/API-Security/0xa7-security-misconfiguration.md) |
