import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
includefiles = ['infoscreen.conf','ressources/','apikey']
sys.path.append(os.path.abspath('controllers'))
sys.path.append(os.path.abspath('other'))
sys.path.append(os.path.abspath('ui'))

setup(  name = "FB Studio Info Dislpay",
        version = "0.0.1",
        description = "Display information about radio status",
        copyright="(c) Romain Maillard 2017",
        options = {"build_exe": {'include_files':includefiles}},
        executables = [Executable(
        "startStudioInfoScreen.py", 
        base="Win32GUI",
        copyright="(c) Romain Maillard 2017",
        icon="ressources/fbld.ico",
        targetName="StudioInfoScreen.exe"
        )])