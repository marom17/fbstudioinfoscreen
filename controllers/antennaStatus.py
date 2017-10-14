# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 13.10.2017
__Name__: antennaStatus.py
__Description__: Get where is the antenna and check if there is no SOS

"""
from PyQt5.QtCore import QThread
import config
from signals import eventSignals
import ssl
import urllib.request
import json

class StatusControl(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        
        self.running = True
        self.url = config.fbUrl
        
    def run(self):
        
        while(self.running):
            
            self.updateStatus()
            self.msleep(500)

    
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False
        
    '''
    Update the studio status
    '''
    def updateStatus(self):
        
        #create an HTTPS connection with the commutation
        context = ssl._create_unverified_context()
        req = urllib.request.Request(self.url)
        
        try:
            r = urllib.request.urlopen(req, timeout=1, context=context)
            data = r.read().decode()
            #print(data.replace('\\n','').replace('\\','')[1:-1])
            data = json.loads(data.replace('\\n','').replace('\\','')[1:-1])
            i = 0
            params = []
            for active in data["Active"]:
                if(active):
                    params.append(config.fbStudioNames[i])
                    continue
                    
                i = i + 1
                
            params.append(data["Active"][len(data["Active"])-2])
            params.append(data["Meters"][len(data["Meters"])-1])
            
            eventSignals.status.emit(params)
        except:
            eventSignals.status.emit([])