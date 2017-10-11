"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: controller.py
__Description__: Control all the controller

"""
from PyQt5.QtCore import QThread
from tl import TLControl
import config
class MainController(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        self.tlLeft = TLControl(config.tlStationLeft)
        self.tlRight = TLControl(config.tlStationRight)
    
    '''
    Launch all the controllers
    '''    
    def run(self):
    
        self.tlLeft.start()
        self.tlRight.start()
        print("Controllers launch")
        
        while(self.running):
            
            self.sleep(1)
            
        self.tlLeft.stop()
        self.tlRight.stop()
        
        self.tlLeft.wait()
        self.tlRight.wait()
        print("Controllers stoped")
    '''
    Stop the loop
    '''        
    def stop(self):
        self.running = False