#This file will contain the code for scraping the FBI website to get stats on hate crimes 
#by year. 

#Importing libraries that will be used in this project. 
from bs4 import BeautifulSoup
from csv import writer
import requests 

#This class will take care of all of the scraping that I do. 
class Scraping():

    def __init__(self):
        self.requests_list = ["https://ucr.fbi.gov/hate-crime/2010/tables/table-1-incidents-offenses-victims-and-known-offenders-by-bias-motivation-2010.xls",
        "https://ucr.fbi.gov/hate-crime/2011/tables/table-1", "https://ucr.fbi.gov/hate-crime/2012/tables-and-data-declarations/1tabledatadecpdf/table_1_incidents_offenses_victims_and_known_offenders_by_bias_motivation_2012.xls",
        "https://ucr.fbi.gov/hate-crime/2013/tables/1tabledatadecpdf/table_1_incidents_offenses_victims_and_known_offenders_by_bias_motivation_2013.xls",
        "https://ucr.fbi.gov/hate-crime/2014/tables/table-1", "https://ucr.fbi.gov/hate-crime/2015/tables-and-data-declarations/1tabledatadecpdf",
        ]
        self.response = requests.get(self.requests_list[0])

    #This method will set up the initial url 
    def setup_soup(self):
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        # self.tables = self.soup.find("table")

    #This method will push the data into the csv file 
    def push_into_csv(self):
        with open("blog_data.csv", "w") as csv_file:
            csv_writer = writer(csv_file)
            #csv_writer.writerow(["year", "total", "anti-black", "anti-jewish", "anti-islamic"])
            # year = 
            # total = 
            black = self.soup.find(id="cell71").get_text()
            jewish = self.soup.find(id="cell121").get_text()
            islamic = self.soup.find(id="cell151").get_text()
            print(black)
            #csv_writer.writerow([year, total, black, jewish, islamic])

            # for table in tables:



    # a_tag = article.find("a")
    # title = a_tag.get_text()
    # url = a_tag["href"]
    # date = article.find("time")["datetime"]
    # csv_writer.writerow([title, url, date])        




test = Scraping()
test.setup_soup()
test.push_into_csv()