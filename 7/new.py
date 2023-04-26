import RPi.GPIO as GPIO
import time

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
COMP = 4
TROYKA = 17
MAX_VOLTAGE = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup (DAC, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (LEDS, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (TROYKA, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup (COMP, GPIO.IN)

def checkVoltage ():
    return GPIO.output(TROYKA)

def decimal2binary (value):
    return [int (bit) for bit in (bin(value)[2:]).zfill(8)]

def numToLeds (value):
    signal = decimal2binary(value)
    GPIO.output (LEDS, signal)
    return signal

valueVoltage = 0
measurements = [0]

try:
    while (valueVoltage < 97):
        startMeasurs = time.clock()
#         GPIO.input(TROYKA, GPIO.HIGH)
#         valueVoltage = checkVoltage() / MAX_VOLTAGE * 100 # percents
#         measurements.append(valueVoltage)
#         print(measurements)