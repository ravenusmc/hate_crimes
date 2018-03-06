#This file will contain the code for scraping the FBI website to get stats on hate crimes 
#by year. 

#Importing libraries that will be used in this project. 
from bs4 import BeautifulSoup
from csv import writer
import requests 

#This class will take care of all of the scraping that I do. 
class Scraping():

    #Setting up for all of the sites that I'll scrape
    def __init__(self):
        self.requests_list = ["https://ucr.fbi.gov/hate-crime/2010/tables/table-1-incidents-offenses-victims-and-known-offenders-by-bias-motivation-2010.xls",
        "https://ucr.fbi.gov/hate-crime/2011/tables/table-1", "https://ucr.fbi.gov/hate-crime/2012/tables-and-data-declarations/1tabledatadecpdf/table_1_incidents_offenses_victims_and_known_offenders_by_bias_motivation_2012.xls",
        "https://ucr.fbi.gov/hate-crime/2013/tables/1tabledatadecpdf/table_1_incidents_offenses_victims_and_known_offenders_by_bias_motivation_2013.xls",
        "https://ucr.fbi.gov/hate-crime/2014/tables/table-1", "https://ucr.fbi.gov/hate-crime/2015/tables-and-data-declarations/1tabledatadecpdf",
        "https://ucr.fbi.gov/hate-crime/2016/tables/table-1"]

    #This method will set up the initial url 
    def setup_soup(self, count):
        self.response = requests.get(self.requests_list[count])
        #setting up beautiful soup.
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    #This method will push the data into the csv file 
    def push_into_csv(self):
        #opening up the csv file that I'll write to
        with open("blog_data.csv", "w") as csv_file:
            cell_list = ['cell71', 'cell81', 'cell121', 'cell131', 'cell141','cell151', 'cell171',
            'cell161', 'cell171', 'cell201']
            #The year will change per page so I need to ensure that each page has the correct
            #year
            year_list = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
            #Creating a csv variable 
            csv_writer = writer(csv_file)
            #This line will write the rows to the CSV file, the header rows. 
            csv_writer.writerow(["year", "total", "black", "jewish", "islamic"])

            count = 0
            while count < len(year_list):
                self.setup_soup(count)
                year = self.soup.find('a', {'href': 'https://ucr.fbi.gov/hate-crime/' + year_list[count] }).get_text()
                if count == 0:
                    black = self.soup.find(id=cell_list[0]).contents[0] 
                    #converting from the weird beautiful soup data type to an integer. 
                    #I have to do this for each of the different variables that I've declared.
                    black = self.get_number(black)
                    jewish = self.soup.find(id=cell_list[2]).get_text()
                    jewish = self.get_number(jewish)
                    islamic = self.soup.find(id=cell_list[5]).get_text()
                    islamic = self.get_number(islamic)
                    total = black + jewish + islamic
                    csv_writer.writerow([year, total, black, jewish, islamic])
                elif count == 1 or count == 2:
                    black = self.soup.find(id=cell_list[1]).contents[0] 
                    #converting from the weird beautiful soup data type to an integer. 
                    black = self.get_number(black)
                    jewish = self.soup.find(id=cell_list[3]).get_text()
                    jewish = self.get_number(jewish)
                    islamic = self.soup.find(id=cell_list[7]).get_text()
                    islamic = self.get_number(islamic)
                    total = black + jewish + islamic
                    csv_writer.writerow([year, total, black, jewish, islamic])
                elif count == 3 or count == 4:
                    black = self.soup.find(id=cell_list[1]).contents[0] 
                    #converting from the weird beautiful soup data type to an integer. 
                    black = self.get_number(black)
                    jewish = self.soup.find(id=cell_list[4]).get_text()
                    jewish = self.get_number(jewish)
                    islamic = self.soup.find(id=cell_list[6]).get_text()
                    islamic = self.get_number(islamic)
                    total = black + jewish + islamic
                    csv_writer.writerow([year, total, black, jewish, islamic])
                elif count == 5 or count == 6:
                    black = self.soup.find(id=cell_list[1]).contents[0] 
                    #converting from the weird beautiful soup data type to an integer. 
                    black = self.get_number(black)
                    jewish = self.soup.find(id=cell_list[6]).get_text()
                    jewish = self.get_number(jewish)
                    islamic = self.soup.find(id=cell_list[9]).get_text()
                    islamic = self.get_number(islamic)
                    total = black + jewish + islamic
                    csv_writer.writerow([year, total, black, jewish, islamic])
                count += 1

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
     

# test = Scraping()
# test.setup_soup(count)
# test.push_into_csv()