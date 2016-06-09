import Adafruit_GPIO.GPIO as GPIO
import gaugette.rotary_encoder
import gaugette.switch
import Adafruit_CharLCD as LCD
from subprocess import call
from w1thermsensor import W1ThermSensor

import math
import threading
import time


relay_pin = "XIO-P7"

# Insert LCD PIN Assignments Here
# lcd_rs = 'P8_8'
# lcd_en = 'P8_10'
# lcd_d4 = 'P8_18'
# lcd_d5 = 'P8_16'
# lcd_d6 = 'P8_14'
# lcd_d7 = 'P8_12'
# lcd_red   = 'P8_7'
# lcd_green = 'P8_9'
# lcd_blue  = 'P8_11'

# 
#   # # # # # # # # # # # # # # # # 
#	T e m p : X X . X 0   T i m e :
#	G o a L : X X 0       0 0 : 0 0 
# 

default_temp = 130
default_time = 0
default_time_steps = 5 #in minutes

class SensorInput:
	def __init__(self):
		self.encoder1_pinA = "XIO-P0"
		self.encoder1_pinB = "XIO-P1"
		self.encoder1_sw = "XIO-P4"

		self.encoder2_pinA = "XIO-P2"
		self.encoder2_pinB = "XIO-P3"
		self.encoder2_sw = "XIO-P5"

		#encoder1 will be Temperature 
		self.encoder1 = gaugette.rotary_encoder.RotaryEncoder.Worker(self.encoder1_pinA, self.encoder1_pinB)
		self.encoder1.start()

		#switch1 will be switch on the Temperature encoder
		self.switch1 = gaugette.switch.Switch(self.encoder1_sw)

		#encoder2 will be the Timer
		self.encoder2 = gaugette.rotary_encoder.RotaryEncoder.Worker(self.encoder2_pinA, self.encoder2_pinB)
		self.encoder2.start()
		#switch2 will be the switch on the Timer encoder
		self.switch2 = gaugette.switch.Switch(self.encoder2_sw)

		#configure our Temperature sensor
		call([sudo modprobe w1-gpio])
		call([sudo modprobe w1-therm])

		self.sensor = W1ThermSensor()
		current_temperature = self.sensor.get_temperature(W1ThermSensor.DEGREES_F)

	def gettemp(self):
		return current_temperature
	
	def	get_rotary_delta1():
		return self.encoder1.get_delta()

	def get_rotary_delta2():
		return self.encoder2.get_delta()

#Let's Go!
class SousVide ()
	def __init__():
		sensors = SensorInput()
		relay = RelayOutput()
		pid = PID()
		pid.SetPoint = default_temp
		pid.setSampleTime(self, 0.5)
		time_remaining = default_time
	def regulate_temperature():
		While time_remaining > 0:
			feedback = sensors.gettemp()
			pidoutput = pid.update(feedback)
			if pidoutput <= .5:
				relay.relay_on()
			else
				relay.relay_off()
	def update_contants():
		delta_encoder1 = sensors.get_rotary_delta1()
		delta_encoder2 = sensors.get_rotary_delta2()

		pid.Setpoint += delta_encoder1
		time_remaining += delta_encoder2 * time.minutes(default_time_steps)

	def time():
		while (time_remaining >= 0):
			time.sleep(1)
			time_remaining -= 1
			return time_remaining





lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              			lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
		lcd.set_color(0.0, 0.0, 1.0)
		lcd.clear()
		lcd.message('Hello There!')
		time.sleep(1)

