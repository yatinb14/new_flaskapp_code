#!/bin/bash
export APP_URL=52.188.146.151
export LOGIN_PORT=5000
export ADMIN_PORT=5001
export HOME_PORT=5002
export VENDOR_PORT=5003
export INVOICE_PORT=5004
export PURCHASE_PORT=5005
export TRAINER_PORT=5006

cd trainer
export FLASK_APP=flaskblog.py
nohup flask run --host 0.0.0.0 --port 5006 &
