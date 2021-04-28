import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import Markup
from werkzeug.utils import secure_filename
from flask import jsonify,json
from forms import BillForm
app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
sess = Session()
sess.init_app(app)
UPLOAD_FOLDER = 'C:/Users/Dell/app/upload'
import datetime






app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv' ,'xlsx' ,'doc', 'docx'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS	



@app.route("/newbill",methods=['GET','POST'])
def newvendor():
	form=BillForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		fileDetails = request.files
		name= userDetails['name'].capitalize() 
		#name.capitalize()
		description = userDetails['description']
		file = fileDetails['file']
		dated = userDetails['dated']
		amount = userDetails['amount']

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO expenses(name,description,file,dated,amount) VALUES(%s, %s, %s, %s, %s)",(name,description,file,dated,amount))
		mysql.connection.commit()
		cur.close()	
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			message = Markup('&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspFile successfully uploaded')
			flash(message)
			return redirect(url_for('bill'))
		else:
			fnmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAllowed file types are txt, pdf, png, jpg, jpeg, gif")
			flash(fnmessage)
		
			#flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif,csv,docx')
			return redirect(url_for('newbill'))
			#if form.validate_on_submit():
		 	#flash(f'InvoiceDetails created for {form.num.data}!','success')
		return redirect(url_for('bill'))
			
			
			#if form.validate_on_submit():
		 	#flash(f'VendorDetails created for {form.name.data}!','success')
			#return redirect(url_for('vendor'))

	if 'email' not in session:
		return redirect('http://'+login_url)			
	return render_template('bill/newbill.html',form=form,var1=var1)
	
	




@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/bill', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/bill/<offset>',methods=['GET','POST'])


def bill(offset):
	#per_page = 10
	search = ""
  #per_page = 10
	vendorDetails = ""
	userDetails =""
	per_page = 10
	#offset = (int(offset)*10)

	offset = (int(offset)*10)
	if 'loggedin' in session:


		if session['usertype'] == 'admin':
		 
		# Use
			
	
			if request.method == "POST":
				search = request.form['search']
			if search == "" or search == "all":


				cur = mysql.connection.cursor()
				resultValue = cur.execute("SELECT * FROM expenses  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
				if resultValue >= 0:
					userDetails = cur.fetchall()

				cur1 = mysql.connection.cursor()
				resultValue1 = cur1.execute("SELECT count(*) FROM expenses ")

				if resultValue1 >= 0:
					detail = cur1.fetchall()
					vendorDetails = tuple(detail[0])

    

			else:

				cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
				sql =  "SELECT * from expenses where id like %s or name like %s " 
				like_val = f'%{search}%'

		#adr = (search,search)

				resultValue = cur2.execute(sql, (like_val, like_val))
				if resultValue >= 0:
					userDetails = cur2.fetchall()

				cur3 = mysql.connection.cursor()
				sql = "SELECT * FROM expenses  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
				like_val = f'%{search}%'

				resultValue4 = cur3.execute(sql,(like_val, like_val))
				if resultValue4 >= 0:
					userDetails = cur3.fetchall()
			#print(user)


				cur4 = mysql.connection.cursor()
				sql = "SELECT count(*) FROM expenses  where id like %s or name like %s  "
		#adr = (id, name)
				like_val = f'%{search}%'
				resultValue5 = cur4.execute(sql,(like_val, like_val))
  
				if resultValue5 >= 0:
					detail = cur4.fetchall()
					vendorDetails = detail[0]
					print(vendorDetails)
			return render_template('bill/bill.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)			


		else:

			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			user1 = cursor.execute('SELECT * FROM expenses WHERE  name = %s', (session['name'],))
			if user1 >=0:
				user = cursor.fetchall()

			return render_template('bill/admin.html', user=user,var1=var1)
				
		if 'email' not in session:
			return redirect('http://'+login_url)

	# User is not loggedin redirect to login page


		# Show the profile page with account info
		



			




@app.route('/getBills')
def getBills():
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id',name AS ' name' ,description AS 'description',amount AS 'amount' FROM expenses")
		

		#print (date)
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)	


@app.route('/getAmounts')
def getAmounts():
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT amount AS 'amount' FROM expenses")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)	

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM expenses WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('bill'))





@app.route('/update',methods=['POST','GET'])
def update():

	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		description = request.form['description']
		dated = request.form['dated']
		amount = request.form['amount']
		status = request.form['status']
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE expenses
				SET name=%s, description=%s,dated = %s,amount=%s ,status=%s
				WHERE id=%s
				""", (name, description,dated, amount,status,id_data))
		message = Markup("Data Updated Successfully")
		flash(message,"success")
		
		mysql.connection.commit()
	return redirect(url_for('bill'))


@app.route('/updatenew',methods=['POST','GET'])
def updatenew():

	if request.method == 'POST':
		id_d = request.form['id']
		name = request.form['name']
		description = request.form['description']
		dated = request.form['dated']
		amount = request.form['amount']
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE expenses
				SET name=%s, description=%s,dated = %s,amount=%s
				WHERE id=%s
				""", (name, description,dated, amount,id_d))
		message = Markup("Data Updated Successfully")
		flash(message,"success")
		
		mysql.connection.commit()
	return redirect(url_for('bill'))




@app.route("/valid")
def valid():
	
	return render_template('bill/valid.html',var1=var1)

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



	if __name__ == '__main__':
		app.run(debug=True)




	











