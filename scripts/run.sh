#!/usr/bin/env bash
cd "`dirname $0`/.."
git pull

export FLASK_APP=/home/pi/dev/kettlr.py
flask run --host=0.0.0.0
