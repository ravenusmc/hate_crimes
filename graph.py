#This file will handle the making of all of the graphs for the web app. 

#Importing libraries for use in this file
from bokeh.charts import Bar, Scatter, output_file, show
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
import csv
import matplotlib.pyplot as plt
import numpy as np
from nvd3 import scatterChart
import pandas as pd


class Graph():

    def test(self):
        #Creatin an output file 
        output_file("test.html")

        #loading the csv to the file 
        file = 'data.csv'
        #Reading and then storing the csv file as a variable. 
        data = pd.read_csv(file)
        #Turning the data into a ColumnDataSource 
        hate_crime_data = ColumnDataSource(data) 

        plot = figure(x_axis_label='Population Percentage in Metro Area', y_axis_label='percentage who voted for Trump',
            plot_width=600, plot_height=500, tools='pan,wheel_zoom,box_zoom,reset,hover,save', 
            title='Trump Voters VS. Percentage Living in Metro Area')

        plot.circle(x='share_population_in_metro_areas', y='share_voters_voted_trump', source=hate_crime_data, 
            size=15)

        hover = plot.select_one(HoverTool)
        hover.tooltips = [('state', '@state'),
        ('Pop. In Metro Area', '@share_population_in_metro_areas'),
        ('Percentage Voted Trump', '@share_voters_voted_trump ')]

        show(plot)

    #This method will generate the graph with the states color coded by who won them-Clinton or Trump
    def generate_bokeh_new_graph(self):
        #Creating an output file 
        output_file("graph.html")

        #loading the csv to the file 
        file = 'hate_crimes.csv'
        #Reading and then storing the csv file as a variable. 
        data = pd.read_csv(file)
        #Turning the data into a ColumnDataSource 
        hate_crime_data = ColumnDataSource(data)

        #This line will be what sets up a color code between which states voted for clinton or trump.
        color_mapper = CategoricalColorMapper(factors=['Trump', 'Clinton'], 
        palette=['red', 'blue']) 

        plot = figure(x_axis_label='Population Percentage in Metro Area', y_axis_label='percentage who voted for Trump',
            plot_width=600, plot_height=500, tools='pan,wheel_zoom,box_zoom,reset,hover,save', 
            title='Trump Voters VS. Percentage Living in Metro Area')

        plot.circle(x='share_population_in_metro_areas', y='share_voters_voted_trump', source=hate_crime_data, 
            size=15, color=dict(field='won_state', transform=color_mapper))

        # plot.circle(x='median_household_income', y='share_voters_voted_trump', source=hate_crime_data, 
        #     size=15, color=dict(field='won_state', transform=color_mapper))

        hover = plot.select_one(HoverTool)
        hover.tooltips = [('state', '@state'),
        ('Pop. In Metro Area', '@share_population_in_metro_areas'),
        ('Percentage Voted Trump', '@share_voters_voted_trump ')]

        show(plot)

graph = Graph()
graph.generate_bokeh_new_graph()






######## OLD CODE DOWN HERE --- FOR FUTURE REFERENCE #########

    #This method will use NVD3 to make the scatter plot 
    # def scatter(self):
    #     #setting up a counter
    #     i = 0
    #     #This arrays will hold the data 
    #     trump = []
    #     income = []
    #     state = []
    #     #Pulling the data from the csv file
    #     trump_data = self.data['share_voters_voted_trump']
    #     income_data = self.data['median_household_income']
    #     state_data = self.data['state']
    #     #I then have to loop through both data sets from the csv file 
    #     #It will loop through the data sets while the len is less than one of the data 
    #     #sets-only need to use one since they are both the same length. 
    #     while i < len(trump_data):
    #         trump.append(float(trump_data[i]))
    #         income.append(float(income_data[i]))
    #         state.append(state_data[i])
    #         #incrementing the counter by one 
    #         i += 1

    #     #creating the temporary HTML file that i'll use    
    #     output_file = open('test_scatterChart.html', 'w')
    #     type = "scatterChart"
    #     #setting up the chart size
    #     chart = scatterChart(name=type, height=350, width=800, x_is_date=False)
    #     chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
    
    #     xdata = income
    #     ydata = trump

    #     kwargs1 = {'shape': 'circle', 'size': '1', }

    #     extra_serie = {"tooltip": False}
    #     chart.add_serie(name="State", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
    #     chart.buildhtml()
    #     output_file.write(chart.htmlcontent)
    #     output_file.close()























