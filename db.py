#This file will make the connection to the database

#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector

class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                            password='pass',
                            host='localhost',
                            port=3306,
                            database='hate_crimes')
        self.cursor = self.conn.cursor()

    #This method will encrypt the password
    def encrypt_pass(self, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed

    #This method will insert a new user into the database.
    def insert(self, user):
        self._SQL = """insert into users
          (username, email, password)
          values
          (%s, %s, %s)"""
        self.cursor.execute(self._SQL, (user.username, user.email, user.password_hashed))
        self.conn.commit()

    #This method will check to see if the password is in the database. 
    def check(self, username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        #Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        #Here I check to see if the username is in the database.
        if str(row) == 'None':
            flag = False
            not_found = True
            password_no_match = False
        #If the user name is in the database I move here to check if the password
        #is valid.
        else:
            hashed = row[3].encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                flag = True
                not_found = False
                password_no_match = False
            #This is a final catch all area. Basically if the password does not match 
            #the user is not getting in. 
            else:
                flag = False
                not_found = False
                password_no_match = True
        return flag, not_found, password_no_match