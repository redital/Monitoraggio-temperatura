import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import datetime

led = 14        # Identificativo del pin del led
fan = 15        # Identificativo del pin della ventola
maxTMP = 58     # La temperatura massima in gradi Celsius oltre la quale si attiva la ventola
directory='/home/redital/Desktop/controllo_ventola'

# Funzione per il setup delle porte GPIO
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(fan, GPIO.OUT)
    GPIO.setwarnings(False)
    loggingACC() # Funzione per logging all'accensione del Raspberry

# Funzione per ottenere il valore delle temperatura si sistema della CPU
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    deg = u'\xb0'  # utf code for degree
    deg = deg.encode('utf8')
    
    #print("temp is {0} degrees".format(temp)) # Scommenta per test 
    return temp


#---------------------------------------------Loggging------------------------------------------------#

# Funzione per logging all'accensione del Raspberry
def loggingACC():
    now=datetime.datetime.now()
    with open(directory + "/fan.log", mode='a') as file:
        deg = u'\xb0'  # utf code for degree
        deg = deg.encode('utf8')
        file.write('------------------ SISTEMA AVVIATO ------------------\n%s: Temperatura = %s%s\n' %(now.strftime("%d-%m-%Y %H:%M:%S"),getCPUtemperature(),deg))
        file.close()

# Funzione per logging all'accensione della ventola
def loggingON():
    now=datetime.datetime.now()
    with open(directory + "/fan.log", mode='a') as file:
        deg = u'\xb0'  # utf code for degree
        deg = deg.encode('utf8')
        file.write('%s: Temperatura = %s%s Ventola ON\n' %(now.strftime("%d-%m-%Y %H:%M:%S"),getCPUtemperature(),deg))
        file.close()

# Funzione per logging allo spegnimento della ventola
def loggingOFF():
    now=datetime.datetime.now()
    with open(directory + "/fan.log", mode='a') as file:
        deg = u'\xb0'  # utf code for degree
        deg = deg.encode('utf8')
        file.write('%s: Temperatura = %s%s Ventola OFF\n' %(now.strftime("%d-%m-%Y %H:%M:%S"),getCPUtemperature(),deg))
        file.close()

#---------------------------------------------Funzioni ventola------------------------------------------------#

# Funzione per l'accensione della ventola
def fanON():
    #print("accendo")  # Scommenta per test
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(fan, GPIO.HIGH)
    loggingON()
    return()

# Funzione per lo spegnimento della ventola
def fanOFF():
    #print("spengo") # Scommenta per test
    GPIO.output(led, GPIO.LOW)
    GPIO.output(fan, GPIO.LOW)
    loggingOFF()
    return()