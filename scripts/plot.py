from monitoraggio_temperatura import *
import sys
import datetime

print (sys.argv)

if len(sys.argv)<2:
    inizio=datetime.datetime.now()
    plotta(leggiTemperature(inizio))

elif len(sys.argv)==3:
    inizio = datetime.datetime.strptime(sys.argv[1] + " " + sys.argv[2],"%d-%m-%Y %H:%M:%S")
    plotta(leggiTemperature(inizio))

elif len(sys.argv)==5:
    inizio = datetime.datetime.strptime(sys.argv[1] + " " + sys.argv[2],"%d-%m-%Y %H:%M:%S")
    fine = datetime.datetime.strptime(sys.argv[3] + " " + sys.argv[4],"%d-%m-%Y %H:%M:%S")
    plotta(leggiTemperature(inizio))

else:
    print("massimo 2 argomenti")
