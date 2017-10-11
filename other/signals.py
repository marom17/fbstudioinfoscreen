"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: signals.py
__Description__: gestion of all the signals

"""
from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    
    tlLeft = pyqtSignal([list])
    tlRight = pyqtSignal([list])

eventSignals = Signals()