import os
import re
import redis
import ast
import pymysql
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session,make_response,send_file
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import jsonify,json
import pdfkit
from flask import Markup
from werkzeug.utils import secure_filename
from forms import InvoiceForm,RecieveForm,UpdateForm

import random
c = (random.randint(0,9))
print(c)

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
sess = Session()
sess.init_app(app)

UPLOAD_FOLDER = 'C:/Users/Dell/app/upload'



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



@app.route("/newinvoice",methods=['GET','POST'])
def newinvoice():
	y = ''
	
	
	#id =''
	#id = ''
	form=InvoiceForm()
	#if request.method == 'GET':
		#demo = request.form.get('demo')
		#arraynew = vardemo
		#data  = json.loads(arraynew)
		#print (data['vardemo'])
		#print(demo)


	#c ='MAG0001'
	num = ''
	if request.method == 'POST':
		
		#print(iddata)
		# Fetch form data
		userDetails = request.form
		#demo = userDetails['demo']
		#print(demo)
		iddata = request.form.get('id')
		name=userDetails['name'].capitalize() 
		#name="yatin"
		#print(name)
		ad=userDetails['ad'].capitalize() 
		gst=userDetails['gst'].capitalize() 
		pan=userDetails['pan'].capitalize() 

		train=userDetails['train'].capitalize() 
		num= userDetails['num']
		dated = userDetails['dated']
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		#pric = 100
		#print(pric)
		#id = request.form.get('id')
		#invoiceid = id
		item = request.form.getlist('item[]')
		#print(item)
		#for y in item:
			#demoy = y
			#print(demoy)
		description = request.form.getlist('description[]')
		#for x in description:
			#demox = x
			#print(demox)
		total = userDetails['total']
		subtotal = userDetails['subtotal']
		words = userDetails['words']
		email = userDetails['email']
		newgst = userDetails['newgst']
		#var2 = [name,ad,gst,pan,train,num,dated,item,description,total,subtotal,words,email,newgst]
		#for i in var2:
			#print(i)
		cur2 = mysql.connection.cursor()
		var3= cur2.execute("SELECT name,ad,gst,pan,train,dated,item,description,total,subtotal,words,email,newgst from invoiced where num='"+num+"'")
		records = cur2.fetchall()
		count = len(records)
		print(count)
		if count == 0:
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO invoiced(name,ad,gst,pan,train,num,dated,total,subtotal,words,email,newgst) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,ad,gst,pan,train,num,dated,total,subtotal,words,email,newgst)) 
			#vararray = [ item,description]
			
			invoiceid = cur.lastrowid
			#sql1 = cur.execute("SELECT id from invoiced WHERE id = %s)",[iddata,])
			#if sql1>= 0:
				#usernew = cur.fetchall()
				#print(sql1)
			
			for x,y,z,v,t in zip(item,description,unitcost,quantity,price):
				print(x)
				print(y)
				print(z)
				print(v)
				print(t)
				#for y in description:
					#print(y)

				
				#sqlnew =  "INSERT INTO invoiceorders(item,description,invoiceid) VALUES ( %s, %s, (SELECT id from invoiced WHERE id = %s) )"
				sqlnew =  "INSERT INTO invoiceorders(item,description,unitcost,quantity,price,invoiceid) VALUES (%s, %s, %s, %s, %s, %s)"

			
				args = (x, y ,z ,v,t,invoiceid)
				cur.execute(sqlnew , args)

			mysql.connection.commit()
		
		# cur.execute("select name from app")
		# vendor=cur.fetchall()
		# print(vendor)
			cur.close()
			#if form.validate_on_submit():
		 	#flash(f'InvoiceDetails created for {form.num.data}!','success')
			return redirect(url_for('invoice'))
		else:
			fmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspInvoice is already created")
			flash(fmessage)
			return redirect(url_for('newinvoice'))
			return render_template('invoice/newinvoice.html',var1=var1)		
	cur1 = mysql.connection.cursor()
	cur1.execute("select name from app")
	vendor=cur1.fetchall()
	print(vendor)
	cur1.close()
	cur2 = mysql.connection.cursor()
	cur2.execute("select address from app")
	address=cur2.fetchall()
	print(address)
	cur2.close()
	c = (random.randint(0,10000))
	


	if 'email' not in session:
		return redirect('http://'+login_url)
	return render_template('invoice/newinvoice.html',title='Invoice',c=c,form=form,vendor=vendor,address=address,var1=var1)


@app.route("/getadd/<vendor>",methods=['GET','POST'])
def getadd(vendor):
	#value=request.GET.getlist('add')
	cur2 = mysql.connection.cursor()
	cur2.execute("select email,address,gstin,pan from app where name='"+vendor+"'")
	row_headers=[x[0] for x in cur2.description] #this will extract row headers
	rv = cur2.fetchall()
	#return(rv)	
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	return json.dumps(json_data)

def get_users(offset=0, per_page=10):
	print(offset)
	print(per_page)
	print (users[offset: offset + per_page])
	return users[offset: offset + per_page]


def getall(offset=0, per_page=10):
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced LIMIT "+ str(offset) + " , "+str(per_page)+"")
	if resultValue >= 0:
		userDetails = cur.fetchall()
	print(userDetails)
	return userDetails


@app.route("/count")
def count():

	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced")
	if resultValue >= 0:
		userDetails = cur.fetchall()
	page, per_page, offset = get_page_args(page_parameter='page',
							per_page_parameter='per_page')
	total = len(users)
	pagination_users = getall(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')	
	return render_template('invoice/count.html',userDetails=userDetails,users=pagination_users,
							page=page,
							per_page=per_page,
							pagination=pagination)




						



#	return render_template('invoice/vendor.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)
@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/invoice', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/invoice/<offset>',methods=['GET','POST'])


def invoice(offset):
	order = ""
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
		resultValue = cur.execute("SELECT * FROM invoiced order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur6 = mysql.connection.cursor()
		resultValue6 = cur6.execute("SELECT * FROM invoiceorders ")
		if resultValue6 >= 0:
			orderDetails = cur6.fetchall()
	

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM invoiced ")


		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])
		
			

    

	else:

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from invoiced where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM invoiced where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM invoiced  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)

		cur7 = mysql.connection.cursor()
		resultValue7 = cur7.execute("SELECT * FROM invoiceorders ")
		if resultValue7 >= 0:
			orderDetails = cur7.fetchall()
		
	if 'email' not in session:
		return redirect('http://'+login_url)
	

    

    
	return render_template('invoice/invoice.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1,orderDetails=orderDetails,order=order)

def create_pdf(template_name,id):
	

	cur = mysql.connection.cursor()
	sql = "select * from invoiced where id = %s"
	#adr = (id)

	resultValue = cur.execute(sql,(id,))

	#resultValue = cur.execute("SELECT * FROM invoiced where id ='"+id+"'")
	if resultValue >= 0:
		pdf = cur.fetchall()
		#print(id)
		#print(type(pdf))
		#print(pdf)
		#count = len(pdf)
		#print(count)

	render = render_template(template_name, pdf=pdf)

	# so that wkhtmltopdf does not print anything
	options = {
		'quiet': ''
	}
	#False is there so that generated pdf is retained in memory, not written on disk
	pdf = pdfkit.from_string(render, False, options)
	return pdf

@app.route('/getpdf/<id>',methods=['GET','POST'])
def pdf_generator(id):
	#print(id)
	#pdf = ''
	#cur = mysql.connection.cursor()
	#resultValue = cur.execute("SELECT * FROM invoiced where id ='"+id+"'")
	#if resultValue >= 0:
		#userDetails = cur.fetchall()
		#print(userDetails)

	response = make_response(create_pdf("invoice/home.html",id))
	response.headers['Content-Type'] = 'application/pdf'
	#response.headers['Content-Disposition'] = 'attachment; filename=report.pdf' #attachement means download
	response.headers['Content-Disposition'] = 'inline; filename=report.pdf'
	return response	
	



@app.route('/demo')
def demo():
	return render_template('invoice/demo.html',var1=var1)

@app.route('/download')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	#path = "sample.txt"
	return send_file( as_attachment=True)	

@app.route('/new')	
def new():
	pdfkit.from_file('invoice/newinvoice.html', 'out.pdf')
	return render_template('invoice/newinvoice.html',var1=var1)




@app.route('/getInvoices')
def getInvoices():
        #per_page = 10
        #offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id' ,name AS 'vendor name' ,num AS 'invoice no',subtotal AS 'total' FROM invoiced ")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)


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
	
  
	

	

@app.route('/pdf',methods=['GET','POST'])	
def pdf():
	form=UpdateForm()
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced" )
	if resultValue >= 0:
		userDetails = cur.fetchall()
	mysql.connection.commit()
	cur.close()	
	
		#print(userDetails)
	#if request.method == 'POST':
		#name = request.form['name']
		#email = request.form['email']
		#status = request.form['status']
		#print(status)
		#id = request.form['id']
		#print(id)

		#cur1 = mysql.connection.cursor()
		#sql = cur1.execute("UPDATE invoiced SET status='1' where id='4'")

    
		#query = "UPDATE invoiced SET name = %s,status = %s WHERE id = %s"
		#data = (name, status, id)
		#sql = cur1.execute(query,data)
		##sql = cur1.execute("UPDATE invoiced SET name=%s, email=%s ,status=%s WHERE id=%s ", (name, email, status, id))
		#print(sql)
		
		#print(sql)
		#flash("hello hello Success")
		#mysql.connection.commit()
		#cur1.close()
		
		
		
		

		#cur.execute( "UPDATE invoiced SET status=1 WHERE id=2")
		#data = (name, ema, status, id,)
		#return redirect('/pdf')
		

	if 'email' not in session:
		return redirect('http://'+login_url)	

	return render_template('invoice/pdf.html',userDetails=userDetails,var1=var1,form=form)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS	


@app.route("/newinvoicerecieved",methods=['GET','POST'])
def newinvoicerecieved():
	form = RecieveForm()
	if request.method == 'POST':
		userDetails = request.form
		fileDetails = request.files
		name = userDetails['name'].capitalize() 
		#name="yatin"
		#print(name)
		
		gst = userDetails['gst'].capitalize() 
		pan = userDetails['pan'].capitalize() 
		file = fileDetails['file']
		
		num = userDetails['num']
		dated = userDetails['dated']
		#unitcost = userDetails['unitcost']
		#qty = userDetails['qty']
		print(userDetails)
		#pric = userDetails['pric']
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		
		#pric = 100
		#print(pric)
		item = request.form.getlist('item[]')
		description = request.form.getlist('description[]')
		total = userDetails['total']
		subtotal = userDetails['subtotal']
		words = userDetails['words']
		newgst = userDetails['newgst']


		cur2 = mysql.connection.cursor()
		var3= cur2.execute("SELECT name,gst,pan,file,dated,item,description,total,subtotal,words,newgst from recieved where num='"+num+"'")
		records = cur2.fetchall()
		count = len(records)
		print(count)
		if count == 0:
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO recieved(name,gst,pan,file,num,dated,total,subtotal,words,newgst) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,gst,pan,file,num,dated,total,subtotal,words,newgst))
			irid = cur.lastrowid
			
			for a,b,x,y,z   in zip(item,description,unitcost,quantity,price):
				print(a)
				print(b)
				print(z)
				print(x)
				print(y)
				#for y in description:
					#print(y)

				
				#sqlnew =  "INSERT INTO invoiceorders(item,description,invoiceid) VALUES ( %s, %s, (SELECT id from invoiced WHERE id = %s) )"
				query1 =  "INSERT INTO recievedorders(item,description,unitcost,quantity,price,irid) VALUES ( %s, %s, %s, %s, %s, %s)"

			
				args1 = (a, b,x, y,z,irid)
				cur.execute(query1 , args1)


			mysql.connection.commit()

			
					
		
		# cur.execute("select name from app")
		# vendor=cur.fetchall()
		# print(vendor)
			cur.close()
		else:
			newmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspInvoice is already created")
			flash(newmessage)
		
			#flash(' Invoice is already created')
			return redirect(url_for('newinvoicerecieved'))	
		if request.method == 'POST':	
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspFile Successfully Uploaded")
				flash(message)
		
				return redirect(url_for('invoicerecieved'))
			else:
				fnmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAllowed file types are txt, pdf, png, jpg, jpeg, gif")
				flash(fnmessage)
		
				#flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
				#return redirect(url_for('newinvoicerecieved'))
				return render_template('invoice/newinvoicerecieved.html',var1=var1)
			#if form.validate_on_submit():
		 	#flash(f'InvoiceDetails created for {form.num.data}!','success')
			return redirect(url_for('invoicerecieved'))
	

	
	cur1 = mysql.connection.cursor()
	cur1.execute("select name from trainer")
	vendornew=cur1.fetchall()
	print(vendornew)
	cur1.close()
	cur2 = mysql.connection.cursor()
	cur2.execute("select trainertype from trainer")
	address=cur2.fetchall()
	print(address)
	cur2.close()
	#cur3 = mysql.connection.cursor()
	#cur3.execute("select num+1 from recieved order by num DESC LIMIT 1")
	#numbernew = cur3.fetchone()
	#tup = str(numbernew)
	#b = tup.strip("(").strip(")").strip(",")
	#cur3.close()
	b = (random.randint(0,10000))

	#numbernew = int(invoicenew)
	print(b)
	if 'email' not in session:
		return redirect('http://'+login_url)
	return render_template('invoice/newinvoicerecieved.html',title='Recieved',form=form,b=b,vendornew=vendornew,address=address,var1=var1)





						



#	return render_template('invoice/vendor.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)

@app.route('/invoicerecieved', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/invoicerecieved/<offset>',methods=['GET','POST'])


def invoicerecieved(offset):
	#per_page = 10
	search = ""
	order =""
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
		resultValue = cur.execute("SELECT * FROM recieved  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM recieved ")

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

    

	else:

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from recieved where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM recieved  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM recieved  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)

	if 'email' not in session:
		return redirect('http://'+login_url)
	

	return render_template('invoice/invoicerecieved.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)

@app.route('/getRecieves')
def getRecieves():
		cur = mysql.connection.cursor()
		newresult = cur.execute("SELECT id AS 'id' ,name AS 'trainer name' ,num AS 'invoice no',subtotal AS 'total' FROM recieved ")
		columns = [desc[0] for desc in cur.description]
		result = []
		rows = cur.fetchall()
		for row in rows:
			row = dict(zip(columns,row))
			result.append(row)
		return jsonify(result)



@app.route("/getnew/<vendor>",methods=['GET','POST'])
def getnew(vendor):
	#value=request.GET.getlist('add')
	cur2 = mysql.connection.cursor()
	cur2.execute("select gstin,pan from trainer where name='"+vendor+"'")
	row_headers=[x[0] for x in cur2.description] #this will extract row headers
	rv = cur2.fetchall()
	#return(rv)
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	return json.dumps(json_data)
  

@app.route("/newpdf/<id_data>/<name>/<location>",methods=['GET','POST'])
def newpdf(id_data,name,location):
	id_data = str(id)
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM invoiced where id ='"+id_data+"'")
	if resultValue >= 0:
		pdf = cur.fetchall()
		print(pdf)
		count = len(pdf)
		print(count)

	rendered = render_template('invoice/newdemo.html', name=name,location=location,var1=var1,pdf=pdf,id_data=id_data)
	pdf = pdfkit.from_string(rendered, False)

	response = make_response(pdf)
	response.headers['Content-Type'] = 'application/pdf'
	#response.headers['Content-Disposition'] = 'attachment; filename=report.pdf' #attachement means download
	response.headers['Content-Disposition'] = 'inline; filename=report.pdf'

	return response
@app.route("/pod")
def pod():
	return render_template('invoice/newdemo.html',var1=var1)





@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM invoiceorders where invoiceid=%s",(id_data,))
	cur.execute("DELETE FROM invoiced WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('invoice'))





@app.route('/update/<id>',methods=['POST','GET'])
def update(id):
	pdf=""
	cur = mysql.connection.cursor()
	sql = "select * from invoiced where id = %s"
	#adr = (id)

	resultValue = cur.execute(sql,(id,))

	
	

	if resultValue >= 0:
		userDetails = cur.fetchall()
		#print(userDetails)	

	
		#print(a)
		#print(b)

	cur1 = mysql.connection.cursor()	
			
	sql2 = "select * from invoiceorders where invoiceid = %s"	

	result = cur1.execute(sql2,(id,))	
	if result >=0:
		orderitem = cur1.fetchall()
		#print(orderitem)


			

	cur.execute("select name from app")
	vendor=cur.fetchall()
			
				


	if 'email' not in session:
		return redirect('http://'+login_url)

	if request.method == 'POST':
		#id_new = request.form['invoiceid']
		#orderid = request.form['orderid']
		name = request.form['name']
		email = request.form['email']
		gst = request.form['gst']
		pan = request.form['pan']
		train = request.form['train']
		status = request.form['status']
		total = request.form['total']
		newgst = request.form['newgst']
		subtotal = request.form['subtotal']
		words = request.form['words']



		item = request.form.getlist('item[]')
		#print(item)
		description = request.form.getlist('description[]')
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		#print(description)
		#orderid = cur.execute("SELECT orderid from invoiceorders WHERE item =%s")
		cur.execute("DELETE FROM invoiceorders where invoiceid=%s",(id,))
		#for it1 in item:
			#print(it1)
		#for de2 in description:
			#print(de2)
			
		

			#query = "SELECT orderid FROM invoiceorders WHERE item = %s and  description = %s"
			#args2 = (c,d)
			#cur.execute(query,args2)
			#id_new = cur.fetchone()[0]
			#print(id_new)
			#query = " SELECT invoiceid from invoiceorders WHERE item = %s and  description = %s"
			#args2 = (a,b)
			#cur.execute(query,args2)
			#invoiceid = cur.fetchone()
			#print(invoiceid)

		for it,de,x,y,z in zip(item,description,unitcost,quantity,price):
			print(it)
			print(de)
			print(x)
			print(y)
			print(z)

	
			sqlnew3 =  "INSERT INTO invoiceorders(item,description,unitcost,quantity,price,invoiceid) VALUES (%s, %s, %s, %s, %s, %s)"

			
			args4 = (it, de ,x,y,z,id,)
			cur.execute(sqlnew3 , args4)
			


			#cur.execute("""
			#		UPDATE invoiceorders
			#		SET item=%s, description=%s
			#		WHERE  orderid=%s
			#		""", (c,d,id_new))
		
		
		cur.execute("""
			UPDATE invoiced
			SET name=%s, email=%s, status=%s,gst=%s ,pan=%s , train= %s,total=%s, newgst=%s, subtotal=%s, words=%s
			WHERE id=%s
			""", (name, email, status,gst,pan,train,total,newgst,subtotal,words,id))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		
		mysql.connection.commit()
		cur.close()
		
	

		return redirect(url_for('invoice'))
	#return render_template('invoice/edit.html',var1=var1,pdf=pdf)		
	
		

	return render_template('invoice/edit.html',userDetails=userDetails,var1=var1,pdf=pdf,orderitem=orderitem,vendor=vendor)



	
	
	



@app.route('/deletenew/<string:id_data>', methods = ['GET'])
def deletenew(id_data):
	newmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")	
	flash(newmessage)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM recievedorders where irid=%s",(id_data,))
	cur.execute("DELETE FROM recieved WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('invoicerecieved'))



@app.route('/updatenew/<id>',methods=['POST','GET'])
def updatenew(id):
	details=""
	cur = mysql.connection.cursor()
	sql = "select * from recieved where id = %s"
	#adr = (id)

	resultValue = cur.execute(sql,(id,))

	
	

	if resultValue >= 0:
		userDetails = cur.fetchall()
		#print(userDetails)	

	
		#print(a)
		#print(b)

	cur1 = mysql.connection.cursor()	
			
	sql2 = "select * from recievedorders where irid = %s"	

	result = cur1.execute(sql2,(id,))	
	if result >=0:
		orderitem = cur1.fetchall()

		#print(orderitem)

	cur.execute("select name from trainer")
	vendornew=cur.fetchall()
	
			

			
				


	if 'email' not in session:
		return redirect('http://'+login_url)


	if request.method == 'POST':
		#id_data = request.form['id']
		name = request.form['name']
		gst = request.form['gst']
		pan = request.form['pan']
		status = request.form['status']
		total = request.form['total']
		newgst = request.form['newgst']
		subtotal = request.form['subtotal']
		words = request.form['words']



		#file = request.form['file']
		item = request.form.getlist('item[]')
		#print(item)
		description = request.form.getlist('description[]')
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		#print(description)
		#orderid = cur.execute("SELECT orderid from invoiceorders WHERE item =%s")
		cur.execute("DELETE FROM recievedorders where irid=%s",(id,))

		for it,de,x,y,z  in zip(item,description,unitcost,quantity,price):
			print(it)
			print(de)
			print(x)
			print(y)


	
			sqlnew3 =  "INSERT INTO recievedorders(item,description,unitcost,quantity,price,irid) VALUES (%s, %s, %s, %s, %s, %s )"

			
			args4 = (it, de ,x,y,z,id,)
			cur.execute(sqlnew3 , args4)
			


		
		
	
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE recieved
				SET name=%s, gst=%s, pan= %s, status=%s ,total=%s, newgst=%s, subtotal=%s, words=%s
				WHERE id=%s
				""", (name, gst,pan, status,total,newgst,subtotal,words,id))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('invoicerecieved'))

	return render_template('invoice/newedit.html',userDetails=userDetails,var1=var1,details=details,orderitem=orderitem,vendornew=vendornew)	















		



	
	

	
	




















