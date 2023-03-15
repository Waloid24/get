import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
dac = dac [::1]
GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def binary2demical(value):
    print (bin(value))
    return [int (bit) for bit in (bin(value)[2:].zfill(8))]

def ValOutput (number):
    print ("Expected volts")
    print (3.3 / 256 * number)

def userInput ():
    try:
        inputStr = int(input())
        number = int (inputStr)

        if number < 0:
            print ("Only posistive numbers")
            return -1

        elif number > 256:
            print ("Number should be < 256")
            return -1

        else:
            return number

    except ValueError:
        if inputStr == "q":
            exit ()
        else:
            print ("Incorrect input: {inputStr} is not a number")
            return -1


try:
    while True:
        print ("Enter number from 0 to 255")

        number = userInput()
        if number != -1:
            binNumber = binary2demical(number)
            GPIO.output(dac, binNumber)
            ValOutput(number)

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()