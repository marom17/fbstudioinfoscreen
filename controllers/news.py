"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: news.py
__Description__: Control news

"""

from PyQt5.QtCore import QThread
import config
from signals import eventSignals
from bs4 import BeautifulSoup
import urllib.request
import re

class NewsControl(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        self.newsUrl = config.newsUrl
        
    
    def run(self):
        
        while(self.running):
            self.parseNews()
            self.sleep(5000)
            
    '''
    Fetch the news
    '''
    def parseNews(self):
        try:
            req = urllib.request.Request(self.newsUrl)
            r = urllib.request.urlopen(req, timeout=10)
            html_doc = r.read().decode()
            soup = BeautifulSoup(html_doc, "html.parser")
            data = []
            try:
                for p in soup.find_all("div",{"class":"News"}):
                    time = p.find("div",{'class':'HeureFluxNews'}).string.replace('\t','').replace('\n','')
                    news = p.find("a",{'class':'TitreNewsLink'}).string
                    data.append([time,news])
                
                newsToSend = []
                for i in range(0,5):
                    newsToSend.append(data[i])
                
                eventSignals.news.emit(newsToSend)
            except:
                print("Error parsing")
        except:
            print("Error connection")