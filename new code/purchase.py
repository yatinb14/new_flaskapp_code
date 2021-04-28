import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session,make_response,send_file
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import jsonify,json
import pdfkit
from werkzeug.utils import secure_filename
from forms import InvoiceForm,RecieveForm
from flask import Markup
import random
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

@app.route("/newpurchase",methods=['GET','POST'])
def newpurchase():
	form=InvoiceForm()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name=userDetails['name'].capitalize() 
		#name="yatin"
		#print(name)
		ad=userDetails['ad'].capitalize() 
		gst=userDetails['gst'].capitalize() 
		pan=userDetails['pan'].capitalize() 
		email=userDetails['email']
		train=userDetails['train']
		num= userDetails['num']
		dated = userDetails['dated']
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		#unitcost = userDetails['unitcost']
		#qty = userDetails['qty']
		print(userDetails)
		#pric = userDetails['pric']
		
		#pric = 100
		#print(pric)
		item = request.form.getlist('item[]')
		description = request.form.getlist('description[]')
		total = userDetails['total']
		subtotal = userDetails['subtotal']
		words = userDetails['words']
		newgst = userDetails['newgst']
		cur2 = mysql.connection.cursor()
		var3= cur2.execute("SELECT name,ad,gst,pan,train,dated,item,description,total,subtotal,words,email,newgst from purchase where num='"+num+"'")
		records = cur2.fetchall()
		count = len(records)
		print(count)
		if count == 0:
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO purchase(name,ad,gst,pan,train,num,dated,total,subtotal,words,email,newgst) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,ad,gst,pan,train,num,dated,total,subtotal,words,email,newgst))
			purchaseid = cur.lastrowid
			
			for x,y,h,g,j   in zip(item,description,unitcost,quantity,price):
				print(x)
				print(y)
				print(h)
				print(g)
				print(j)
				#for y in description:
					#print(y)

				
				#sqlnew =  "INSERT INTO invoiceorders(item,description,invoiceid) VALUES ( %s, %s, (SELECT id from invoiced WHERE id = %s) )"
				sqlnew =  "INSERT INTO purchaseorders(item,description,unitcost,quantity,price,purchaseid) VALUES ( %s, %s, %s, %s, %s, %s)"

			
				args = (x, y ,h, g,j,purchaseid)
				cur.execute(sqlnew , args)


			
			mysql.connection.commit()
			# cur.execute("select name from app")
			# vendor=cur.fetchall()
			# print(vendor)
			cur.close()
		#if form.validate_on_submit():
		 #flash(f'PO Details created for {form.num.data}!','success')
			return redirect(url_for('purchase'))
		else:
			fmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspPO is already created,use different number")
			flash(fmessage)
		
			
			return redirect(url_for('newpurchase'))	
	cur1 = mysql.connection.cursor()
	cur1.execute("select name from app")
	vendor=cur1.fetchall()
	#print(vendor)
	cur1.close()
	cur2 = mysql.connection.cursor()
	cur2.execute("select address from app")
	address=cur2.fetchall()
	#print(address)
	cur2.close()
	#cur3 = mysql.connection.cursor()
	#cur3.execute("select num+1 from purchase order by num DESC LIMIT 1")
	#numbernew = cur3.fetchone()
	#tup = str(numbernew)
	#c = tup.strip("(").strip(")").strip(",")
	#cur3.close()
	c = (random.randint(0,10000))
	if 'email' not in session:
		return redirect('http://'+login_url)
	return render_template('purchase/newpurchase.html',c=c,title='NewPurchase',form=form,vendor=vendor,address=address,var1=var1)





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
	resultValue = cur.execute("SELECT * FROM purchase LIMIT "+ str(offset) + " , "+str(per_page)+"")
	if resultValue >= 0:
		userDetails = cur.fetchall()
	print(userDetails)
	return userDetails


@app.route("/count")
def count():

	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM purchase")
	if resultValue >= 0:
		userDetails = cur.fetchall()
	page, per_page, offset = get_page_args(page_parameter='page',
							per_page_parameter='per_page')
	total = len(users)
	pagination_users = getall(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')	
	return render_template('purchase/count.html',userDetails=userDetails,users=pagination_users,
							page=page,
							per_page=per_page,
							pagination=pagination)




@app.route('/', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/purchase', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/purchase/<offset>',methods=['GET','POST'])


def purchase(offset):
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
		resultValue = cur.execute("SELECT * FROM purchase order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM purchase ")

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

    

	else:

		

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from purchase where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM purchase  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM purchase  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)
	if 'email' not in session:
		return redirect('http://'+login_url)
	

    

    
	return render_template('purchase/purchase.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)


@app.route('/getPurchases')
def getPurchases():
		#per_page = 10
		#offset = (int(offset)*10)
		cur = mysql.connection.cursor()
		resultValue = cur.execute("SELECT id AS 'id' ,name AS 'vendor name' ,num AS 'invoice no',subtotal AS 'total' FROM purchase")
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

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS		


@app.route("/newpurchaserecieved",methods=['GET','POST'])
def newpurchaserecieved():
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
		unitcost = request.form.getlist('unitcost[]')
		print(unitcost)
		quantity = request.form.getlist('quantity[]')
		print(quantity)
		#print(userDetails)
		price = request.form.getlist('price[]')
		print(price)
		
		#pric = userDetails['pric']
		
		#pric = 100
		#print(pric)
		item = request.form.getlist('item[]')
		description = request.form.getlist('description[]')
		total = userDetails['total']
		subtotal = userDetails['subtotal']
		words = userDetails['words']
		newgst = userDetails['newgst']
		cur2 = mysql.connection.cursor()
		var3= cur2.execute("SELECT name,gst,pan,file,dated,total,subtotal,words ,newgst from newrecieved where num='"+num+"'")
		records = cur2.fetchall()
		count = len(records)
		print(count)
		if count == 0:
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO newrecieved(name,gst,pan,file,num,dated,total,subtotal,words,newgst) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name,gst,pan,file,num,dated,total,subtotal,words,newgst))
			prid = cur.lastrowid
			
			for a,b,l,m,n in zip(item,description,unitcost,quantity,price):
				print(a)
				print(b)
				print(l)
				print(m)
				print(n)
				#for y in description:
					#print(y)

				
				#sqlnew =  "INSERT INTO invoiceorders(item,description,invoiceid) VALUES ( %s, %s, (SELECT id from invoiced WHERE id = %s) )"
				query1 =  "INSERT INTO newrecievedorders(item,description,unitcost,quantity,price,prid) VALUES (%s, %s, %s, %s, %s, %s)"

			
				args1 = (a, b ,l, m ,n, prid)
				cur.execute(query1 , args1)


			
			mysql.connection.commit()

			
					
		
		# cur.execute("select name from app")
		# vendor=cur.fetchall()
		# print(vendor)
			cur.close()
		else:
			fmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspPO is already created")
			flash(fmessage)
		
			return redirect(url_for('newpurchaserecieved'))	
		if request.method == 'POST':	
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspFile Successfully Uploaded")
				flash(message)
		
				#flash('File successfully uploaded')
				return redirect(url_for('purchaserecieved'))
			else:
				fnmessage = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspAllowed file types are txt, pdf, png, jpg, jpeg, gif")
				flash(fnmessage)
		
				#flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
				return redirect(url_for('newpurchaserecieved'))
			#if form.validate_on_submit():
		 	#flash(f'InvoiceDetails created for {form.num.data}!','success')
			return redirect(url_for('purchaserecieved'))
	

	
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
	#cur3.execute("select num+1 from newrecieved order by num DESC LIMIT 1")
	#numbernew = cur3.fetchone()
	#tup = str(numbernew)
	#b = tup.strip("(").strip(")").strip(",")
	#cur3.close()
	b = (random.randint(0,10000))
	if 'email' not in session:
		return redirect('http://'+login_url)
	return render_template('purchase/newpurchaserecieved.html',b=b,title='Recieved',form=form,vendornew=vendornew,address=address,var1=var1)



@app.route('/purchaserecieved', defaults={'offset': 0},methods=['GET','POST'])
@app.route('/purchaserecieved/<offset>',methods=['GET','POST'])


def purchaserecieved(offset):
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
		resultValue = cur.execute("SELECT * FROM newrecieved  order by id LIMIT "+ str(offset) + " , "+str(per_page)+"")
		if resultValue >= 0:
			userDetails = cur.fetchall()

		cur1 = mysql.connection.cursor()
		resultValue1 = cur1.execute("SELECT count(*) FROM newrecieved ")

		if resultValue1 >= 0:
			detail = cur1.fetchall()
			vendorDetails = tuple(detail[0])

    

	else:

		

		cur2 = mysql.connection.cursor()
    #sql = "SELECT * from app where name LIKE %s OR email LIKE %s or id LIKE %s", (se
		sql =  "SELECT * from newrecieved where id like %s or name like %s " 
		like_val = f'%{search}%'

		#adr = (search,search)

		resultValue = cur2.execute(sql, (like_val, like_val))
		if resultValue >= 0:
			userDetails = cur2.fetchall()

		cur3 = mysql.connection.cursor()
		sql = "SELECT * FROM newrecieved  where id like %s or name like %s  order by id LIMIT "+ str(offset) + " , "+str(per_page)+""
		#adr = (id,name)
		like_val = f'%{search}%'

		resultValue4 = cur3.execute(sql,(like_val, like_val))
		if resultValue4 >= 0:
			userDetails = cur3.fetchall()
			#print(user)


		cur4 = mysql.connection.cursor()
		sql = "SELECT count(*) FROM newrecieved  where id like %s or name like %s  "
		#adr = (id, name)
		like_val = f'%{search}%'
		resultValue5 = cur4.execute(sql,(like_val, like_val))
  
		if resultValue5 >= 0:
			detail = cur4.fetchall()
			vendorDetails = detail[0]
			print(vendorDetails)
	if 'email' not in session:
		return redirect('http://'+login_url)
	

    
    
	return render_template('purchase/purchaserecieved.html',userDetails=userDetails,vendorDetails=vendorDetails,var1=var1)


@app.route('/getPORecieves')
def getPORecieves():
		cur = mysql.connection.cursor()
		newresult = cur.execute("SELECT id AS 'id' ,name AS 'vendor name' ,num AS 'invoice no',subtotal AS 'total' FROM newrecieved ")
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
  
def create_pdf(template_name,id):
	

	cur = mysql.connection.cursor()
	sql = "select * from purchase where id = %s"
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

	response = make_response(create_pdf("purchase/home.html",id))
	response.headers['Content-Type'] = 'application/pdf'
	#response.headers['Content-Disposition'] = 'attachment; filename=report.pdf' #attachement means download
	response.headers['Content-Disposition'] = 'inline; filename=report.pdf'
	return response	





@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM purchaseorders where purchaseid=%s",(id_data,))
	cur.execute("DELETE FROM purchase WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('purchase'))





@app.route('/update/<id>',methods=['POST','GET'])
def update(id):
	pdf=""
	cur = mysql.connection.cursor()
	sql = "select * from purchase where id = %s"
	#adr = (id)

	resultValue = cur.execute(sql,(id,))

	
	

	if resultValue >= 0:
		userDetails = cur.fetchall()
		#print(userDetails)	

	
		#print(a)
		#print(b)

	cur1 = mysql.connection.cursor()	
			
	sql2 = "select * from purchaseorders where purchaseid = %s"	

	result = cur1.execute(sql2,(id,))	
	if result >=0:
		orderitem = cur1.fetchall()
		#print(orderitem)


			

			
				
	
	cur.execute("select name from app")
	vendor=cur.fetchall()
	#print(vendor)
	


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
		cur.execute("DELETE FROM purchaseorders where purchaseid=%s",(id,))
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

		for it,de,h,g,j in zip(item,description,unitcost,quantity,price):
			print(it)
			print(de)
			print(h)
			print(g)
			print(j)

	
			sqlnew3 =  "INSERT INTO purchaseorders(item,description,unitcost,quantity,price,purchaseid) VALUES (%s, %s, %s, %s, %s, %s )"

			
			args4 = (it, de, h, g, j, id,)
			cur.execute(sqlnew3 , args4)
			

		cur.execute("""
			UPDATE purchase
			SET name=%s, email=%s, status=%s,gst=%s ,pan=%s , train= %s,total=%s, newgst=%s, subtotal=%s, words=%s
			WHERE id=%s
			""", (name, email, status,gst,pan,train,total,newgst,subtotal,words,id))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		
		mysql.connection.commit()
		cur.close()
		
	

		return redirect(url_for('purchase'))
	#return render_template('purchase/edit.html',var1=var1,pdf=pdf)		
	
		

	return render_template('purchase/edit.html',userDetails=userDetails,var1=var1,pdf=pdf,orderitem=orderitem,vendor=vendor)



	
	
	


@app.route('/deletenew/<string:id_data>', methods = ['GET'])
def deletenew(id_data):
	message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRecord Has Been Deleted Successfully")
	flash(message)
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM newrecievedorders where prid=%s",(id_data,))
	cur.execute("DELETE FROM newrecieved WHERE id=%s", (id_data,))
	mysql.connection.commit()
	return redirect(url_for('purchaserecieved'))




@app.route('/updatenew/<id>',methods=['POST','GET'])
def updatenew(id):
	details=""
	folder = 'C:/Users/Dell/app/upload'
	cur = mysql.connection.cursor()
	sql = "select * from newrecieved where id = %s"
	#adr = (id)

	resultValue = cur.execute(sql,(id,))

	
	

	if resultValue >= 0:
		userDetails = cur.fetchall()
		#print(userDetails)	

	
		#print(a)
		#print(b)

	cur1 = mysql.connection.cursor()	
			
	sql2 = "select * from newrecievedorders where prid = %s"	

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
		file = request.form['file']
		
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
		cur.execute("DELETE FROM newrecievedorders where prid=%s",(id,))

		for it,de,l,m,n in zip(item,description,unitcost,quantity,price):
		#	print(it)
		#	print(de)

	
			sqlnew3 =  "INSERT INTO newrecievedorders(item,description,unitcost,quantity,price,prid) VALUES ( %s, %s, %s, %s, %s, %s )"

			
			args4 = (it, de,l, m, n ,id,)
			cur.execute(sqlnew3 , args4)
			


		
		
	
		cur = mysql.connection.cursor()
		cur.execute("""
				UPDATE newrecieved
				SET name=%s, gst=%s, pan= %s, status=%s, total=%s, newgst=%s, subtotal=%s, words=%s
				WHERE id=%s
				""", (name, gst,pan, status,total,newgst,subtotal,words, id))
		message = Markup("&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspData Updated Successfully")
		flash(message)
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('purchaserecieved'))

	return render_template('purchase/newedit.html',userDetails=userDetails,folder=folder,var1=var1,details=details,orderitem=orderitem,vendornew=vendornew)	






#def send_image(filename):
	#return send_from_directory("upload", filename)












	














