import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask import Markup
from flask_mysqldb import MySQL
from flask import jsonify,json
from forms import TrainerForm
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





@app.route("/newtrainer",methods=['GET','POST'])
def newtrainer():
	form=TrainerForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name= userDetails['name'].capitalize() 
		trainertype = userDetails['trainertype'].capitalize()
		print(trainertype)
		status = userDetails['status'].capitalize()
		gstin= userDetails['gstin'].upper() 
		pan = userDetails['pan'].upper() 
		acc1 = userDetails['acc1'].upper()
		acc2 = userDetails['acc2'].upper()
		acc3 = userDetails['acc3'].upper()
		acc4 = userDetails['acc4'].upper()
		tech1 = userDetails['tech1']
		tech2 = userDetails['tech2']
		tech3 = userDetails['tech3']
		cur3 = mysql.connection.cursor()
		var3= cur3.execute("SELECT * from trainer where gstin='"+gstin+"' OR name='"+name+"' ")
		records = cur3.fetchall()
		count = len(records)
		print(count)
		if count == 0:
		
			cur = mysql.connection.cursor()
			if trainertype == 'External':
				cur.execute("INSERT INTO trainer(name,trainertype,status,gstin,pan,acc1,acc2,acc3,acc4,tech1,tech2,tech3) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,trainertype,status,gstin,pan,acc1,acc2,acc3,acc4,tech1,tech2,tech3))
			mysql.connection.commit()
			cur.close()

			cur2 = mysql.connection.cursor()
			if trainertype == 'Internal':
				cur2.execute("INSERT INTO trainer(name,trainertype,status,tech1,tech2,tech3) VALUES(%s, %s, %s, %s, %s, %s)",(name,trainertype,status,tech1,tech2,tech3))
			mysql.connection.commit()
			cur2.close()
			return redirect(url_for('trainer'))
		else:
			flash(' User already registered')
			return render_template('trainer/newtrainer.html',var1=var1)	
			
		
	if 'email' not in session:
		return redirect('http://'+login_url)	
	return render_template('trainer/newtrainer.html',var1=var1,form=form)


@app.route('/getTrainers')
def getTrainers():
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id',name AS 'trainer name',trainertype AS 'type',status AS 'status',gstin AS 'gstin',pan AS 'pan',acc2 AS 'holdername' FROM trainer")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)	




@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/trainer', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/trainer/<offset>',methods=['GET','POST'])

 

def trainer(offset):
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
		resultValue = cur.execute("SELECT * FROM trainer  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

 

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM trainer ")

 

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

 



 

	else:

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from trainer where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM trainer  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM trainer where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)
	if 'email' not in session:
		return redirect('http://'+login_url)
	

	return render_template('trainer/trainer.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)




@app.route("/demo")
def demo():
	return render_template('trainer/demo.html',var1=var1)



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



@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM trainer WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('trainer'))





@app.route('/update',methods=['POST','GET'])
def update():

	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		trainertype = request.form['trainertype']
		gstin = request.form['gstin']
		pan = request.form['pan']
		#email = request.form['email']
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE trainer
				SET name=%s, trainertype=%s,gstin=%s ,pan=%s
				WHERE id=%s
				""", (name, trainertype,gstin, pan,id_data))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		
		mysql.connection.commit()
	return redirect(url_for('trainer'))












