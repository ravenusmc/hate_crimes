#This file will contain the code for scraping the FBI website to get stats on hate crimes 
#by year. 

#Importing libraries that will be used in this project. 
from bs4 import BeautifulSoup
from csv import writer
import requests 

#This class will take care of all of the scraping that I do. 
class Scraping():

    def __init__(self):
        self.response = requests.get("https://ucr.fbi.gov/hate-crime/2010/tables/table-1-incidents-offenses-victims-and-known-offenders-by-bias-motivation-2010.xls")


    def setup_soup(self):
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        print(self.soup)



test = Scraping()
test.setup_soup()