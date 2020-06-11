from flask import Flask,render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__) 
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URL']=os.environ.get("DATABASE_URL")

@app.route("/") 
def home_view(): 
		return "<h1>Sudhanshu</h1>"

@app.route("/new")
def new():
	return render_template("new.html")