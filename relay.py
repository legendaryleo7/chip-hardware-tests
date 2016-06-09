#this is an abstraction layer to quickly toggle a GPIO pin between Low and High


import Adafruit_GPIO as GPIO

class RelayOutput:
	def __init__(self, relay_pin):
		#define the relay pin:
		self.relayPIN = relay_pin
		GPIO.BaseGPIO.setup(self, self.relayPIN, GPIO.OUT,)
	def relay_on(self):
		GPIO.BaseGPIO.output(self, self.relayPIN, True)
	def relay_off(self):
		GPIO.BaseGPIO.output(self, self.relayPIN, False)
