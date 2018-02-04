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
        #self.data = pd.read_csv('data.csv')
        self.data = pd.read_csv('hate_crimes.csv')

    def test(self):
        print(self.data)

    def mean(self):
        print(self.data['median_household_income'].mean())

    #This method will return a list of correlations. Since, I don't have everything planned out 
    #That I want to look at, I'll find the correlations as I go and add them to the list. 
    def correlation(self):
        #Creating the list that will hold all of the values
        correlation_list = []
        #Getting the values and then appending them to the list
        correlation_list.append(self.data['median_household_income'].corr(self.data['share_voters_voted_trump']))
        correlation_list.append(self.data['share_population_in_metro_areas'].corr(self.data['share_voters_voted_trump']))
        correlation_list.append(self.data['share_white_poverty'].corr(self.data['avg_hatecrimes_per_100k_fbi']))
        correlation_list.append(self.data['black_poverty'].corr(self.data['avg_hatecrimes_per_100k_fbi']))
        #Returning the list 
        return correlation_list


""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  

"""



# data = Data()
# data.test()
#data.correlation()

