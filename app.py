from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
