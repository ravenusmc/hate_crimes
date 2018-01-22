#This file will create the user object

class User():

  def __init__(self, username, email, password, hashed):
    self.username = username
    self.email = email
    self.password = password
    self.password_hashed = hashed