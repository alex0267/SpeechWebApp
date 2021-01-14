#!/bin/bash
# wait-for-postgres.sh

set -e

cmd="$*"

until psql "host=$POSTGRES_HOST port=5432 dbname=$POSTGRES_DB user=$POSTGRES_USER password=$POSTGRES_PASSWORD"  -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$cmd"