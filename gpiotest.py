print(1)
from gpiozero import LED
print(2)
from time import sleep
print(3)

led = LED(17)
print(4)
led.on()
print(5)

sleep(2)
print(6)
led.off()
print(7)

