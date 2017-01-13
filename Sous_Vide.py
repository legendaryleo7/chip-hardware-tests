from w1thermsensor import W1ThermSensor
import pid
import time
import math
import Adafruit_GPIO as GPIO


class SousVideBaseClass():
    def __init__(self, relay_pin, setpoint, Kp, Ki, Kd, controllerdirection, celsius=False):
        
        #define a relay pin
        self.relay_pin = relay_pin
        self.pid = pid.PID(self.temp, self.relay_pin, setpoint, Kp, Ki, Kd, controllerdirection )
        self.pid.set_mode("automatic")
        self.celsius = celsius
        gpio = GPIO.get_platform_gpio()
        gpio.setup(self.relay_pin, GPIO.OUT)
        #We're using Active Low 
        gpio.output(self.relay_pin, GPIO.HIGH)
        
    def run(self):
        self.pid.update = self.update_temp(celsius)
        if self.pid.compute():
            return self.pid.output
        else:
            return False
        
    def millis():
        return int(round(time.time() * 1000))
    
    
class SousVideRelayOneSensor(SousVideBaseClass):
    def __init__(self, 
                 relay_pin, 
                 setpoint, 
                 Kp, 
                 Ki, 
                 Kd, 
                 controllerdirection, 
                 celsius=False, 
                 windowsize=5000 ):
        
        
       
        
        #Establish our PID Library
        super(SousVideRelayOneSensor, self).__init__(self, 
                                            relay_pin, 
                                            setpoint, 
                                            Kp, 
                                            Ki, 
                                            Kd, 
                                            controllerdirection)
        
        #Set up a discrete way to use the analog relay_pin of the
        #PID with a digital relay_pin like a relay
        self.windowsize = windowsize
        self.windowstarttime = millis()
        self.pid.set_output_limits(0, self.windowsize)
        
         #Initialize our W1_Therm Library
        self.sensor = W1ThermSensor()
        #Establish our starting temperature
        self.celsius = celsius
        self.pid.input = self.update_temp(self.celsius)
        
    def run(self):
        #Run our PID
        self.pid.input = self.update_temp(self.celsius)
        self.pid.compute()
        
        #Configure 
        self.now = millis()
        if self.now - self.windowstarttime > self.windowsize:
            self.windowstarttime += self.windowsize
            
        if self.pid.output > self.now - self.windowstarttime:
            GPIO.set_mode(self.relay_pin, GPIO.LOW)
        else: 
            GPIO.set_mode(self.relay_pin, GPIO.HIGH)    
     
    def update_temp(celsius):

        if celsius is False:
            return self.sensor.get_temperature(W1ThermSensor.DEGREES_F)
        elif celsius is True:
            return self.sensor.get_temperature(W1ThermSensor.DEGREES_C)
               
class SousVideRelayOneSensorCharLCD(SousVideRelayOneSensor):
        
    def __init__(self,
                 relay_pin,
                 setpoint, 
                 Kp, 
                 Ki, 
                 Kd, 
                 controllerdirection, 
                 lcd, 
                 celsius=False, 
                 windowsize=5000):
        
        super(SousVideRelayOneSensorCharLCD, self).__init__(relay_pin, 
                                                   setpoint, 
                                                   Kp, 
                                                   Ki, 
                                                   Kd, 
                                                   controllerdirection, 
                                                   celsius=False,
                                                   windowsize=5000)
        self.lcd = lcd
        # Create Farenheight Degree Symbol
        self.lcd.create_char(1, [0b11000,
                                 0b11000,
                                 0b00000,
                                 0b00111,
                                 0b00100,
                                 0b00110,
                                 0b00100,
                                 0b00000])
            
        
        # Create Celsius  Degree Symbol
        self.lcd.create_char(2, [0b11000,
                                 0b11000,
                                 0b00011,
                                 0b00100,
                                 0b00100,
                                 0b00100,
                                 0b00011,
                                 0b00000])
        self.lcd.clear()
        
    def run(self):
        self.run()
        #super(SousVideRelayCharLCD, self).run()
        lcd.clear
        lcd.message('TEMP:{0:0.1f}\x01  \nGOAL:{1:0.1f}\x01'.format(self.pid.input, self.pid.setpoint))
        
        