from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#each class will be a table in database
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(120), unique = True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable = False)
	posts = db.relationship('Post', backref = 'author', lazy = True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title =  db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content =  db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	
	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"
		
#from sqlalchemy_1 import db
# from sqlalchemy_1 import User, Post
# db.drop_all()
# db.create_all()	
# user_1 = User(username = 'John', email = 'john@email.com', password = 'password')
# db.session.add(user_1)
# user_2 = User(username = 'Jane', email = 'jane@email.com', password = 'password')
# db.session.add(user_2)
# db.session.commit()
# User.query.all()
# User.query.first()
# User.query.filter_by(username = 'John').all()
# user = User.query.filter_by(username = 'John').first()

# user
# user.id
# user = user.query.get(1)
# user

# user.posts
# user.id
# post_1 = Post(title = 'Blog 1', content = 'First blog content', user_id = user.id)
# post_2 = Post(title = 'Blog 2', content = 'Second blog content', user_id = user.id)

# db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()
# user.posts

# for post in user.posts:
	# print(post.title)

# post = Post.query.first()
# post
# post.user_id
# post.author

# db.drop_all()
# db.create_all()
# User.query.all()
# Post.query.all()	

if __name__ == '__main__':
	app.run(debug=True)		