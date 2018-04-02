import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin = 5
GPIO.setup(pinNum, GPIO.OUT)
GPIO.output(pinNum, GPIO.HIGH)
#GPIO.output(pinNum, GPIO.LOW)
