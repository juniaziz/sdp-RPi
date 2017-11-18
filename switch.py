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

