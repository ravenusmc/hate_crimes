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

    #This method will get the mean values for all of the columns. 
    def mean(self):
        #This list will hold all of the mean values that I'll be using for this project 
        column_names = ['median_household_income', 'share_unemployed_seasonal','share_population_in_metro_areas',
        'share_population_with_high_school_degree','share_non_citizen','share_white_poverty','gini_index',
        'share_non_white', 'avg_hatecrimes_per_100k_fbi' ]
        #To display nice names on the data.html page, I have this list with the strings formatted the 
        #way that I want. 
        fixed_column_names = ['Median Household Income', 'Share Unemployed Seasonal','Share Population in Metro Areas',
        'Share Population With High School Degree','Share Non Citizen','Share White Poverty','Gini Index',
        'Share Non White', 'Avg Hate Crimes / 100k By FBI' ]
        #This is the dictionary that will hold all of the data
        mean_dict = {}
        #A count for the below while loop
        count = 0
        #This while loop will loop through the mean for each column and pair it up with the column 
        #name. 
        while count < len(column_names):
            # Here I am getting the mean for each column as I loop through it 
            data = self.data[column_names[count]].mean()
            # Formatting the values for only two decimal places
            data = format(data, '5.2f')
            # Placing the column name, the key and its corresponding value, into the dict. 
            mean_dict[fixed_column_names[count]] = data
            #Incrementing the count by one
            count += 1
        #Returning the dict. 
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

    #This method will get me the standard deviation of a column 
    def standard_deviation(self):
        test = self.data['median_household_income'].std()
        print(test)





""" Things to look at:

    1. Average of median_household_income 
    2. Average of share_white_poverty
    3. Average of gini_index
    4. Average of hate_crimes / FBI  

"""



data = Data()
data.standard_deviation()
# data.mean()
# data.correlation()

