#!/bin/bash
set -x

echo "CLEARING UP PORT 7878..."
kill -9 $(lsof -t -i :7878)

echo "STARTING THE GUNICORN WSGI WEBSERVER...."
/usr/bin/gunicorn -w 4 --bind unix:/opt/gunicorn.sock wsgi:app


