from w1thermsensor import W1ThermSensor
import pid
import time
import math
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.PWM as PWM
import Adafruit_CharLCD as LCD
import Sous_Vide
from time import sleep


relay = "XIO-P0"
setpoint = 130
Kp = 0
Ki = 0
Kd = 0
controllerdirection = "direct"

sousvide = Sous_Vide.SousVideRelayOneSensor(relay, setpoint, Kp, Ki, controllerdirection)

while 1:
    sousvide.run()
    print("Output was {0:0.1f} and Temp was {1:0.1f}".format(sousvide.pid.output, self.pid.input))
    sleep(5)