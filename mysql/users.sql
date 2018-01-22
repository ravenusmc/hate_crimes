--The code in this file is the code that was used to set up the database and table for this 
--project
--CREATE DATABASE hate_crime;

--This is the table that I'm using for this project 
CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);