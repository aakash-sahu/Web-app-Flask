from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user

posts =[
	{
		'author': 'Aakash Sahu',
		'title': 'First blog post',
		'content': 'First post content using Flask',
		'date': '17th July 2018'
	},
	{
		'author': 'John Doe',
		'title': 'Another blog post',
		'content': 'Second post content using Flask',
		'date': '18th July 2018'
	}	
	]

@app.route("/")
@app.route("/home")
def Home():
	return render_template('home.html', posts = posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET','POST']) #add methods for sign up button
def register():
		form = RegistrationForm()
		if form.validate_on_submit():
			hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user = User(username = form.username.data, email = form.email.data, password = hashed_password)
			db.session.add(user)
			db.session.commit()
			flash(f'Account created for {form.username.data}! You are now able to log in', 'success')
			#flash(f'Account created for {form.username.data}!', 'success')
			#return redirect(url_for('Home')) #uses function name
			return redirect(url_for('login'))
		return render_template('register.html', title = 'Register', form = form)

"""
remove hardcoded validation on submit
"""		
@app.route("/login", methods = ['GET','POST'])
def login():
		form = LoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(email = form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user, remember = form.remember.data)
				redirect(url_for('home'))
			# if form.email.data == 'admin@blog.com' and form.password.data == 'password':
				# flash('You have been logged in!', 'success')
				# return redirect(url_for('Home'))
			else:
				flash('Login unsuccessful. Please check email and password','danger')
		return render_template('login.html', title = 'Login', form = form)		
