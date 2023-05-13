from controllo_ventola import getCPUtemperature #ricordati che restituisce una stringa, non un float
import matplotlib.pyplot as plt
import matplotlib.dates as mlp_dates
import datetime
import numpy as np

directory='/home/redital/Desktop/monitoraggio_temperatura'
annoZero=2022

def scriviTemperatura():
    now=datetime.datetime.now()
    with open(directory + "/temperature.log", mode='a') as file:
            file.write('{0}: {1}\n'.format(now.strftime("%d-%m-%Y %H:%M:%S"),getCPUtemperature()))
            file.close()

def leggiTemperature(inizioStringa="01-01-2022 00:00:00", fineStringa="01-01-2122 23:59:59"):
    inizio=conversioneTempo(inizioStringa)
    fine=conversioneTempo(fineStringa)
    #print("da " + inizioStringa + " a " + fineStringa)
    temperature={}
    with open(directory + "/temperature.log", mode='r') as file:
        for i in file.readlines():
            try:
                temperature[conversioneTempo(i.split(": ")[0])]=float(i.split(": ")[-1])
            except:
                print("riga {0} invalida ignorata".format(i))
    daEliminare=[]
    for key in temperature:
        if key[0]>fine[0] or (key[0]==fine[0] and key[1]>fine[1]) or key[0]<inizio[0] or (key[0]==inizio[0] and key[1]<inizio[1]):
            daEliminare.append(key)
    for key in daEliminare:
        del temperature[key]
    return temperature

def leggiUltimeXOre(x):
    fineStringa=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    oraFine=int(fineStringa.split(" ")[-1].split(":")[0])
    inizioStringa=fineStringa.split(" ")[0] + " " + str(oraFine-x) + ":" + fineStringa.split(":")[1] + ":" + fineStringa.split(":")[2]
    print (inizioStringa + " ------>" + fineStringa)
    return leggiTemperature(inizioStringa,fineStringa)

def leggiUltimiXMinuti(x):
    fineStringa=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    oraFine=int(fineStringa.split(":")[1])
    inizioStringa=fineStringa.split(":")[0] + ":" + str(oraFine-x) + ":" + fineStringa.split(":")[2]
    print (inizioStringa + " ------>" + fineStringa)
    return leggiTemperature(inizioStringa,fineStringa)

def conversioneTempo(stringaTempo):
    dataStringa=stringaTempo.split(" ")[0]
    orarioStringa=stringaTempo.split(" ")[-1]
    #Il minimo giorno esistente è 01/01/2022 che è codificato come 32. Per ogni data esiste un unico codice, ma non per ogni codice esiste una data
    data=(int(dataStringa.split("-")[2])-annoZero)*360 + (int(dataStringa.split("-")[1]))*31 + int(dataStringa.split("-")[0])
    orario=(int(orarioStringa.split(":")[0]))*60*60 + (int(orarioStringa.split(":")[1]))*60 + int(orarioStringa.split(":")[2])
    return data, orario


def plotta (temperature):
    #xTupla=temperature.keys()
    x=[]
    for i in temperature.keys():
        x.append(i[1]+(i[0]-342)*86399)
    y=temperature.values()
    #print(list(x))
    #print(list(y))
    plt.plot(list(x),list(y))
    plt.title("Monitoraggio temperatura")
    plt.show()
