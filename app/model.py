from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand



# Database Configurations
app = Flask(__name__)
DATABASE = 'newtest'
PASSWORD = 'p@ssw0rd123'
USER = 'root'
HOSTNAME = 'mysqlserver'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):

	# Data Model User Table
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=False)
	email = db.Column(db.String(120), unique=True)
	phone = db.Column(db.String(120), unique=True)
	fax = db.Column(db.String(120), unique=False)

	def __init__(self, username, email, phone, fax):
		# initialize columns
		self.username = username
		self.email = email
		self.phone = phone
		self.fax = fax

	def __repr__(self):
		return '<User %r>' % self.username


class Author(db.Model):
	__tablename__ = 'authors'

	# Data Model Author Table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), unique=True)
	user_id = db.Column(db.Integer, unique=False)

	def __init__(self, name, user_id):
		# initialize columns
		self.name = name
		self.user_id = euser_idmail

	def __repr__(self):
		return '<Author %r>' % self.name

class Keyword(db.Model):
	__tablename__ = 'keywords'

	# Data Model Keyword Table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), unique=True)

	def __init__(self, name):
		# initialize columns
		self.name = name

	def __repr__(self):
		return '<Keyword %r>' % self.name

class Monograph(db.Model):
	__tablename__ = 'monographs'

	# Data Model Monograph Table
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, unique=True)
	abstract = db.Column(db.Text, unique=False)
	future = db.Column(db.Text, unique=False)
	file = db.Column(db.String(255), unique=False)

	def __init__(self, title, abstract, future, file):
		# initialize columns
		self.title = title
		self.abstract = abstract
		self.future = future
		self.file = file

	def __repr__(self):
		return '<Monograph %r>' % self.title

class MonographHasAuthor(db.Model):
	__tablename__ = 'monographs_has_authors'

	# Data Model Keyword Table
	monograph_id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, primary_key=True)

	def __init__(self, monograph_id, author_id):
		# initialize columns
		self.monograph_id = monograph_id

	def __repr__(self):
		return '<monograph_id %r>' % self.monograph_id

class MonographHasKeyword(db.Model):
	__tablename__ = 'monographs_has_keywords'

	# Data Model Keyword Table
	monograph_id = db.Column(db.Integer, primary_key=True)
	keyword_id = db.Column(db.Integer, primary_key=True)

	def __init__(self, monograph_id):
		# initialize columns
		self.monograph_id = monograph_id
		self.keyword_id = keyword_id

	def __repr__(self):
		return '<monograph_id %r>' % self.monograph_id


class CreateDB():
	def __init__(self, hostname=None):
		if hostname != None:	
			HOSTNAME = hostname
		import sqlalchemy
		engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
		engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db

if __name__ == '__main__':
	manager.run()