#!/usr/bin/env bash

pip install -r theboxcoders/requirements.txt
python theboxcoders/manage.py collectstatic --noinput
python theboxcoders/manage.py migrate
