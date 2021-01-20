# SpeechWebApp

## Git workflow

- feature branch : feature/feature_name
- bug fix : fix/bug_name
- test : test/test_name

## Docker

Build and start the web application together with the backend by typing from the root of the project:

```sh
docker-compose -f ./docker/docker-compose.yml -f/.docker/test.yml up
```

launch tests in docker 

```sh
docker-compose -f ./docker/docker-compose.yml -f/.docker/test.yml run backend pytest
```

## Local dev

### Backend

Ensure that you have Postgres installed and running and issue the following commands to create a role and database:

```
$ psql postgres
postgres=# CREATE USER postgres WITH PASSWORD 'postgres';
postgres=# CREATE DATABASE test_db;
```

Installing the dependencies and running the server:

```sh
cd api/
python -m venv venv
pip install -r requirements.txt
source venv/bin/activate
PYTHONPATH=./src POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_DB=test_db POSTGRES_HOST=localhost POSTGRES_PORT=5432  python -m src.app
```

### Frontend

Installing the dependencies and running the webpack dev server:

```sh
cd web-app/
npm install
npm run start
```
