from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#login library
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '52e943135217b09a69608306d2fa4865'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#initializing login manager and functioanlity added in models to validate login
login_manager = LoginManager(app)

from flaskblog import routes

#how to generate secret key
#import secrets
#secrets.token_hex(16)
#output: '52e943135217b09a69608306d2fa4865'

