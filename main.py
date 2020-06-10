from flask import Flask,render_template,request, url_for

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return "<h1>Sudhanshu</h1>"

@app.route("/new")
def new():
	return render_template("new.html")
