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

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)




while True:
    input_state = GPIO.input(18)
    if input_state == False:
       camera = picamera.PiCamera()
       camera.capture('image.jpg')
       time.sleep(0.5)
       ap = argparse.ArgumentParser()

       ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
       args = vars(ap.parse_args())
    
       filename = "ocr.jpg"

       text = pytesseract.image_to_string(Image.open(filename))
       print(text)

       engine = pyttsx.init()
       engine.say(text)
       engine.runAndWait()

       time.sleep(10)

       break



