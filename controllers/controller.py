"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: controller.py
__Description__: Control all the controller

"""
from PyQt5.QtCore import QThread
from tl import TLControl
import config
from clock import ClockControl
from news import NewsControl
from emissions import EmissionControl
from antennaStatus import StatusControl
from meteo import MeteoControl
from music import MusicControl

class MainController(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        self.tlLeft = TLControl('left',config.tlStationLeft)
        self.tlRight = TLControl('right',config.tlStationRight)
        self.clock = ClockControl()
        self.news = NewsControl()
        self.broadcast = EmissionControl()
        self.FBstatus = StatusControl()
        self.meteo = MeteoControl()
        self.music = MusicControl()
    
    '''
    Launch all the controllers
    '''    
    def run(self):
    
        self.tlLeft.start()
        self.tlRight.start()
        self.clock.start()
        self.news.start()
        self.broadcast.start()
        self.FBstatus.start()
        self.meteo.start()
        self.music.start()
        print("Controllers launch")
        
        while(self.running):
            
            self.sleep(1)
            
        self.tlLeft.quit()
        self.tlRight.quit()
        self.clock.stop()
        self.news.quit()
        self.broadcast.quit()
        self.FBstatus.stop()
        self.meteo.stop()
        self.music.stop()
        
        self.clock.wait()
        self.FBstatus.wait()
        self.meteo.wait()
        self.music.wait()
        print("Controllers stoped")
    '''
    Stop the loop
    '''        
    def stop(self):
        self.running = False