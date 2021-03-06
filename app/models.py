from flask.ext.login import UserMixin
from . import login_manager
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Role(db.Model):
	__tablename__='roles'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)

class User(db.Model,UserMixin):
	__tablename__='users'

	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	name = db.Column(db.String(64))
	location = db.Column(db.String(64))
	about_me = db.Column(db.Text())
	member_since = db.Column(db.DateTime(), default=datetime.utcnow)
	last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
	
	def ping(self):
		self.last_seen = datetime.utcnow()
		db.session.add(self)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))