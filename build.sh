#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python core/manage.py collectstatic --noinput

python core/manage.py makemigrations

python core/manage.py migrate
