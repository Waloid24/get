import RPi.GPIO as GPIO

import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def binary2demical(value):
    return [int (bit) for bit in (bin(value)[2:]).zfill(8)]

try:
    print ("Input priod of function")    #adfsghadflg
    number = int(input())

    while True:
        for i in range (256):
            binNumber = binary2demical(i)
            GPIO.output (dac, binNumber)
            time.sleep (number / (256*2))

        for i in range (255, -1, -1):
            binNumber = binary2demical(i)
            GPIO.output (dac, binNumber)
            time.sleep (number / (256*2))

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()