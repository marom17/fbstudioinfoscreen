"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: signals.py
__Description__: gestion of all the signals

"""
from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    
    tl = pyqtSignal(str,list)
    time = pyqtSignal(str,str)
    news = pyqtSignal(list)

eventSignals = Signals()