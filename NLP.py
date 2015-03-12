#this code gets urls for all articles using webscraping and the NLP api. takes all articles that list on the page. edit for whatever dates you need

import urllib2
from bs4 import BeautifulSoup
names=["GPS", "NFLX", "CAT", "ROST", "ADSK", "STJ", "GME", "DAL", "BAC", "ATI", "LUV", "GRPN", "INTC", "AAPL", "MOLG", "WAIR", "OTIV", "AMDA", "ARUN", "ICLDW", "AAPL", "GOOG", "BABA"]

def calc(names):
    for i in names:
        url = 'http://finance.yahoo.com/q?s='+i
        data = urllib2.urlopen(url)
        soup = BeautifulSoup(data)
        
        divs = soup.find('div',attrs={'id':'yfi_headlines'})
        div = divs.find('div',attrs={'class':'bd'})
        ul = div.find('ul')
        lis = ul.findAll('li')
        print i
        m=0.0
        for li in lis:
            headlines = li.find('a').get('href')
            #print headlines
            ur='http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=76f7dbc36d0342aeafd46210b09db50177b0a3ac&url='+headlines
            dat=urllib2.urlopen(ur)
            sou=BeautifulSoup(dat)
            if sou.find('score')!=None:
                m+=float(sou.find('score').string)
        return m
        
#calc(names)