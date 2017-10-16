"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: config.py
__Description__: create the internal configuration

"""

import configparser

#parse the config file
configfile = configparser.RawConfigParser()
configfile.read('infoscreen.conf')

#tl-live urls
tlStationLeft = configfile.get('tl-live','stationLeft')
tlStationRight = configfile.get('tl-live','stationRight')
newsUrl = configfile.get('news','newsFeed')
fbUrl = configfile.get('fbinfo','url')
fbStudioNames = configfile.get('fbinfo','studioNames').split(',')
meteoprediction = configfile.get('meteo','prediction')