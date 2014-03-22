from bs4 import BeautifulSoup
import twilio.twiml
import requests
import urllib, urllib2
import sys
import wikipedia
import re
from collections import defaultdict
MAX_SUMMARY_SIZE = 350


def getPage(query, lang='en'):
    wikipedia.set_lang(lang)

    content = "Query not found! We're sorry, try a different one! :("

    try:
        page = wikipedia.page(query)
        title = page.title
        content = wikipedia.summary(title, sentences="6") # gets summary for the article
        title = title + ": "
    except:
        pass

    return content


def tokenize(text):
    '''Very simple white space tokenizer, in real life we'll be much more
    fancy.
    '''
    return text.split()

def split_to_sentences(text):
    '''Very simple spliting to sentences by [.!?] and paragraphs.
    In real life we'll be much more fancy.
    '''
    sentences = []
    start = 0

    # We use finditer and not split since we want to keep the end
    for match in re.finditer('(\s*[.!?]\s*)|(\n{2,})', text):
        sentences.append(text[start:match.end()].strip())
        start = match.end()

    if start < len(text):
        sentences.append(text[start:].strip())

    return sentences


def token_frequency(text):
    '''Return frequency (count) for each token in the text'''
    frequencies = defaultdict(int)
    for token in tokenize(text):
        frequencies[token] += 1

    return frequencies


def sentence_score(sentence, frequencies):
    return sum((frequencies[token] for token in tokenize(sentence)))


def create_summary(sentences, max_length):
    summary = []
    size = 0
    for sentence in sentences:
        summary.append(sentence)
        size += len(sentence)
        if size >= max_length:
            break
    summary = summary[:max_length]
    
    return '\n'.join(summary)


def summarize(text, max_summary_size=MAX_SUMMARY_SIZE):
    frequencies = token_frequency(text)
    sentences = split_to_sentences(text)
    sentences.sort(key=lambda s: sentence_score(s, frequencies), reverse=1)
    summary = create_summary(sentences, max_summary_size)

    return summary

