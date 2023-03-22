import RPi.GPIO as GPIO
import time

def userInput ():
    try:
        number = int(input())

        if number < 0:
            print("Only positive number")
            return -1
        
        elif number > 255:
            print("A number must be less then 256")
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
GPIO.setup (26, GPIO.OUT)

p = GPIO.PWM(26, 0.5)    #channel = 26, frequency = 50Hz
p.start(0)              #where dc is the duty cycle (0.0 <= dc <= 100.0)


try:
    while True:
        print("Enter the duty cycle") #fladgkjfasf
        dc = userInput()
        if dc != -1:
            p.ChangeDutyCycle(dc) 


finally:
    GPIO.output (26, 0)
    GPIO.cleanup()

