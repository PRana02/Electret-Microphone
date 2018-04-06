# A python script to understand the custom skills created on Alexa
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
    
@ask.intent('professor',mapping={'who':'who'}) 
def turn(who):

    if(who=='your'):
        return statement('My professor is Piyush Rana')
    
    elif(who=='my'):
        return statement('Your professor is Kristian Medri')
    
    if __name__ == '__main__':
            port = 5000 #the custom port you want
            
            app.run(host='0.0.0.0', port=port)
