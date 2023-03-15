import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
dac = dac [::1]
GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

p = 


finally:
    GPIO.output (dac, 0)
    GPIO.output (sec, 0)
    GPIO.cleanup()

