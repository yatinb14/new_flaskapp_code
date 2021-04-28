import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import jsonify,json
from forms import AccountForm
app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
sess = Session()
sess.init_app(app)


app.config['SECRET_KEY']='584bd72428c13cfb572da08954dd5944de5a4219ad2b79eaadbee5bcefa19b14'
app_on = str(os.getenv("APP_URL"))
home_on = str(os.getenv("HOME_PORT"))
vendor_on = str(os.getenv("VENDOR_PORT"))
invoice_on = str(os.getenv("INVOICE_PORT"))
purchase_on = str(os.getenv("PURCHASE_PORT"))
trainer_on = str(os.getenv("TRAINER_PORT"))
login_on = str(os.getenv("LOGIN_PORT"))
admin_on = str(os.getenv("ADMIN_PORT"))
report_on = str(os.getenv("REPORT_PORT"))
bill_on = str(os.getenv("BILL_PORT"))

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_db = os.getenv("DB_DB")
db_password = os.getenv("DB_PASSWORD")
home_url = str(app_on) + ":" + str(home_on)
vendor_url = str(app_on) + ":" + str(vendor_on)
invoice_url = str(app_on) + ":" + str(invoice_on)
purchase_url = str(app_on) + ":" + str(purchase_on)
trainer_url = str(app_on) + ":" + str(trainer_on)
login_url = str(app_on) + ":" + str(login_on)
admin_url = str(app_on) + ":" + str(admin_on)
report_url = str(app_on) + ":" + str(report_on)
bill_url = str(app_on) + ":" + str(bill_on)
#

var1 = [app_on + ":" + home_on,app_on + ":" + vendor_on,app_on + ":" + invoice_on,app_on + ":" + purchase_on,app_on + ":" + trainer_on,app_on + ":" + login_on,app_on + ":" + admin_on,app_on + ":" + report_on,app_on + ":" + bill_on]
app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = db_db
mysql = MySQL(app) 

@app.route("/")
@app.route("/home")
def home():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced where status = 'open' order by ID DESC LIMIT 5 ")

	if resultValue >= 0:
		userDetails = cur.fetchall()		
	cur1 = mysql.connection.cursor()
	resultValue1 = cur1.execute("SELECT * FROM purchase where status = 'open' order by ID DESC LIMIT 5 ")

	if resultValue1 >= 0:
		purchaseDetails = cur1.fetchall()	
	print(var1)	

	if 'email' not in session:
		return redirect('http://'+login_url)

	return render_template('home/home.html',userDetails=userDetails,purchaseDetails=purchaseDetails,var1=var1)



@app.route("/demo")
def demo():	
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced order by ID DESC LIMIT 5 ")

	if resultValue >= 0:
		userDetails = cur.fetchall()		
	cur1 = mysql.connection.cursor()
	resultValue1 = cur1.execute("SELECT * FROM purchase order by ID DESC LIMIT 5 ")

	if resultValue1 >= 0:
		purchaseDetails = cur1.fetchall()	
	print(var1)	

	if 'email' not in session:
		return redirect('http://'+login_url)

	return render_template('home/demo.html',userDetails=userDetails,purchaseDetails=purchaseDetails,var1=var1)


	




@app.route("/getinvoice/",methods=['GET','POST'])
def getinvoice():
	cur2 = mysql.connection.cursor()
	cur2.execute("select id,name,num,dated,train,subtotal from invoiced")
	row_headers=[x[0] for x in cur2.description] #this will extract row headers
	rv = cur2.fetchall()
	#return(rv)
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	print(json_data)
	return json.dumps(json_data)

	


@app.route("/getpurchase/<vendor>",methods=['GET','POST'])
def getpurchase(vendor):
	#value=request.GET.getlist('add')
	cur2 = mysql.connection.cursor()
	cur2.execute("select id,name,gst,dated,train,subtotal from purchase where name='"+vendor+"'")
	row_headers=[x[0] for x in cur2.description] #this will extract row headers
	rv = cur2.fetchall()
	#return(rv)
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	return json.dumps(json_data)
	




@app.route("/newdash")
def users():
	return render_template('home/dashboard.html',var1=var1)



@app.route("/register")
def register():
	return render_template('home/register.html',var1=var1)	

@app.route("/logout",methods=['GET', 'POST'])  
def logout():  
	session.clear()

	return redirect('http://'+login_url)
	 	
@app.route('/set/')
def set():
	session['key'] = 'value'
	return 'ok'

@app.route('/get/')
def get():
	return session.get('key', 'not set')


		
@app.route("/dashboard")
def dashboard():	
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced ")

	if resultValue >= 0:
		userDetails = cur.fetchall()
		countinvoice = len(userDetails)		
		print(countinvoice)
	cur1 = mysql.connection.cursor()
	resultValue1 = cur1.execute("SELECT * FROM purchase ")

	if resultValue1 >= 0:
		purchaseDetails = cur1.fetchall()	
		countpurchase = len(purchaseDetails)
		print(countpurchase)

	cur2 = mysql.connection.cursor()
	resultValue2 = cur2.execute("SELECT * FROM app ")

	if resultValue2 >= 0:
		vendorDetails = cur2.fetchall()	
		countvendor = len(vendorDetails)
		print(countvendor)

	cur3 = mysql.connection.cursor()
	resultValue3 = cur3.execute("SELECT * FROM trainer ")

	if resultValue3 >= 0:
		trainerDetails = cur3.fetchall()	
		counttrainer = len(trainerDetails)
		print(counttrainer)
		
		
	

	if 'email' not in session:
		return redirect('http://'+login_url)

	return render_template('home/dboard.html',userDetails=userDetails,purchaseDetails=purchaseDetails,var1=var1,vendorDetails=vendorDetails,trainerDetails=trainerDetails,countvendor=countvendor,counttrainer=counttrainer,countpurchase=countpurchase,countinvoice=countinvoice)


























