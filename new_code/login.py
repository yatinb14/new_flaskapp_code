import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask import jsonify,json
from forms import RegistrationForm

app = Flask(__name__)
SESSION_TYPE = 'redis'
SESSION_REDIS = redis.from_url('redis://127.0.0.1:6379')





app.config.from_object(__name__)
sess = Session()
sess.init_app(app)

@app.route('/set/')
def set():
	session['key'] = 123
	return 'ok'

@app.route('/get/')
def get():
	return session.get('key', 'not set')




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



@app.route("/register",methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name= userDetails['name']
		email = userDetails['email']
		password = userDetails['password']


		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name,email,password) VALUES(%s, %s, %s)",(name,email,password))
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('login'))
	if 'email' not in session:
		return redirect('http://'+login_url)
	return render_template('login/register.html',var1=var1,form=form)	


@app.route("/",methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
	error = ''
	
    # Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and'email' in request.form and 'password' in request.form:
        # Create variables for easy access
		email = request.form['email']
		password = request.form['password']

		status = request.form.get('status')
		print(status)
			# Check if account exists using MySQL
		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cur.execute('SELECT * FROM users WHERE status >= 1 AND email = %s AND password = %s', ( email, password))

		# Fetch one record and return result
		user = cur.fetchone()


		# If account exists in accounts table in out database
		if user:
			# Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['id'] = user['id']
			session['name'] = user['name']
			session['usertype'] = user['usertype']
			session['email'] = user['email']




			#flash('Welcome %s' % email)
			#print('http://'+home_url)
			return redirect('http://'+home_url)
		else:
			error = 'Incorrect email/password!'
			

	return render_template('login/login.html', error=error,var1=var1)



@app.route("/home", methods=['GET', 'POST'])
def home():	
	if 'email' not in session:
		return redirect(url_for('login'))
	return render_template('login/home.html',var1=var1)



	



@app.route("/logout",methods=['GET', 'POST'])  
def logout():  
	session.clear()
	return render_template('login/login.html',var1=var1) 

























