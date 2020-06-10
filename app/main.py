from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return "<h1>Sudhanshu</h1>"

