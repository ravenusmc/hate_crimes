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
        "https://ucr.fbi.gov/hate-crime/2016/tables/table-1"]
        # self.response = requests.get(self.requests_list[0])

    #This method will set up the initial url 
    def setup_soup(self):
        self.response = requests.get(self.requests_list[0])
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        # self.tables = self.soup.find("table")

    #This method will push the data into the csv file 
    def push_into_csv(self):
        #opening up the csv file that I'll write to
        with open("blog_data.csv", "w") as csv_file:
            #Creating a csv variable 
            csv_writer = writer(csv_file)
            #This line will write the rows to the CSV file, the header rows. 
            csv_writer.writerow(["year", "total", "anti-black", "anti-jewish", "anti-islamic"])
            year = self.soup.find('a', {'href': 'https://ucr.fbi.gov/hate-crime/2010'}).get_text()
            black = self.soup.find(id="cell71").contents[0]
            #converting from the weird beautiful soup data type to an integer. 
            black = self.get_number(black)
            jewish = self.soup.find(id="cell121").get_text()
            jewish = self.get_number(jewish)
            islamic = self.soup.find(id="cell151").get_text()
            islamic = self.get_number(islamic)
            total = black + jewish + islamic
            csv_writer.writerow([year, total, black, jewish, islamic])



    #This method will get the numbers from the content of the web scraping. 
    #I was returning a blank line each time I scraped and needed to get rid of that blank 
    #line so I created this method. 
    def get_number(self, data):
        #Setting a counter. I start it at 1 because my black space is at zero in the 
        #data argument. 
        count = 1
        #A list to hold each number 
        num_list = []
        #A while loop that will loop through the data variable and push each number into the 
        #list
        while count < len(data):
            if data[count] != ',':
                num_list.append(data[count])
            count += 1
        #rejoing the list into an array. By calling int, I'm ensuring that each number is 
        #converted from a string to an integer. 
        crime_number = int(''.join(num_list))
        #returning the integer. 
        return crime_number




    # a_tag = article.find("a")
    # title = a_tag.get_text()
    # url = a_tag["href"]
    # date = article.find("time")["datetime"]
    # csv_writer.writerow([title, url, date])        




test = Scraping()
test.setup_soup()
test.push_into_csv()