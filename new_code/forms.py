from flask_wtf import FlaskForm
from wtforms import StringField,TextField,SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired,Length,Email

class RegistrationForm(FlaskForm):
	name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('email',validators=[DataRequired(), Email()])
	
	password = StringField('password', validators=[DataRequired()])
	submit=SubmitField('Add')

class AccountForm(FlaskForm):
	name=StringField('Vendor Name',
		validators=[DataRequired(), Length(min =2, max=20)])
	address=StringField('Address',
		validators=[DataRequired(), Length(min =2, max=20)])
	email=StringField('Email',
		validators=[DataRequired(), Email()])
	gstin=StringField('GSTIN',
		validators=[DataRequired(), Length(min =2, max=15)])
	pan=StringField('PAN',
		validators=[DataRequired(), Length(min=2, max=10)])
	submit=SubmitField('Add')


class TrainerForm(FlaskForm):
	name=StringField('name',
		validators=[DataRequired(), Length(min =2, max=20)])
	trainertype=RadioField('trainertype', coerce=str,
		choices=[('value','Internal'),('value_two','External')])
	status=StringField('status',
		validators=[DataRequired(), Length(min=2 , max=20)])
	gstin=StringField('gstin',
		validators=[DataRequired(), Length(min =2, max=15)])
	pan=StringField('pan',
		validators=[DataRequired(), Length(min=2, max=10)])
	acc1=StringField('acc1',
		validators=[DataRequired(), Length(min=2, max=40)])
	acc2=StringField('acco2',
		validators=[DataRequired(), Length(min=2, max=30)])
	acc3=StringField('acc3',
		validators=[DataRequired(), Length(min=2, max=40)])
	acc4=StringField('acc4',
		validators=[DataRequired(), Length(min=2, max=40)])
	tech1=StringField('tech1',
		validators=[DataRequired(), Length(min=2, max=60)])
	tech2=StringField('tech2',
		validators=[DataRequired(), Length(min=2, max=60)])
	tech3=StringField('tech3',
		validators=[DataRequired(), Length(min=2, max=60)])
	submit=SubmitField('Add')
	
class InvoiceForm(FlaskForm):
  name=StringField('name',validators=[DataRequired(), Length(min =2,max=20)])
  ad=StringField('ad',validators=[DataRequired(), Length(min =2,max=20)])
  gst=StringField('GST',validators=[DataRequired()])
  pan=StringField('PAN',validators=[DataRequired()])
  train=StringField('train',validators=[DataRequired()])
  num=IntegerField('num',validators=[DataRequired()])
  dated=IntegerField('dated',validators=[DataRequired()])
  #unitcost=IntegerField('unitcost',validators=[DataRequired()])
  #qty=IntegerField('qty',validators=[DataRequired()])
  #pric=IntegerField('pric',validators=[DataRequired()])
  item=StringField('item',validators=[DataRequired()])
  description=StringField('description',validators=[DataRequired()])
  total=IntegerField('total',validators=[DataRequired()])
  #subtotal=IntegerField('subtotal',validators=[DataRequired()])
  subtotal=IntegerField('subtotal',validators=[DataRequired()])
  words=StringField('balance',validators=[DataRequired()])
  
  submit=SubmitField('Add')


class RecieveForm(FlaskForm):
  name=StringField('name',validators=[DataRequired(), Length(min =2,max=20)])
  ad=StringField('ad',validators=[DataRequired(), Length(min =2,max=20)])
  gst=StringField('GST',validators=[DataRequired()])
  pan=StringField('PAN',validators=[DataRequired()])
  file=StringField('file',validators=[DataRequired()])
  num=IntegerField('Num',validators=[DataRequired()])
  dated=IntegerField('dated',validators=[DataRequired()])
  #unitcost=IntegerField('unitcost',validators=[DataRequired()])
  #qty=IntegerField('qty',validators=[DataRequired()])
  #pric=IntegerField('pric',validators=[DataRequired()])
  item=StringField('item',validators=[DataRequired()])
  description=StringField('description',validators=[DataRequired()])
  total=IntegerField('total',validators=[DataRequired()])
  #subtotal=IntegerField('subtotal',validators=[DataRequired()])
  subtotal=IntegerField('subtotal',validators=[DataRequired()])
  words=StringField('balance',validators=[DataRequired()])
  
  submit=SubmitField('Add')
  
class UpdateForm(FlaskForm):
  name=StringField('name',validators=[DataRequired(), Length(min =2,max=20)])
  email=StringField('email',validators=[DataRequired(), Length(min =2,max=20)])
  status=StringField('status',validators=[DataRequired()])
  
  submit=SubmitField('Add')

class BillForm(FlaskForm):
  name=StringField('name',validators=[DataRequired(), Length(min =2,max=20)])
  description=StringField('description',validators=[DataRequired()])
  file=StringField('file',validators=[DataRequired()])
  dated=IntegerField('dated',validators=[DataRequired()])
  amount=IntegerField('Num',validators=[DataRequired()])
  
  submit=SubmitField('Add')	

