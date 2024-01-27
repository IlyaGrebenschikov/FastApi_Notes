# Async CRUD Application
Simple CRUD application with FastAPI, PostgreSQL, SQLAlchemy and Alembic

Setup:

`docker compose -f docker_compose.yaml up`

Env-file:

`You need to rename .env_example to .env and set your values.`

`POSTGRES_HOST=host`

`POSTGRES_PORT=port`

`POSTGRES_USER=username`

`POSTGRES_PASSWORD=password`

`POSTGRES_DB=dbname`

`DB_URL='postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'`
