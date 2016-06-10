import Adafruit_GPIO.GPIO as GPIO
import gaugette.rotary_encoder
import gaugette.switch
import Adafruit_CharLCD as LCD
from subprocess import call
from w1thermsensor import W1ThermSensor
import relay
import PID

import math
import threading
import time


relay_pin = "XIO-P7"

encoder1_pinA = "XIO-P0"
encoder1_pinB = "XIO-P1"
encoder1_sw = "XIO-P4"
encoder2_pinA = "XIO-P2"
encoder2_pinB ="XIO-P3"
encoder2_sw ="XIO-P5"

# Insert LCD PIN Assignments Here
# This came from the BBB and will not work with CHIP
# lcd_rs = 'P8_8'
# lcd_en = 'P8_10'
# lcd_d4 = 'P8_18'
# lcd_d5 = 'P8_16'
# lcd_d6 = 'P8_14'
# lcd_d7 = 'P8_12'
# lcd_red   = 'P8_7'
# lcd_green = 'P8_9'
# lcd_blue  = 'P8_11'



default_temp = 130
default_time = 0
default_time_steps = 5 #in minutes

tempsensor = W1ThermSensor()
current_temperature = tempsensor.get_temperature(W1ThermSensor.DEGREES_F)


#Let's Go!
class SousVide ():
	def __init__():
        lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              			lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
		lcd.set_color(0.0, 0.0, 1.0)
		lcd.clear()
		lcd.message('Hello There!')
		time.sleep(1)
        encoder1=rotary_encoder.RotaryEncoder.Worker(encoder1_pinA,  encoder1_pinB)
        encoder1.run()
        encoder2=rotary_encoder.RotaryEncoder.Worker(encoder2_pinA,  encoder2_pinB)
        encoder2.run()
        
        pid = PID()
		pid.SetPoint = default_temp
		pid.setSampleTime(self, 0.5)
		time_remaining = default_time
	def regulate_temperature():
		While time_remaining > 0:
			feedback = current_temperature
			pidoutput = pid.update(feedback)
			if pidoutput <= .5
				relay.RelayOutput.relay_on()
			else
				relay.RelayOutput.relay_off()
	def update_contants():
		delta_encoder1 = encoder1.get_delta()
		delta_encoder2 =encoder2.get_delta()

		pid.Setpoint += delta_encoder1
		time_remaining += delta_encoder2 * time.minutes(default_time_steps)

	def time():
		while (time_remaining >= 0):
			time.sleep(1)
			time_remaining -= 1
			return time_remaining
    def update_screen()
        lcd.message("Temp:"+round(current_temperature, 1)+"F TimeGoal:"+pid.SetPoint +"F   "+time(time_remaining))

# 
#   # # # # # # # # # # # # # # # # 
#	 T  e  m p  :  X X  X .  X  F     T  i  m e  :
#	 G  o  a L  :  X  X X F         0  0  :  0  0  
# 




