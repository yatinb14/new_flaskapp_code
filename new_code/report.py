import os
import re
import redis
from os import environ
from flask import Flask,render_template,url_for,flash,redirect,request,session,make_response,Response
from flask_session.__init__ import Session
from flask_mysqldb import MySQL,MySQLdb
import MySQLdb.cursors
from flask_mysqldb import MySQL
from flask import jsonify,json

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
sess = Session()
sess.init_app(app)

from datetime import datetime, timedelta

sub = datetime.today() - timedelta(days=90)

#print(sub)


from datetime import datetime
import datetime
dt = datetime.datetime.today()
month = f'{dt.month:02d}'
#print(month)
#print(type(month))
year = dt.year
#print(year)
dtt = int(month) - 1
#print (dtt)

d = dt.year
#print(d)
lastyear = d - 1
#print(lastyear)

e = str(lastyear)+ "-" +str('1')+ "-" +str('01')
#print(e)
f = str(lastyear)+ "-" +str('12')+ "-" +str('31')
#print(f)
b = str(year)+ "-" +str(dtt)+ "-" +str('01')
#print(b)
c = str(year)+ "-" +str(dtt)+ "-" +str('31')
#print(c)
#sub1 = str(c) - str('90')
#print(sub1)
a_date = datetime.date(year, dtt, 31)
#print(a_date)

days = datetime.timedelta(90)
halfyear = datetime.timedelta(180)
one = datetime.timedelta(30)
print(one)
newone = a_date - one
print(newone)
#print(a_date)
newonemonth = datetime.datetime.strptime(str(newone), "%Y-%m-%d")
print(newone.year)
print(newone.month)
fromdated = str(newonemonth.year)+ "-" +str(newonemonth.month)+ "-" +str('01')#onemonthvariable
print(fromdated)

newdated = a_date - halfyear
newexample = datetime.datetime.strptime(str(newdated), "%Y-%m-%d")
#print(newexample.year)
#print(newexample.month)
y = str(newexample.year)+ "-" +str(newexample.month)+ "-" +str('01')#half yearly variable
#print(y)

#print(newdated)


new_date = a_date - days
example = datetime.datetime.strptime(str(new_date), "%Y-%m-%d")

#print(example.year)
#print(example.month)
h = str(example.year)+ "-" +str(example.month)+ "-" +str('01')
#print(h)
#print(new_date)







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
@app.route("/report",methods=['GET','POST'])
def report():
	if request.method == 'POST':
		# Fetch form data
		user = request.form
		fromdate= user['fromdate']
		todate = user['todate']
		#today = datetime.today.month()
		#datem = datetime(today.year, today.month, 1)
		#print(today)
		#print(datem)
		dt = datetime.datetime.today()
		year = dt.year
		print(year)
		dtt = dt.month -1
		print(dtt.year)

		print("Total rows are:  ", len(userDetails))

		print("Printing each row")
		for row in userDetails:
			print("Id: ", row[0])
			print("Name: ", row[1])
			print("Email: ", row[2])
			print("Salary: ", row[3])
			print("")
	if 'email' not in session:
		return redirect('http://'+login_url)		

	return render_template("report/report.html",var1=var1)

@app.route("/home")
def home():
	return render_template('report/home.html',var1=var1)





def create_pdf(template_name, data):
	render = render_template(template_name, data=data)

	# so that wkhtmltopdf does not print anything
	options = {
		'quiet': ''
	}
	#False is there so that generated pdf is retained in memory, not written on disk
	pdf = pdfkit.from_string(render, False, options)
	return pdf

@app.route('/pdf/<date>')
def pdf_generator(date):
	response = make_response(create_pdf("report/template.html", {"date": date}))
	response.headers['Content-Type'] = 'application/pdf'
	response.headers['Content-Disposition'] = 'inline; filename=report.pdf'
	return response	

@app.route("/hello")
def hello():
	return '''
		<html><body>
		Hello. <a href="/getcsv">Click me.</a>
		</body></html>
		'''



@app.route("/getcsv",methods=['GET','POST'])
def getcsv():
	fromdate =''
	todate = ''
	service = ''
	duration =''
	from datetime import datetime, timedelta

	sub = datetime.today() - timedelta(days=90)

	print(sub)

	import datetime
	dt = datetime.datetime.today()
	month = f'{dt.month:02d}'
	print(month)
	print(type(month))
	year = dt.year
	print(year)
	dtt = int(month) - 1
	print (dtt)
	a = 1
	d = dt.year
	print(d)
	lastyear = d - 1
	print(lastyear)

	e = str(lastyear)+ "-" +str('01')+ "-" +str('01')
	print(e)
	f = str(lastyear)+ "-" +str('12')+ "-" +str('31')
	print(f)

	fromdated = str(year)+ "-" +str(dtt)+ "-" +str('01')
	print(fromdated)
	todated = str(year)+ "-" +str(dtt)+ "-" +str('31')
	print(todated)
	a_date = datetime.date(year, dtt, 31)
	print(a_date)
	days = datetime.timedelta(90)
	new_date = a_date - days
	example = datetime.datetime.strptime(str(new_date), "%Y-%m-%d")

	print(example.year)
	print(example.month)
	h = str(example.year)+ "-" +str(example.month)+ "-" +str('01')#valueof quarter year in hardcode
	print(h)
	print(new_date)
	

	
	halfyear = datetime.timedelta(180)
	newdated = a_date - halfyear
	print(newdated)
	newexample = datetime.datetime.strptime(str(newdated), "%Y-%m-%d")
	print(newexample.year)
	print(newexample.month)
	y = str(newexample.year)+ "-" +str(newexample.month)+ "-" +str('01')#half yearly variable
	print(y)






	if request.method == 'POST':
		# Fetch form data
		user = request.form
		fromdate= user['fromdate']
		print(fromdate)
		todate = user['todate']
		
		service = user['service']
		duration = user['duration']
	
		print(user)
	csv = ' '
	cur = mysql.connection.cursor()

	



	#resultValue = cur.execute("SELECT * from purchase where dated >= %s and dated <= %s")
	if service == 'purchase':
		if duration == 'onemonth':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (fromdated,todated)

			resultValue = cur.execute(sql, adr)

			

			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'quarter':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 90 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (h,a_date)

			resultValue = cur.execute(sql, adr)


			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'half':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 180 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (y,a_date)

			resultValue = cur.execute(sql, adr)

			
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'oneyear':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (e,f)

			resultValue = cur.execute(sql, adr)
			
			

			
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"




		else:
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (fromdate,todate )

			resultValue = cur.execute(sql, adr)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"


	
	


 


	if service =='invoice':
		if duration == 'onemonth':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW();"
			

			resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'quarter':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 90 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (h,a_date)

			resultValue = cur.execute(sql, adr)

			

			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'half':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 180 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (y,a_date)

			resultValue = cur.execute(sql, adr)

			

		
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"


		elif duration == 'oneyear':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (e,f)

			resultValue = cur.execute(sql, adr)
			

			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"




		else:
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (fromdate,todate )

			resultValue = cur.execute(sql, adr)


			if resultValue >= 0:
				userDetails = cur.fetchall()

		#print("Total rows are:  ", len(userDetails))

		#print("Printing each row")
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"
			#csv = '7,8,9'
	
	# with open("outputs/Adjacency.csv") as fp:
	#     csv = fp.read()
	
	
	return Response(
		csv,
		mimetype="text/csv",
		headers={"Content-disposition":
				"inline; filename=myplot.csv"})






@app.route("/demo",methods=['GET','POST'])
def demo():
	if request.method == 'POST':
		# Fetch form data
		user = request.form
		print(user)
		fromdate= user['fromdate']
		todate = user['todate']
	
	return render_template("report/report.html",var1=var1)

@app.route("/result",methods=['GET','POST'])
def result():
	fromdate =''
	todate = ''
	service = ''
	duration =''
	result = ''
	userDetails = ''
	from datetime import datetime, timedelta

	sub = datetime.today() - timedelta(days=90)

	print(sub)

	import datetime
	dt = datetime.datetime.today()
	month = f'{dt.month:02d}'
	print(month)
	print(type(month))
	year = dt.year
	print(year)
	dtt = int(month) - 1
	print (dtt)
	a = 1
	d = dt.year
	print(d)
	lastyear = d - 1
	print(lastyear)

	e = str(lastyear)+ "-" +str('01')+ "-" +str('01')
	print(e)
	f = str(lastyear)+ "-" +str('12')+ "-" +str('31')
	print(f)

	#fromdated = str(year)+ "-" +str(dtt)+ "-" +str('01')
	#print(fromdated)
	#todated = str(year)+ "-" +str(dtt)+ "-" +str('31')
	#print(todated)
	a_date = datetime.date(year, dtt, 31)
	print(a_date)
	days = datetime.timedelta(90)
	new_date = a_date - days
	example = datetime.datetime.strptime(str(new_date), "%Y-%m-%d")

	print(example.year)
	print(example.month)
	h = str(example.year)+ "-" +str(example.month)+ "-" +str('01')#valueof quarter year in hardcode
	print(h)
	print(new_date)
	

	
	halfyear = datetime.timedelta(180)
	newdated = a_date - halfyear
	print(newdated)
	newexample = datetime.datetime.strptime(str(newdated), "%Y-%m-%d")
	print(newexample.year)
	print(newexample.month)
	y = str(newexample.year)+ "-" +str(newexample.month)+ "-" +str('01')#half yearly variable
	print(y)

	one = datetime.timedelta(30)
	print(one)
	newone = a_date - one
	print(newone)
	#print(a_date)
	newonemonth = datetime.datetime.strptime(str(newone), "%Y-%m-%d")
	print(newone.year)
	print(newone.month)
	fromdated = str(newonemonth.year)+ "-" +str(newonemonth.month)+ "-" +str('01')#onemonthvariable
	print(fromdated)






	if request.method == 'POST':
		# Fetch form data
		result = request.form
		fromdate= result['fromdate']
		print(fromdate)
		todate = result['todate']
		
		service = result['service']
		duration = result['duration']
	
		print(result)
	csv = ' '
	cur = mysql.connection.cursor()

	



	#resultValue = cur.execute("SELECT * from purchase where dated >= %s and dated <= %s")
	if service == 'purchase':
		if duration == 'onemonth':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (fromdated,a_date)

			resultValue = cur.execute(sql, adr)

			

			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'quarter':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 90 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (h,a_date)

			resultValue = cur.execute(sql, adr)


			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'half':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 180 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (y,a_date)

			resultValue = cur.execute(sql, adr)

			
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'oneyear':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  purchase WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (e,f)

			resultValue = cur.execute(sql, adr)
			
			

			
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"




		elif duration == 'custom':
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (fromdate,todate )

			resultValue = cur.execute(sql, adr)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"


	
	


 


	if service =='invoice':
		if duration == 'onemonth':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW();"
			
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			sql = "select * from purchase where dated >= %s and dated <= %s"
			adr = (fromdated,a_date)

			resultValue = cur.execute(sql, adr)

			

			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'quarter':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 90 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (h,a_date)

			resultValue = cur.execute(sql, adr)

			

			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"

		elif duration == 'half':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 180 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (y,a_date)

			resultValue = cur.execute(sql, adr)

			

		
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"


		elif duration == 'oneyear':
			#sql = "SELECT DATE_FORMAT(dated, '%m/%d/%Y')FROM    purchase WHERE   dated BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();"
			#sql = "SELECT * FROM  invoiced WHERE dated BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW();"
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (e,f)

			resultValue = cur.execute(sql, adr)
			

			#resultValue = cur.execute(sql)
			if resultValue >= 0:
				userDetails = cur.fetchall()
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"




		elif duration == 'custom':
			sql = "select * from invoiced where dated >= %s and dated <= %s"
			adr = (fromdate,todate )

			resultValue = cur.execute(sql, adr)


			if resultValue >= 0:
				userDetails = cur.fetchall()

		#print("Total rows are:  ", len(userDetails))

		#print("Printing each row")
			for row in userDetails:
				csv += str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+ ","+str(row[5])+ ","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+ ","+str(row[10])+","+str(row[11])+","+str(row[12])+"\n"
			#csv = '7,8,9'
	
	# with open("outputs/Adjacency.csv") as fp:
	#     csv = fp.read()
	if 'email' not in session:
		return redirect('http://'+login_url)
	
	return render_template('report/result.html',var1 = var1,userDetails = userDetails)


@app.route("/valid")
def valid():
	
	return render_template('report/valid.html',var1=var1)

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







