#!/bin/bash

mkdir -p /var/run/gunicorn
chmod 777 /var/run/gunicorn/

. env/bin/activate
cd automation \
  && nohup gunicorn --access-logfile - --workers 3 --bind unix:/var/run/gunicorn/nacm.sock nacm.wsgi:application > app.log &
