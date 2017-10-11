"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: startStudioInfoScreen.py
__Description__: Start the studio info screen

"""
from PyQt5.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

print("Start Info Display")

ui = QWidget()
ui.show()
app.exec_()

print("Stop Info Display")