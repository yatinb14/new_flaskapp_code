#!/bin/bash
AMSHOME_DIR=/home/AMSnewly/AMS
cd $AMSHOME_DIR
source ./env
printf "The aAMS application URL IP is $APP_URL\n"
cd $AMSHOME_DIR
cd login
nohup flask run --host $IPADD --port $LOGIN_PORT &
echo "Login component of AMS application has been started"
cd ../admin
nohup flask run --host $IPADD --port $ADMIN_PORT &
echo "Admin component of AMS application has been started"
cd ../home
nohup flask run --host $IPADD --port $HOME_PORT &
echo "Home component of AMS application has been started"
cd ../vendor
nohup flask run --host $IPADD --port $VENDOR_PORT &
echo "vendor component of AMS application has been started"
cd ../invoice
nohup flask run --host $IPADD --port $INVOICE_PORT &
echo "Invoice component of AMS application has been started"
cd ../purchase
nohup flask run --host $IPADD --port $PURCHASE_PORT &
echo "Purchase component of AMS application has been started"
cd ../trainer
nohup flask run --host $IPADD --port $TRAINER_PORT &
echo "trainer component of AMS application has been started"
cd ../report
nohup flask run --host $IPADD --port $REPORT_PORT &
echo "report component of AMS application has been started"
cd ../bill
nohup flask run --host $IPADD --port $BILL_PORT &
echo "bill component of AMS application has been started"
echo "All components started for AMS application"
