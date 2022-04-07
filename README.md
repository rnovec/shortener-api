# Shortener API

An API REST to shorten URLs

## Features

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper with SQLite3 implementation
- [Pytest](https://docs.pytest.org/en/7.1.x/) - The **pytest** framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

## Requirements

- Python 3.8+
- Docker
- Docker Compose

### Run locally

```bash
docker-compose up
```

#### OpenSwagger docs

- [http://localhost:8000/docs](http://localhost:8000/docs)

#### Run tests

```
docker-compose run --rm api pytest
```

## Live Example

### Swagger docs

[https://shortener-challenge.herokuapp.com/docs](https://shortener-challenge.herokuapp.com/docs)

## Shortener Approach

| Field      | Type     | Description                                                                      |
| ---------- | -------- | -------------------------------------------------------------------------------- |
| id         | Integer  | Unique integer identifier.                                                       |
| url        | String   | URL/URI with maximum length of 2083 chars to respect the Microsoft browser spec. |
| code       | String   | 4-digit code of random letters.                                                  |
| created_at | Datetime | Timestamp to track row creation.                                                 |
