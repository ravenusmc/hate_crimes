#This file will hold all of the work for the CSV file. 
import csv
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import scatterChart
import pandas as pd

import random


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
        #setting up a counter
        i = 0
        #This arrays will hold the data 
        trump = []
        income = []
        state = []
        #Pulling the data from the csv file
        trump_data = self.data['share_voters_voted_trump']
        income_data = self.data['median_household_income']
        state_data = self.data['state']
        #I then have to loop through both data sets from the csv file 
        #It will loop through the data sets while the len is less than one of the data 
        #sets-only need to use one since they are both the same length. 
        while i < len(trump_data):
            trump.append(float(trump_data[i]))
            income.append(float(income_data[i]))
            state.append(state_data[i])
            #incrementing the counter by one 
            i += 1

        #creating the temporary HTML file that i'll use    
        output_file = open('test_scatterChart.html', 'w')
        type = "scatterChart"
        #setting up the chart size
        chart = scatterChart(name=type, height=350, width=800, x_is_date=False)
        chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
    
        xdata = income
        ydata = trump

        kwargs1 = {'shape': 'circle', 'size': '1', }

        extra_serie = {"tooltip": {"y_start": "Mike ", "y_end": "" }}
        chart.add_serie(name="State", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  

"""



data = Data()
data.scatter()

