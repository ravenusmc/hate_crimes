
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Recieving the information from the user.
        username = request.form['username']
        password = request.form['password']
        #creating the db connection object
        db = Connection()
        #Checking to see if the user is in the database.
        flag, not_found, password_no_match = db.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('home'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            if not_found:
                flash('Username not found, maybe sign up!')
            elif password_no_match:
                flash('Password does not match! Maybe sign up!')
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
        #Once the information is added to the db, the user is redirected to login page. 
        return redirect(url_for('login'))
    return render_template('signup.html')

#This route will take the user to the home page, once they sign in
@app.route('/home')
def home():
    allowed_in = True 
    return render_template('home.html', allowed_in = allowed_in)

#This route will sign out the user 
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    #Redirect to Landing page
    return redirect(url_for('landing'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)