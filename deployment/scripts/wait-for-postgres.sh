#!/bin/bash
set -e

until PGPASSWORD=$DB_PASSWORD psql -h $HOST -d $DB_NAME -U $DB_USER -c '\q'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - ready to connection"
exec "$@"