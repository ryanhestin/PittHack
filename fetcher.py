from bs4 import BeautifulSoup
import twilio.twiml
import requests
import urllib, urllib2
import sys
import wikipedia
import re
from collections import defaultdict
import twitter
MAX_SUMMARY_SIZE = 350

api = twitter.Api(
    consumer_key='Y4ThdncoRUdVTwcItPDrA', 
    consumer_secret='vVbQzGXO1RpN4gh70O2rCyt050vuinvTsb8I9GHyde0', 
    access_token_key='27364715-L0jlYzgZ4SAs4jmX8PU8m4dryOrePirBFaSRwUA0y', 
    access_token_secret='ME4IKOjjoUbHpTWH8v2tQRSFPAQ1b24Xo166afOfb4o3t'
)


def getTweet(query):
    statuses = api.GetUserTimeline(screen_name=query, count=1)
    s = statuses[0];
    return s.text;



def getPage(query, lang='en'):
    wikipedia.set_lang(lang)

    content = "Query not found! We're sorry, try a different one! :("



    searchObj = re.search( r'-\d+$', query, re.M|re.I)

    if searchObj: #if the page number is inside query
        #print ("found")
        page_num = searchObj.group()[1:] #gets the number of page without the dash
        real_query = query[0: len(query)-len(searchObj.group())]
        print(real_query)
        print(page_num)
        try:
            page = wikipedia.page(real_query)
            pageContent = page.content
            #print(pageContent)

            sentence_arr = pageContent.split(". ")

            start = int(page_num)+1
            stop =  start +2
            content = ""
            for x in range (start, stop):
                #print sentence_arr[x]
                content = content + sentence_arr[x] +". " # this is the returned result
        except:
            pass

    else: #page number not inside query
        try:
            page = wikipedia.page(query)
            title = page.title
            content = wikipedia.summary(title, sentences="2") # gets summary for the article
            title = title + ": "
        except:
            pass

    return content



