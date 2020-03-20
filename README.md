# cs105-prj-phase3-climatechangeisreal
cs105-prj-phase3-climatechangeisreal created by GitHub Classroom

Hazel Nguyen: 862054134

Itzel Gonzalez: 861304050

# Datasets

Sentiment of Climate Change

https://data.world/crowdflower/sentiment-of-climate-change
We will obtain this data set by downloading 


Sentiment Analysis – Global Warming/Climate Change

https://www.figure-eight.com/data-for-everyone/
We will obtain this data set by downloading 


Use **Twitter API** to use their data and compile tweets

https://developer.twitter.com/en/docs

Use twitter API to compile tweets about *"climate change" and "corona virus"*

- Find correlation between the two recent events
http://twitter.com/search?q=climate%20change%20coronavirus&src=typeahead_click


We will use scrapy web-crawler to find data on only Riverside tweets about climate change
Geo - Place information 


We will obtain information through  API download
Riverside/Inland Empire Area Climate Data

https://data.countyofriverside.us

# Phase 1

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


Using Scrapy
We set up a scrapy project under a directory called Scraper
`scrapy startproject Scraper`

Go to:
`cd ItzelsScraper/tutorial/`

Type:
`scrapy shell "https://en.wikipedia.org/wiki/List_of_weather_records"`


This command gives you access to an interactive scraper that will help you scrape individual elements of the page
Now you need to find which commands will give you the right data
Using this shell we will find the specific elements that contain our data, 
then we create python script that isolates the data. Found Here: `ItzelsScraper/tutorial/tutorial/spiders/temp_spider.py/`

We use:
`scrapy crawl climates -o climates.csv`

to output csv file with all our data.


# Tweepy

A python library that allows one to obtains tweets from Twitter API. To use this library, you would need a twitter developer account and python in order to install tweepy.

Once we have this, we make a Twitter application that will be used to interface with Python code we will write, and allow us to stream and process live tweets. After creating the Twitter application, we will leverage the "tweepy" module to stream the tweets.

The data gathered from this is all in tweets.txt

`pip install tweepy`

# Phase 2 - EDA 

# Twitter API

From the twitter API, I was able to gather data by making a query that searches for tweets about "climate change" and "corona virus". From the API, I was able to gather tweets. However, there were restrictions to how many tweets I am able to gather per day, so to compile a large set of data, I made gathered 100 tweets per day and per it all into a separate file. From the tweets.txt file, the data compiled is hard to read and have irrelevant data that we did not need. Using EDA cleaning, I narrowed down my dataset and created a dataframe with attributes that I was going to access on: id, username, location, date, and more that is customizable to the fitting. 

# Phase 3

Itzel:

**Hazel** 

In this phase, I assess the data and used what we were able to learn in class such as making visualizations and make predictions using machine learning (linear regression). From the data, I was able to make a time series graph that plot the number of times people talked about climate change and the the corona virus. Using data gathered from three separate days, there was a growth to the amount of people that talked about the virus and climate change. 

Another feature I added is sentiment analysis on the data. A tweet will be given a score ranging from (-1, 0, 1). The ranges corresponds to negative, neutral, and positive. This allows me to make a histogram to show the sentiment data and compare the results. 

**Machine Learning (Make Predictions on Sentiment)**

With the newly added feature about sentiment on the tweets, I am able to make predictions using machine learning. The sklearn library from python allows one to use functions like LinearRegression to train my data and make predictions. The test data I use are tweets that I searched for on a separate day. It is able to predict whether the tweets are negative, neutral, or positive. 

