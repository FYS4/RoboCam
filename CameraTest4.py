import os
import sys
import time
import RPi.GPIO as GPIO

GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

image_num = 1

GPIO.output(4, False)

while True:
    if GPIO.input(17):
        strImage = str(image_num)
        os.system("raspistill -t 1000 -hf -vf -o image" + strImage + ".jpg")
        GPIO.output(4, True)
        time.sleep(3)
        GPIO.output(4, False)
        
