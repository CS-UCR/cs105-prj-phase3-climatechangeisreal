import scrapy
import time
  

class ClimateSpider(scrapy.Spider):
    name = "climates"
    start_urls = ['https://en.wikipedia.org/wiki/List_of_weather_records' ,]

    

    def parse(self, response):
        body = response.css('tr')
        Countries = []
        Temperatures = []
        Locations = []
        Dates = []
        for column in body:
            values = column.css('td')
            if(len(values) == 4):
                Countries.append(values[0].css('a').getall())
                Temperatures.append(values[1].css('td').getall())
                Locations.append(values[2].css('a').getall())
                Dates.append(values[3].css('span').getall())
        for x in range(0, len(Countries)):
            yield{
                'Country' : Countries[x],
                'Temperature' : Temperatures[x],
                'Location' : Locations[x],
                'Date' : Dates[x]
            }

                
           