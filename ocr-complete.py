import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

from PIL import Image
import pytesseract
import argparse
import cv2
import pyttsx
import os
import RPi.GPIO as GPIO
import time
import picamera
from Queue import Queue
from threading import Thread

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

q = Queue()  #This is the line of audio that we need to play. So if more than
            #one audio, then the audio will wait in line to finish the first one

def say_loop(): #this is a function
    engine = pyttsx.init()
    while True:
        engine.say(q.get())
        engine.runAndWait()
        q.task_done()

def first_iteration():  #this is the function that is called.
    t = Thread(target=say_loop)
    t.daemon = True
    t.start()
    for i in range(0, 3):
        q.put(' ')

def continous(str): #this function is called for our audio
    q.put(str)


if __name__=="__main__":  #This is where our program starts from.

    first_iteration()  #Here the audio engine is initialized.

    while True: #while loop started
        input_state = GPIO.input(18)
        if input_state == False:        #if the button is pressed
           camera = picamera.PiCamera()
           camera.resolution = (1024, 768)
           camera.brightness = 70
           camera.contrast = 50
           camera.sharpness = 50 
           camera.start_preview()
           time.sleep(2)
           camera.capture("/home/pi/OCR/image.jpg")
           time.sleep(0.5) # wait for .5 seconds to let RPi process everything
       
           camera.close() #close the camera

           time.sleep(2)
       
           filename = os.path.abspath("/home/pi/OCR/image.jpg") #opening the file.
           text = pytesseract.image_to_string(Image.open(filename)) #Tesseract

           text = "  "  + text
           
           print(text)

           time.sleep(2)    #then we wait two second to let RPi process the above function
           continous(text)  #and then we play our required audio
           print("========END OF LOOP========")





