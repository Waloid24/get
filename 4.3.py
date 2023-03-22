import RPi.GPIO as GPIO
import time

def userInput ():
    try:
        number = int(input())

        if number < 0:
            print("Only positive number")
            return -1
        
        elif number > 100:
            print("A number must be less then 100")
            return -1
        
        else:
            return number
    
    except ValueError:
        if number == "q":
            exit ()
        else:
            print ("Incorrect input: {inputStr} is not a number")
            return -1

GPIO.setmode(GPIO.BCM)
GPIO.setup (22, GPIO.OUT)

p = GPIO.PWM(22, 100)    #channel = 26, frequency = 50Hz
p.start(0)               #where dc is the duty cycle (0.0 <= dc <= 100.0)


try:
    while True:
        print("Enter the % for duty cycle") #fladgkjfasf
        dc = userInput()
        p.ChangeDutyCycle(dc)
        print (f"Estimated volt: {dc/100 * 3.3}")


finally:
    p.stop()
    GPIO.output (22, 0)
    GPIO.cleanup()

