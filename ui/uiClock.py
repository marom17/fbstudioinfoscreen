"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiClock.py
__Description__: Display the time

"""

from PyQt5.QtWidgets import QFrame, QWidget, QLabel
from signals import eventSignals

class UIClock(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        self.setParent(parent)
        self.resize(parent.width()/2,parent.height()/2)
        self.setMinimumSize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:red")
        self.setAutoFillBackground(True)
        
        text = QLabel("Hello",self)
        
        eventSignals.time.connect(self.updateTime)
        
        self.show()
        
    '''
    Update the time
    '''
    def updateTime(self,date,time):
        pass
        