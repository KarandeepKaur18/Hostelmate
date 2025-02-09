from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student_sign_up():
    return render_template("student_sign_up.html")

@app.route("/admin")
def admin_sign_up():
    return render_template("admin_sign_up.html")

@app.route("/staff")
def staff_sign_up():
    return render_template("staff_sign_up.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
