import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask import Markup
from flask import jsonify,json
from forms import RegistrationForm



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

@app.route("/register",methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name= userDetails['name'].capitalize() 
		email = userDetails['email']
		password = userDetails['password']
		usertype = userDetails['usertype']


		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name,email,password,usertype) VALUES(%s, %s, %s, %s)",(name,email,password,usertype))
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('users'))
	if 'email' not in session:
		return redirect('http://'+login_url)	
	
	return render_template('admin/register.html',var1=var1,form=form)	




@app.route('/getUsers',methods=['GET','POST'])
def getUsers():
		
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id',name AS 'user name',email AS 'email',status AS 'status' FROM users")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)




@app.route('/newusers')	
def newusers():


	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM users")
	if resultValue >= 0:
		userDetails = cur.fetchall()
	mysql.connection.commit()
	cur.close()	
	


	return render_template('admin/newusers.html',userDetails=userDetails,var1=var1)



@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	messagenew = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(messagenew)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM users WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('users'))





@app.route('/update',methods=['POST','GET'])
def update():

	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		password = request.form['password']
		email = request.form['email']
		status = request.form['status']
		#usertype = request.form['usertype']
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE users
				SET name=%s,password=%s, email=%s, status=%s
				WHERE id=%s
				""", (name, password, email, status, id_data))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		mysql.connection.commit()
	return redirect(url_for('users'))





						



#	return render_template('admin/vendor.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)
@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/users', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/users/<offset>',methods=['GET','POST'])


def users(offset):
	#per_page = 10
	search = ""
  #per_page = 10
	vendorDetails = ""
	userDetails =""
	per_page = 10
	#offset = (int(offset)*10)

	offset = (int(offset)*10)
	if request.method == "POST":
		search = request.form['search']
	if search == "" or search == "all":


		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT * FROM users  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM users ")

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

    
	else:

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from users where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM users  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM users  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)
	if 'email' not in session:
		return redirect('http://'+login_url)
	

	return render_template('admin/users.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)


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



























