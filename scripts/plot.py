from monitoraggio_temperatura import *
import sys
import datetime

print (sys.argv)

if len(sys.argv)<2:
    inizio=datetime.datetime.now().strftime("%d-%m-%Y H:M:S").split(" ")[0] + " 00:00:00"
    plotta(leggiTemperature(inizio))

elif len(sys.argv)==3:
    plotta(leggiTemperature(sys.argv[1] + " " + sys.argv[2]))

elif len(sys.argv)==5:
    plotta(leggiTemperature(sys.argv[1] + " " + sys.argv[2],sys.argv[3] + " " + sys.argv[4]))

else:
    print("massimo 2 argomenti")
