import RPi.GPIO as GPIO
import time


DAC = [10, 9, 11, 5, 6, 13, 19, 26]
DAC = DAC[::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

def binary2decimal (value):
    return [int (bit) for bit in (bin(value)[2:]).zfill(8)]


try:
    Number = int (input())

    while True:
        print ("Input period of function")

        for i in range (256):
            binNumber = binary2decimal(i) 
            GPIO.output(DAC, binNumber)
            time.sleep (Number / (256*2))

        for i in range (255, -1, -1):
            binNumber = binary2decimal(i) 
            GPIO.output(DAC, binNumber)
            time.sleep (Number / (256*2))



finally:
    GPIO.output(DAC, 0)
    GPIO.cleanup()