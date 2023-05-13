import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import os
from costanti import *

# Funzione per ottenere il valore delle temperatura si sistema della CPU
def getCPUtemperature():                                    #ricordati che restituisce una stringa, non un float
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    deg = u'\xb0'  # codice utf gradi
    deg = deg.encode('utf8')
    
    #print("temp is {0} degrees".format(temp))
    return temp

def scriviTemperatura():
    now=datetime.datetime.now()
    with open(directory + "/temperature.log", mode='a') as file:
            file.write('{0}: {1}\n'.format(now.strftime("%d-%m-%Y %H:%M:%S"),getCPUtemperature()))
            file.close()

def leggiTemperature(inizio = default_inizio, fine = default_fine):
    #inizio=datetime.datetime.strptime(inizioStringa,"%d-%m-%Y %H:%M:%S")
    #fine=datetime.datetime.strptime(fineStringa,"%d-%m-%Y %H:%M:%S")
    #print("da " + inizioStringa + " a " + fineStringa)
    temperature={}
    with open(directory + "/temperature.log", mode='r') as file:
        for i in file.readlines():
            try:
                temperature[datetime.datetime.strptime(i.split(": ")[0],"%d-%m-%Y %H:%M:%S")]=float(i.split(": ")[-1])
            except:
                print("riga {0} invalida ignorata".format(i))
    temperature = {key:value for key, value in temperature.items() if key>=inizio and key<=fine}
    return temperature

def leggiUltimeXOre(x):
    fine = datetime.datetime.now()
    inizio = fine - timedelta(hours=x)
    return leggiTemperature(inizio,fine)

def leggiUltimiXMinuti(x):
    fine = datetime.datetime.now()
    inizio = fine - timedelta(minutes=x)
    return leggiTemperature(inizio,fine)

def plotta (temperature):
    x=temperature.keys()
    y=temperature.values()
    #print(list(x))
    #print(list(y))
    plt.plot(list(x),list(y))
    plt.title("Monitoraggio temperatura")
    plt.show()
