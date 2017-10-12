"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: emissions.py
__Description__: Parse the comming emission

"""
from PyQt5.QtCore import QThread
from signals import eventSignals
from bs4 import BeautifulSoup
import urllib.request

class EmissionControl(QThread):
    
    def __init__(self):
        super().__init__()
        self.running = True
        
    def run(self):
        while(self.running):
            
            self.getBroadcast()
            
            self.sleep(10000)
            
    '''
    Get the emissions
    '''
    def getBroadcast(self):
        
        req = urllib.request.Request("https://www.frequencebanane.ch/grille-demissions/")
        r = urllib.request.urlopen(req)
        html_doc = r.read().decode()
        soup = BeautifulSoup(html_doc, "html.parser")
        p = soup.find_all("div",{'class':'wpex-row vcex-post-type-grid clr'})
        
        data = []
        
        for h in p[2].find_all("div",{'class':'match-height-content'}):
            title = h.find('a').string
            date = h.find('div').string.replace('\n','').replace('\t','')
            data.append([title,date])
            
        params = []
        
        for i in range(0,3):
            try:
                params.append(data[i])
            except:
                pass
        
        eventSignals.broadcast.emit(params)