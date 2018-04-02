#!/bin/bash

# Bash Script to innvoke the Alexa with one click on Raspberry Pi.

# To kill the processes that are already running
pkill -f node     
pkill -f java
pkill -f wakeWordA

#Starts Companion Service - Basically a server for Amazon Alexa
echo "starting companion service"
cd /home/pi/alexakind/alexa-avs-sample-app/samples/
cd companionService && npm start&
echo "starting companion service" > alexa_startup.out

sleep 5   # sleep for 5 seconds to load the server

#Starts Javaclient Service - This creates the Client part for Amazon Alexa
echo "starting javaclient"
cd /home/pi/alexakind/alexa-avs-sample-app/samples/
cd javaclient && mvn exec:exec&
echo "starting javaclient" >> alexa_startup.out

sleep 25     # sleep for 5 seconds to load the client as it takes some time


#Starts Wake word Agent to invoke Alexa by a word "Alexa"
echo "starting wake word agent"
cd /home/pi/alexakind/alexa-avs-sample-app/samples/
cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai&
echo "starting wake word agent" >> alexa_startup.out

