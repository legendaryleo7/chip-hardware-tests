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

lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns,
                              lcd_rows, lcd_red, lcd_green, lcd_blue,
                              gpio=GPIO.get_platform_gpio(),
                              invert_polarity=True,
                              enable_pwm=True,
                              pwm=PWM.get_platform_pwm(pwmtype="softpwm"),
                              initial_color=(1.0, 1.0, 1.0))

sousvide = Sous_Vide.SousVideRelayOneSensorCharLCD(relay_pin,
                                            setpoint, 
                                            Kp, 
                                            Ki, 
                                            Kd, 
                                            controllerdirection, 
                                            lcd)
while 1:
    sousvide.run()
    