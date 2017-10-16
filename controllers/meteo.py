"""
__Author__: Romain Maillard
__Date__: 16.10.2017
__Name__: meteo.py
__Description__: Fetch and parse the meteo

"""
from PyQt5.QtCore import QThread
import config
from signals import eventSignals
from bs4 import BeautifulSoup
import urllib.request
import re
from config import configfile

class MeteoControl(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        self.meteoText = MeteoText()
        self.meteoForcast = MeteoForcast()
        
    def run(self):
        self.meteoText.start()
        self.meteoForcast.start()
        
        while(self.running):
            
            self.sleep(1)
            
    def stop(self):
        self.running = False
        self.meteoText.quit()
        self.meteoForcast.quit()
        
    
    
        
class MeteoText(QThread):
    
    def __init__(self):
        super().__init__()
        self.running = True
        
    def run(self):
        
        while(self.running):
            
            self.getMeteo()
            self.sleep(10)
        
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False
        
    '''
    Get the meteo from website
    '''
    def getMeteo(self):
        data = []
        try:
            req = urllib.request.Request(config.meteoprediction)
            r = urllib.request.urlopen(req)
            html_doc = r.read().decode()
        except:
            print("Error connection")
        try: 
            soup = BeautifulSoup(html_doc, "html.parser")
            p = soup.find('div',{'id':'Meteo_prevision_txt'})
            for h in p.find_all('div'):
                try:
                    data.append(h.string.replace('\t',''))
                except:
                    pass
        except:
            print("Error parsing meteo")
            
        eventSignals.meteoText.emit(data)
    
class MeteoForcast(QThread):
    def __init__(self):
        super().__init__()
        self.running = True
        
        f = open(config.meteoAPI,'r')
        
        self.apikey = f.read()
        
        print(self.apikey)
        
    def run(self):
        
        while(self.running):
            
            #self.getMeteo()
            self.sleep(10)
            
        
    '''
    Get the meteo from website
    '''
    def getMeteo(self):
        data = []
        try:
            req = urllib.request.Request("http://api.wunderground.com/api/"+self.apikey+"/forecast/q/ch/lausanne.json")
            r = urllib.request.urlopen(req)
            html_doc = r.read().decode()
        except:
            print("Error connection")
        try: 
            soup = BeautifulSoup(html_doc, "html.parser")
            p = soup.find('div',{'id':'Meteo_prevision_txt'})
            for h in p.find_all('div'):
                try:
                    data.append(h.string.replace('\t',''))
                except:
                    pass
        except:
            print("Error parsing meteo")
            
        eventSignals.meteoText.emit(data)