"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: clock.py
__Description__: Update the time

"""
from PyQt5.QtCore import QThread
from signals import eventSignals
import time

class ClockControl(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        
    '''
    Run the clock
    '''
    def run(self):
        
        while(self.running):
            
            self.updateClock()
            
            self.msleep(500)
            
            
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False
        
    '''
    Update the clock
    '''
    def updateClock(self):
        date = time.strftime("%Y-%m-%d")
        hour = time.strftime("%H:%M:%S")
        
        eventSignals.time.emit(date,hour)