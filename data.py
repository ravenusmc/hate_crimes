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

    #This method will get the mean values for all of the columns. 
    def mean(self):
        #This list will hold all of the mean values that I'll be using for this project 
        column_names = ['median_household_income', 'share_unemployed_seasonal','share_population_in_metro_areas',
        'share_population_with_high_school_degree','share_non_citizen','share_white_poverty','gini_index',
        'share_non_white', 'avg_hatecrimes_per_100k_fbi' ]
        mean_dict = {}
        mean_list = []
        number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for name in column_names:
            # Here I am getting the mean for each column as I loop through it 
            data = self.data[name].mean()
            
            # Formatting the values for only two decimal places
            data = format(data, '5.2f')
            # Placing the column name, the key and its corresponding value, into the dict. 
            mean_dict[name] = data
            # mean_dict[num] = number 
            # mean_list.append(mean_dict[name] = data, mean_dict[number[count]] = number)
        return mean_dict

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
        correlation_list.append(self.data['gini_index'].corr(self.data['avg_hatecrimes_per_100k_fbi']))
        correlation_list.append(self.data['share_non_white'].corr(self.data['share_voters_voted_trump']))
        #Returning the list 
        return correlation_list


""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  

"""



data = Data()
data.mean()
# data.correlation()

