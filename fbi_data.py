#This file will contain the code to make the graphs based on the data that I web scraped from 
#the FBI hate crimes web pages. Please see the file, scrape.py, in the scraping folder to see 
#the code for how I did this. 

#importing libraries that I will use with this project
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import ColumnDataSource, figure, output_file, show
import pandas as pd

class BuildGraphs():

    def build_chart(self):

        #Creating the output file
        output_file("fbi.html")

        #loading the csv to the file 
        file = 'fbi_data.csv'
        #Reading and then storing the csv file as a variable. 
        data = pd.read_csv(file)
        #Turning the data into a ColumnDataSource 
        fbi_data = ColumnDataSource(data)


        p = figure(plot_width=400, plot_height=400, tools='pan,wheel_zoom,box_zoom,reset,hover,save',)
        p.line(x='year', y='black', line_width=2, source=fbi_data)

        #setting up the hover features. 
        hover = p.select_one(HoverTool)
        hover.tooltips = [('Year', '@year'),
        ('Total Hate Crimes Against Blacks', '@black')]

        #excuting the code to create the graph
        show(p)

test = BuildGraphs()
test.build_chart()

