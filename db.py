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