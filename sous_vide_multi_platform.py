from w1thermsensor import W1ThermSensor
from enum import Enum
import PID
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.PWM as PWM
import Adafruit_CharLCD as LCD
import rotary_encoder


class ThermalUnits(Enum):
    CELSIUS = 1
    FAHRENHEIT = 2


class SousVide:
    def __init__(self, temp_unit=ThermalUnits.FAHRENHEIT):

        # Initialize Python GPIO Library
        self.plat = GPIO.Platform.platform_detect()
        self.gpio = GPIO.get_platform_gpio()

        # Set pin assignments
        self.set_pin_assignments()

        # Start the PID
        self.pid = PID.PID()
        self.temp_unit = temp_unit
        self.pid.SetPoint = self.set_default_temperature(self.temp_unit)

        self.lcd_columns = 16
        self.lcd_rows = 2
        
        # Initialize the LCD using the pins
        self.lcd = LCD.Adafruit_RGBCharLCD(self.lcd_rs,
                                           self.lcd_en,
                                           self.lcd_d4,
                                           self.lcd_d5,
                                           self.lcd_d6,
                                           self.lcd_d7,
                                           self.lcd_columns,
                                           self.lcd_rows,
                                           self.lcd_red,
                                           self.lcd_green,
                                           self.lcd_blue,
                                           gpio=GPIO.get_platform_gpio(),
                                           invert_polarity=True,
                                           enable_pwm=True,
                                           pwm=PWM.get_platform_pwm(pwmtype="softpwm"),
                                           initial_color=(1.0, 1.0, 1.0))

        # Blue startup screen
        self.lcd.set_color(0.0, 0.0, 1.0)
        self.lcd.clear()

        # Create Fahrenheit Degree Symbol
        self.lcd.create_char(1, [0b11000,
                                 0b11000,
                                 0b00000,
                                 0b00111,
                                 0b00100,
                                 0b00110,
                                 0b00100,
                                 0b00000])

        # Create Celsius Degree Symbol
        self.lcd.create_char(2, [0b11000,
                                 0b11000,
                                 0b00011,
                                 0b00100,
                                 0b00100,
                                 0b00100,
                                 0b00011,
                                 0b00000])

        # Initialize One Wire Thermal Sensor
        self.sensor = W1ThermSensor()

        # Setup relay for Active Low
        self.gpio.setup(self.relay_pin, GPIO.OUT)
        self.gpio.output(self.relay_pin, GPIO.HIGH)

        self.pid.setSampleTime(1)

        # Start the rotary encoder
        self.rotary_encoder0 = rotary_encoder.RotaryEncoder.Worker(self.rc1_a_pin, self.rc1_b_pin)
        self.rotary_encoder0.start()

    def get_temperature(self, temp_unit):
        """
        Polls the temperature sensor and returns a value based on the current
        unit measurement.

        Args:
            temp_unit: this is an enumeration of the ThermalUnits class

        Returns:
            The current temperature
        """
        if temp_unit is ThermalUnits.FAHRENHEIT:
            return self.sensor.get_temperature(W1ThermSensor.DEGREES_F)

        elif temp_unit is ThermalUnits.CELSIUS:
            return self.sensor.get_temperature(W1ThermSensor.DEGREES_C)

    def set_default_temperature(self):
        if self.temp_unit is ThermalUnits.FAHRENHEIT:
            return 130
        elif self.temp_unit is ThermalUnits.CELSIUS:
            return 55

    def set_pin_assignments(self):
        # Set Pin Assignments for the CHIP
        if self.plat is 5:
            # C.H.I.P. CharLCD Configuration
            self.lcd_rs = 'LCD-D4'
            self.lcd_en = 'LCD-D3'
            self.lcd_d4 = 'LCD-D6'
            self.lcd_d5 = 'LCD-D5'
            self.lcd_d6 = 'LCD-D10'
            self.lcd_d7 = 'LCD-D7'
            self.lcd_red = 'LCD-D12'
            self.lcd_green = 'LCD-D11'
            self.lcd_blue = 'LCD-D14'
            self.temp_pin = "LCD-D2"
            self.relay_pin = "LCD-D13"
            # Rotary Encoder pins
            self.rc1_a_pin = "XIO-P0"
            self.rc1_b_pin = "XIO-P1"

        elif self.plat is 1:
            # Raspberry Pi configuration:
            self.lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
            self.lcd_en = 22
            self.lcd_d4 = 25
            self.lcd_d5 = 24
            self.lcd_d6 = 23
            self.lcd_d7 = 18
            self.lcd_red = 4
            self.lcd_green = 17
            self.lcd_blue = 7  # Pin 7 is CE1
            # Temperature Sensor pin is LCD-D2
            self.temp_pin = 0  # Change this to something useful

            # Relay Pin Assignment
            self.relay_pin = 1  # Change this to something useful

        elif self.plat is 2:

            # BeagleBone Black configuration:
            self.lcd_rs = 'P8_8'
            self.lcd_en = 'P8_10'
            self.lcd_d4 = 'P8_18'
            self.lcd_d5 = 'P8_16'
            self.lcd_d6 = 'P8_14'
            self.lcd_d7 = 'P8_12'
            self.lcd_red = 'P8_7'
            self.lcd_green = 'P8_9'
            self.lcd_blue = 'P8_11'
            # Temperature Sensor pin is LCD-D2
            self.temp_pin = 0  # Change this to something useful

            # Relay Pin Assignment
            self.relay_pin = 1  # Change this to something useful

    def run(self):
        try:
            while 1:
                encoder1_delta = self.rotary_encoder0.get_delta()
                if encoder1_delta != 0:
                    self.pid.SetPoint = (encoder1_delta * .25) + self.pid.SetPoint

                temp = self.get_temperature(self.tempUnit)
                self.pid.update(temp)

                if self.pid.output >= 0:
                    self.gpio.output(self.relay_pin, GPIO.HIGH)
                    self.lcd.set_color(1.0, 0.0, 0.0)  # Red
                else:
                    self.gpio.output(self.relay_pin, GPIO.LOW)
                    self.lcd.set_color(0.0, 0.0, 1.0)  # Blue

                self.lcd.clear()
                self.lcd.message('TEMP:{0:0.1f}\x01  \nGOAL:{1:0.1f}\x01'.format(temp, self.pid.SetPoint))

        except KeyboardInterrupt:
            self.gpio.output(self.relay_pin, GPIO.HIGH)
            self.lcd.clear()
            if self.plat is 5:
                import CHIP_IO.Utilities as UT
                UT.unexport_all()
            pass



