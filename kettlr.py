#!/usr/bin/env python
import time

from flask import Flask
import RPi.GPIO as GPIO
import sh
import signal


class KettleRobot:
    TIME_TO_TURN_ON = 1
    def turn_on_kettle(self):
        servopin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servopin, GPIO.OUT, initial=False)
        p = GPIO.PWM(servopin,50)
        p.start(12.5)
        time.sleep(self.TIME_TO_TURN_ON)
        p.ChangeDutyCycle(2.5)
        time.sleep(self.TIME_TO_TURN_ON)
        p.stop()
        GPIO.cleanup()


app = Flask(__name__)

@app.route("/on/")
def turn_the_kettle_on():
    robot = KettleRobot()
    robot.turn_on_kettle()
    return "Boiling!"