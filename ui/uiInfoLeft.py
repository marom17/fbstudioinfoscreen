"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiInfoLeft.py
__Description__: Display the left Banane info

"""
from PyQt5.QtWidgets import QFrame
from uiBroadcast import uiBroadcast

class UIInfoLeft(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        
        #set frame
        self.setParent(parent)
        self.resize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:black")
        
        self.drawInfoLeft()
        
        self.show()
        
        
    def drawInfoLeft(self):
        
        self.broadcast = uiBroadcast(self)