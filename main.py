
#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
import requests

#importing files that I made for the project 
from user import *
from db import *

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/')
def landing():
    return render_template('landing.html')

#This route will take the user to the login page
@app.route('/login')
def login():
    return render_template('login.html')

#This route will take the user to sign up page
@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Pulling data from the form on the signup page
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        #creating the db object to interact with the db. 
        db = Connection()
        #Encrypting the password
        password, hashed = db.encrypt_pass(password)
        #creating user object 
        user = User(username, email, password, hashed)
        #Adding the user to the database
        db.insert(user)

        return redirect(url_for('login'))
    return render_template('signup.html')

#This route will take the user to the home page, once they sign in
@app.route('/home')
def home():
    return render_template('home.html')

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)