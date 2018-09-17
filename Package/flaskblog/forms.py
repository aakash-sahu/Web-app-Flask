#Create forms, use fields for different fields, and validators for validation of those fields in runtime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', 
			validators= [DataRequired(), Length(min =2, max = 20)])
	email = StringField('Email',
			validators = [DataRequired(), Email()])
	password = 	PasswordField('Password',
			validators = [DataRequired()])
	confirm_password = 	PasswordField('Confirm Password',
			validators = [DataRequired(), EqualTo('password')])	
	submit = SubmitField('Sign Up')
	
	#adding validation for fields such that to check if username or email already exists
	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different username')
			
	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a another one')		

class LoginForm(FlaskForm):
	email = StringField('Email',
			validators = [DataRequired(), Email()])
	password = 	PasswordField('Password',
			validators = [DataRequired()])
	remember = BooleanField('Remember me')		 #through cookie by setting up secret key in main file
	submit = SubmitField('Log in')	