import RPi.GPIO as GPIO
import time

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256

def decimal2binary (value):
    return [int (bit) for bit in (bin(value)[2:]).zfill(8)]


GPIO.setmode(GPIO.BCM)
GPIO.setup (DAC, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (LEDS, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)


def num2dac (value):
    signal = decimal2binary(value)
    GPIO.output (DAC, signal)
    return signal

def volume(signal):
    array1 = [0,0,0,0,0,0,0,0]
    numOfLeds = 0
    for i in range (0, 8, 1):
        if signal[i] == 1:
            numOfLeds = i
            break
    for i in range (7-numOfLeds, -1, -1):
        array1[i] = 1
    return array1

sum = 0

try:
    while True:
        for value in range (7, -1, -1):
            number = 2**value + sum
            signal = num2dac (number)
            time.sleep (0.0007)
            compValue = GPIO.input (comp)
            if compValue == 1:
                sum = sum + 2**value

        voltage = sum / levels * maxVoltage
        print ("ADC value = {:^3} -> {}, input voltage = {:.2f}".format (sum, signal, voltage))
        binNumber = volume (signal)
        GPIO.output (LEDS, binNumber)
        sum = 0

except KeyboardInterrupt:
    print ("\nThe program was stopped by the keyboard")

finally:
    GPIO.output (DAC, GPIO.LOW)
    GPIO.cleanup(DAC)