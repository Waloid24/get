import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
COMP = 4
TROYKA = 17
MAX_VOLTAGE = 3.3
LEVELS = 256

GPIO.setmode(GPIO.BCM)
GPIO.setup (DAC, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (LEDS, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup (TROYKA, GPIO.OUT)
GPIO.output (TROYKA, 0)
GPIO.setup (COMP, GPIO.IN)

def checkVoltage ():
    return GPIO.input(TROYKA)

def decimal2binary (value):
    return [int (bit) for bit in (bin(value)[2:]).zfill(8)]

def numToLeds (value):
    signal = decimal2binary(value)
    GPIO.output (LEDS, signal)
    return signal

def num2dac (value):
    signal = decimal2binary(value)
    GPIO.output (DAC, signal)
    return signal

valueVoltage = 0
measurements = [0]
times = [0]
sum = 0
voltage = 0

try:
    GPIO.output (TROYKA, 0)
    startMeasurs = time.time()
    numMeasurs = 0
    while voltage < 3.17:
        for value in range (7, -1, -1):
            number = 2**value + sum
            signal = num2dac (number)
            time.sleep (0.05)
            compValue = GPIO.input (COMP)
            if compValue == 1:
                sum = sum + 2**value

        voltage = sum / LEVELS * MAX_VOLTAGE
        print ("ADC value = {:^3} -> {}, input voltage = {:.2f}".format (value, signal, voltage))
        measurements.append(voltage)
        sum = 0
        times.append (time.time()-startMeasurs)
        numMeasurs += 1
    GPIO.output (TROYKA, 1)
    while voltage > 0.74:
        for value in range (7, -1, -1):
            number = 2**value + sum
            signal = num2dac (number)
            time.sleep (0.05)
            compValue = GPIO.input (COMP)
            if compValue == 1:
                sum = sum + 2**value

        voltage = sum / LEVELS * MAX_VOLTAGE
        print ("ADC value = {:^3} -> {}, input voltage = {:.2f}".format (value, signal, voltage))
        measurements.append(voltage)
        sum = 0
        times.append (time.time()-startMeasurs)
        numMeasurs += 1

    endMeasurs = time.time()
    duration = endMeasurs - startMeasurs
    print (duration)
    plt.plot (times, measurements)
    plt.show ()

    measurements_str = [str(item) for item in measurements]

    with open("data.txt", "w") as outfile:
        outfile.write ("\n".join(measurements_str))

    kvantovanie = MAX_VOLTAGE / 256
    period = duration/numMeasurs
    frequency = 1/period
    
    with open("settings.txt", "w") as outfile:
        outfile.write ("duration = " + str(duration) + "\nkvantovanie = " + str(kvantovanie) + "\nperiod = " + str(period) + "\nfrequency = " + str(frequency))


except KeyboardInterrupt:
    print ("\nThe program was stopped by the keyboard")

finally:
    GPIO.output (DAC, GPIO.LOW)
    GPIO.output (LEDS, GPIO.LOW)
    GPIO.cleanup(DAC)
    GPIO.cleanup(LEDS)