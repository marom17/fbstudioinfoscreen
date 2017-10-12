"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiBroadcast.py
__Description__: Display the next broadcast

"""
from PyQt5.QtWidgets import QFrame
from signals import eventSignals

class uiBroadcast(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        self.setParent(parent)
        self.resize(parent.width(),parent.height()/2)
        self.setMaximumSize(parent.width(),parent.height()/2+1)
        self.setStyleSheet("background-color:black")
        eventSignals.broadcast.connect(self.updateBroadCast)
        
        
    def updateBroadCast(self,params):
        print(params)