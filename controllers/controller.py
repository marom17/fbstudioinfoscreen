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
    
    '''
    Launch all the controllers
    '''    
    def run(self):
    
        self.tlLeft.start()
        self.tlRight.start()
        self.clock.start()
        print("Controllers launch")
        
        while(self.running):
            
            self.sleep(1)
            
        self.tlLeft.quit()
        self.tlRight.quit()
        self.clock.stop()
        
        #self.tlLeft.wait()
        #self.tlRight.wait()
        self.clock.wait()
        print("Controllers stoped")
    '''
    Stop the loop
    '''        
    def stop(self):
        self.running = False