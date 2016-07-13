import CHIP_IO.GPIO as GPIO
from subprocess import call
from w1thermsensor import W1ThermSensor
import PID
import time


# Temperature Sensor pin is LCD-D2
relay_pin = "XIO-P0"
target_temp =input('Enter a target temp: ')
#call("sudo modprobe w1_therm")

temp_sensor = W1ThermSensor()
temperature_in_fahrenheit = temp_sensor.get_temperature(W1ThermSensor.DEGREES_F)



GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.LOW)

pid = PID.PID()
pid.SetPoint=target_temp
pid.setSampleTime(1)



while 1:
    pid.update(temperature_in_fahrenheit)
    output = pid.output
    if output >= 1:
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        GPIO.output(relay_pin, GPIO.HIGH)
    temperature_in_fahrenheit = temp_sensor.get_temperature(W1ThermSensor.DEGREES_F)
    print("PID OUTOUT IS: " + str(output) + " and the temperature is: " + str(round(temperature_in_fahrenheit, 1)))
    time.sleep(5)
