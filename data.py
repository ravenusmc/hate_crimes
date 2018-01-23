#This file will hold all of the work for the CSV file. 
import csv
import numpy as np
import pandas as pd


#This class will handle all of the data manipulation
class Data():

    def __init__(self):
        self.data = pd.read_csv('data.csv')

    def test(self):
        print(self.data)



""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  


 """



data = Data()
data.test()

