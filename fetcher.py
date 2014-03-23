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

    try:
        page = wikipedia.page(query)
        title = page.title
        content = wikipedia.summary(title, sentences="2") # gets summary for the article
        title = title + ": "
    except:
        pass

    return content


def tokenize(text):
    '''Very simple white space tokenizer, in real life we'll be much more
    fancy.
    '''
    return text.split()


