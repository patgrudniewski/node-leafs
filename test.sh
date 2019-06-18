#! /usr/bin/env sh

WD=$(dirname $(realpath --no-symlinks $0))

docker run --rm \
    -v $WD:/srv \
    -e PYTHONDONTWRITEBYTECODE=1 \
    python:3.6-alpine \
    /srv/test.py
