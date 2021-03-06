#!/bin/bash
cd /thinknyx/ams/
source ./newenv
export FLASK_DEBUG=1
export FLASK_ENV=development
cd new_code
export FLASK_APP=login.py
nohup flask run --host 0.0.0.0 --port 5000 &
echo "Login started"
cd ../new_code
export FLASK_APP=admin.py
nohup flask run --host 0.0.0.0 --port 5001 &
echo "Admin started"
cd ../new_code
export FLASK_APP=home.py
nohup flask run --host 0.0.0.0 --port 5002 &
echo "Home started"
cd ../new_code
export FLASK_APP=vendor.py
nohup flask run --host 0.0.0.0 --port 5003 &
echo "vendor started"
cd ../new_code
export FLASK_APP=invoice.py
nohup flask run --host 0.0.0.0 --port 5004 &
echo "Invoice started"
cd ../new_code
export FLASK_APP=purchase.py
nohup flask run --host 0.0.0.0 --port 5005 &
echo "Purchase started"
cd ../new_code
export FLASK_APP=trainer.py
nohup flask run --host 0.0.0.0 --port 5006 &
echo "trainer started"
cd ../new_code
export FLASK_APP=report.py
nohup flask run --host 0.0.0.0 --port 5007 &
echo "report started"
cd ../new_code
export FLASK_APP=bill.py
nohup flask run --host 0.0.0.0 --port 5008 &
echo "bill started"
echo "All components started for the application"
