# A python script to turn the LED on and off according to the command given to Alexa.
# Running this script also sends the data to firebase database
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

from firebase import firebase
firebase = firebase.FirebaseApplication('https://switch-e1142.firebaseio.com', None) #Creating firebase database instance

GPIO.setmode(GPIO.BCM)
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
    
@ask.intent('TurnLights', mapping={'status':'status'}) 
def turn(status):

    GPIO.setup(17,GPIO.OUT) #configure for the specific pin
    
    if(status=='on'):
        GPIO.output(17,GPIO.HIGH)
        firebase.put('https://switch-e1142.firebaseio.com','LED','ON') #Pushing the staus of LED to the firebase database

    elif(status=='off'):
        GPIO.output(17,GPIO.LOW)
        firebase.put('https://switch-e1142.firebaseio.com','LED','OFF') #Pushing the staus of LED to the firebase database

        return statement('Turning {} LED'.format(status))

        if __name__ == '__main__':
            port = 5000 #the custom port you want
                
            app.run(host='0.0.0.0', port=port)
