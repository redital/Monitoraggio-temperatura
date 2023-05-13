import monitoraggio_temperatura as ct
from time import sleep

while True:
	ct.scriviTemperatura()
	sleep(300)
