from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def auth():
    return render_template("auth.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/process', methods=["POST"])
def process():
    # validate the form here ...
    # create the hash
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "name":request.form['name'],
        "email": request.form['email'],
        "dob": request.form['dob'],
        "password": hashed_pw
    }
    User.save(data)
    print(data)
    return redirect('/home')

@app.route('/home')
def home():
    return render_template("home.html")


