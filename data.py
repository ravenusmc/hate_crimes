#This file will hold all of the work for the CSV file. 
from bokeh.charts import Scatter, output_file, show
from bokeh.plotting import figure, output_file, show
import csv
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import scatterChart
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




""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  

"""



data = Data()
#data.scatter()
data.bokeh()

