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
from flask import Markup
from forms import AccountForm
app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
sess = Session()
sess.init_app(app)
users = list(range(100))



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




@app.route("/newvendor",methods=['GET','POST'])
def newvendor():
	userDetails=""
	form=AccountForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name= userDetails['name'].capitalize() 
		address = userDetails['address']
		email = userDetails['email']
		gstin = userDetails['gstin'].upper() 
		pan = userDetails['pan'].upper() 
		cur2 = mysql.connection.cursor()
		var3= cur2.execute("SELECT email,address,pan from app where gstin='"+gstin+"' OR name='"+name+"' ")
		records = cur2.fetchall()
		count = len(records)
		print(count)
		if count == 0:
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO app(name,address,email,gstin,pan) VALUES(%s, %s, %s, %s, %s)",(name,address,email,gstin,pan))
			mysql.connection.commit()
			cur.close()
			return redirect(url_for('vendor'))
		else: 
		
			flash(' User already registered')
			
			return render_template('vendor/newvendor.html',var1=var1)	
			
			#if form.validate_on_submit():
		 	#flash(f'VendorDetails created for {form.name.data}!','success')
			#return redirect(url_for('vendor'))
	if 'email' not in session:
		return redirect('http://'+login_url)			
	return render_template('vendor/newvendor.html',var1=var1,userDetails=userDetails)
	
	

#@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
#@app.route('/vendor', defaults={'offset': 0},methods=['GET','POST'])
#@app.route('/vendor/<offset>',methods=['GET','POST'])

#def vendor(offset):
	#per_page = 10
	#search = ""
	#per_page = 10
	#vendorDetails = ""
	#userDetails =""
	#per_page = 10
	#offset = (int(offset)*10)

	#offset = (int(offset)*10)
	#cur = mysql.connection.cursor()
	#resultValue = cur.execute("SELECT * FROM app  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
	#if resultValue >= 0:
#		userDetails = cur.fetchall()
#
#	cur1 = mysql.connection.cursor()
#	resultValue1 = cur1.execute("SELECT count(*) FROM app ")
#
#	if resultValue1 >= 0:
#		detail = cur1.fetchall()
#		vendorDetails = detail[0]
		

#	return render_template('vendor/vendor.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)
@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/vendor', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/vendor/<offset>',methods=['GET','POST'])


def vendor(offset):
	#per_page = 10
	search = ""
	name = ""
  #per_page = 10
	vendorDetails = ""
	userDetails =""
	per_page = 10
	user = " "
	#offset = (int(offset)*10)

	offset = (int(offset)*10)
	if request.method == "POST":
		search = request.form['search']
	if search == "" or search == "all":


		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT * FROM app  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM app ")

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

    

	else:

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from app where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM app  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM app  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)
	if 'email' not in session:
		return redirect('http://'+login_url)
	

    
	return render_template('vendor/vendor.html',user = user,userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)

    
  	


#endpoint for search
#@app.route('/search', methods=['GET', 'POST'])
#def search():
#    if request.method == "POST":
#        search = request.form['search']
 #       # search by author or book
  #      cursor = cur2 = mysql.connection.cursor()
   #     cursor.execute("SELECT name, email,id from app WHERE name LIKE %s OR email LIKE %s or id LIKE %s", (search , search , search))
    #    data = cursor.fetchall()
     #   # all in the search box will return all the tuples
      #  if len(data) == 0 and search == 'all': 
       #     cursor.execute("SELECT * from app")
        #    data = cursor.fetchall()
        #return render_template('vendor/vendor.html', data=data,var1=var1)
    #return render_template('vendor/vendor.html',var1=var1)




@app.route("/checkvendor/<vend>",methods=['GET','POST'])
def checkvendor(vend):
        #offset = (int(offset)*10)
		cur2 = mysql.connection.cursor()
		count= cur2.execute("SELECT email,address,gstin,pan from app where name='"+vend+"'")
		print(count)
		return(str(count))		
		



	
	

@app.route('/getVendors')
def getVendors():
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id',name AS 'vendor name' ,address AS 'address',pan AS 'pan',email AS 'email',gstin AS 'gstin' FROM app")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)

@app.route("/demo")
def demo():
	return render_template('vendor/demo.html',var1=var1)


@app.route("/valid")
def valid():
	
	return render_template('vendor/valid.html',var1=var1)

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


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM app WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('vendor'))





@app.route('/update',methods=['POST','GET'])
def update():

	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		address = request.form['address']
		gstin = request.form['gstin']
		pan = request.form['pan']
		email = request.form['email']
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE app
				SET name=%s, address=%s,gstin=%s ,pan=%s,email=%s
				WHERE id=%s
				""", (name, address,gstin, pan,email,id_data))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		
		mysql.connection.commit()
	return redirect(url_for('vendor'))






	if __name__ == '__main__':
		app.run(debug=True)




	











