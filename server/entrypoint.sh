#!/bin/sh

# remember to get this working you must make it executable before running docker 
# use chmod +x  server/src/entrypoint.sh from root

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0