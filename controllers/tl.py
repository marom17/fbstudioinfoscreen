"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: tl.py
__Description__: Parse the infos from the TL

"""
from PyQt5.QtCore import QThread
import config
from signals import eventSignals
from bs4 import BeautifulSoup
import urllib.request
import re

class TLControl(QThread):
    '''
    classdocs
    '''
    def __init__(self,side,stationUrl):
        super().__init__()
        self.side = side
        self.stationUrl = stationUrl
        self.running = True
        
        
    def run(self):
        while(self.running):
            
            self.getSchedul()
            self.msleep(4000)
            
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False
        
    def getSchedul(self):
        try:
            req = urllib.request.Request(self.stationUrl)
            r = urllib.request.urlopen(req, timeout=10)
            html_doc = r.read().decode()
            soup = BeautifulSoup(html_doc, "html.parser")
            try:
                linename = soup.find("div",{'class':'linename'})
                name = soup.find("div",{'class':'name'})
                nameString = []
                nameString.append(name.contents[0])
                nameString.append(name.contents[2])
                params = []
                params.append(linename.string)
                params.append(nameString[0])
                params.append(str(nameString[1])[3:-4])
                data = []
                for p in soup.find_all("div",{"class":'time'}):
                    #print(p)
                    if("None" not in str(p.string)):
                        data.append(p.string)
                    else:
                        text = str(p)
                        text = re.findall(r"[0-9]{1,2}:[0-9]{1,2}|[0-9']{2,3}", text)
                        data.append(text[0])
                        
                
                for i in range(0,4):
                    params.append(data[i])
                
                eventSignals.tl.emit(self.side,params)
            except:
                print("Error parse")
        
        except:
            print("Error Connection")
        