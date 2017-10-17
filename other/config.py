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
tlStationLeft1 = configfile.get('tl-live','stationLeft1')
tlStationRight1 = configfile.get('tl-live','stationRight1')
tlStationLeft2 = configfile.get('tl-live','stationLeft2')
tlStationRight2 = configfile.get('tl-live','stationRight2')
newsUrl = configfile.get('news','newsFeed')
fbUrl = configfile.get('fbinfo','url')
fbStudioNames = configfile.get('fbinfo','studioNames').split(',')
meteoprediction = configfile.get('meteo','prediction')
meteoAPI = configfile.get('meteo','apiKeyyFile')
meteoCity = configfile.get('meteo','city')
picfolder = "ressources/meteopics/"