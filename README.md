# cs105-prj-phase1-climatechangeisreal
cs105-prj-phase1-climatechangeisreal created by GitHub Classroom

Hazel Nguyen: 862054134

Itzel Gonzalez: 861304050

# Datasets

Sentiment of Climate Change
https://data.world/crowdflower/sentiment-of-climate-change


We will obtain this data set by downloading 
Sentiment Analysis – Global Warming/Climate Change
https://www.figure-eight.com/data-for-everyone/


We will obtain this data set by downloading 
Use Twitter API to use their data and compile tweets
https://developer.twitter.com/en/docs


We will use the twitter API to find data on only Riverside tweets about climate change
Geo - Place information of a tweet
https://developer.twitter.com/en/docs/geo/place-information/overview


We will obtain information through  API download
Riverside/Inland Empire Area Climate Data
https://data.countyofriverside.us

# Scrapy Web Crawler

`<pip install Scrapy>`

We will use Scrapy to crawl through our datasets. Included in our code is an example from lab to scrape through a dataset.
We are going to scrape quotes.toscrape.com, a website that lists quotes from famous authors. 
We are going to scrape twitter.com, a website that has a dataset of tweets to scrape for "climate" change.


Web Crawler - bot browses, web indexes, and locates web-pages
vs.
Web Scraper - scrapes/extracts content of interest from given page

Crawler Operation
Begin with “seed” URLS
Fetch/parse them
Extract URLs they point to
Check if URL content has already been seen
If not, Place URLs on a queue
Fetch each URL on the queue. Repeat

Using Scrapy
We set up a scrap project under a directory called webScraper
scrapy startproject webScraper

We then create a Spider class that will extract data by following links in the initial requested page, then it will parse the downloaded page content.

Code for first Spider: 

import scrapy

class DataSpider(scrapy.Spider):
    name = “climate_data”

    def start_requests(self):
        urls = [
            'https://data.countyofriverside.us <https://data.countyofriverside.us/>/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = ‘data-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)






