#!/bin/bash

gunicorn -w 1 -k gevent --bind 0.0.0.0:8000 coolmarks.wsgi:application
