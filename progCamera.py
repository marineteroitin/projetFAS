# -*- coding: utf-8 -*-

import picamera
import datetime
import time

def prendrePhoto(): 
	time.sleep(3) #temps d'attente avant de prendre la photo en secondes
	camera = picamera.PiCamera() 
	camera.resolution = (2592,1944) #resolution max de notre type de caméra
	camera.capture(str(datetime.datetime.now())+'.jpg') #prise de la photo avec renommage dans str

print("execution de prendre photo")
prendrePhoto()

