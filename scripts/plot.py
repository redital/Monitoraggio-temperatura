from monitoraggio_temperatura import *
import sys
import datetime
import re

#print (sys.argv)
if len(sys.argv)<2 or sys.argv[1].lower == "oggi":
    inizio=datetime.datetime.now().replace(hour=0,minute=0,second=0)
    plotta(leggiTemperature(inizio))

elif sys.argv[1].lower == "alltime":
    plotta()

elif re.match("ultime[0-9][0-9]?ore",sys.argv[1].lower())!=None:
    x = int(sys.argv[1].lower().split("ultime")[-1].split("ore")[0])
    plotta(leggiUltimeXOre(x))

elif sys.argv[1].lower == "ultimaora":
    plotta(leggiUltimeXOre(1))

elif re.match("ultimi[0-9][0-9]?minuti",sys.argv[1].lower())!=None:
    x = int(sys.argv[1].lower().split("ultimi")[-1].split("minuti")[0])
    plotta(leggiUltimiXMinuti(x))

elif sys.argv[1].lower == "oggi":
    plotta()

elif len(sys.argv)==3:
    try:
        inizio = datetime.datetime.strptime(sys.argv[1] + " " + sys.argv[2],"%d-%m-%Y %H:%M:%S")
    except:
        print("Input invalido!")
    plotta(leggiTemperature(inizio))

elif len(sys.argv)==5:
    try:
        inizio = datetime.datetime.strptime(sys.argv[1] + " " + sys.argv[2],"%d-%m-%Y %H:%M:%S")
        fine = datetime.datetime.strptime(sys.argv[3] + " " + sys.argv[4],"%d-%m-%Y %H:%M:%S")
    except:
        print("Input invalido!")
    plotta(leggiTemperature(inizio))

else:
    print("massimo 2 argomenti")
