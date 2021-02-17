import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pins = {
    22 : {'name' : 'GPIO 22', 'state' : GPIO.LOW},
    23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
    17 : {'name' : 'GPIO 17', 'state' : GPIO.LOW},
    27 : {'name' : 'GPIO 27', 'state' : GPIO.LOW}
}

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

GPIO.output(23, GPIO.HIGH)
sleep(2)
GPIO.output(23, GPIO.LOW)

GPIO.cleanup()