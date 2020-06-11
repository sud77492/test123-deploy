from flask import Flask,render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__) 
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URL']=os.environ.get("DATABASE_URL")

# db=SQLAlchemy(app)

# class User(db.Model):
# 	__tablename__='users'

# 	id=db.Column(db.Integer, primary_key=True)
# 	name=db.Column(db.String, primary_key=True)
# 	email=db.Column(db.String, primary_key=True)

# db.init_app()

@app.route("/") 
def home_view(): 
		return "<h1>Sudhanshu</h1>"

@app.route("/new")
def new():
	return render_template("new.html")