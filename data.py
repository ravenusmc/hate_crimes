#This file will hold all of the work for the CSV file. 
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#This class will handle all of the data manipulation
class Data():

    def __init__(self):
        self.data = pd.read_csv('data.csv')

    def test(self):
        print(self.data)

    def mean(self):
        print(self.data['median_household_income'].mean())

    def correlation(self):
        print(self.data.corr())

    def scatter(self):
        colors = (0,0,0)
        area = np.pi*3
        trump = self.data['share_voters_voted_trump']
        income = self.data['median_household_income']
        plt.scatter(income, trump, s=area, c=colors, alpha=0.5)
        plt.title('Trump Voters Vs Income')
        plt.xlabel('Income Level')
        plt.ylabel('Percentage Voting Trump')
        plt.show()




""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  


 """



data = Data()
data.scatter()

