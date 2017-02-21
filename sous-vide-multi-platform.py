from w1thermsensor import W1ThermSensor
import PID
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.PWM as PWM
import Adafruit_CharLCD as LCD
import rotary_encoder

# Configure Defaults
# Configure Units
celsius_unit = False  # Default to Farnheight

# starting temp
if celsius_unit is False:
    target_temp = 130
elif celsius_unit is True:
    target_temp = 55

plat = GPIO.Platform.platform_detect()

if plat is 5:
    # C.H.I.P. CharLCD Configuration
    lcd_rs = 'LCD-D4'
    lcd_en = 'LCD-D3'
    lcd_d4 = 'LCD-D6'
    lcd_d5 = 'LCD-D5'
    lcd_d6 = 'LCD-D10'
    lcd_d7 = 'LCD-D7'
    lcd_red = 'LCD-D12'
    lcd_green = 'LCD-D11'
    lcd_blue = 'LCD-D14'

    # Temperature Sensor pin is LCD-D2
    temp_pin = "LCD-D2"

    # Relay Pin Assignment
    relay_pin = "LCD-D13"

    # Rotary Encoder pins
    rc1_a_pin = "XIO-P0"
    rc1_b_pin = "XIO-P1"

elif plat is 1:
    # Raspberry Pi configuration:
    lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
    lcd_en = 22
    lcd_d4 = 25
    lcd_d5 = 24
    lcd_d6 = 23
    lcd_d7 = 18
    lcd_red = 4
    lcd_green = 17
    lcd_blue = 7  # Pin 7 is CE1
    # Temperature Sensor pin is LCD-D2
    temp_pin = 0  # Change this to something useful

    # Relay Pin Assignment
    relay_pin = 1  # Change this to something useful

elif plat is 2:

    # BeagleBone Black configuration:
    lcd_rs = 'P8_8'
    lcd_en = 'P8_10'
    lcd_d4 = 'P8_18'
    lcd_d5 = 'P8_16'
    lcd_d6 = 'P8_14'
    lcd_d7 = 'P8_12'
    lcd_red = 'P8_7'
    lcd_green = 'P8_9'
    lcd_blue = 'P8_11'
    # Temperature Sensor pin is LCD-D2
    temp_pin = 0  # Change this to something useful

    # Relay Pin Assignment
    relay_pin = 1  # Change this to something useful


# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize GPIO
gpio = GPIO.get_platform_gpio()
# Initialize One Wire Thermal Sensor
sensor = W1ThermSensor()

# Initialize the LCD using the pins
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns,
                              lcd_rows, lcd_red, lcd_green, lcd_blue,
                              gpio=GPIO.get_platform_gpio(),
                              invert_polarity=True,
                              enable_pwm=True,
                              pwm=PWM.get_platform_pwm(pwmtype="softpwm"),
                              initial_color=(1.0, 1.0, 1.0))


# Blue startup screen
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()

# Create Farenheight Degree Symbol
lcd.create_char(1, [0b11000,
                    0b11000,
                    0b00000,
                    0b00111,
                    0b00100,
                    0b00110,
                    0b00100,
                    0b00000])


# Create Celsius  Degree Symbol
lcd.create_char(2, [0b11000,
                    0b11000,
                    0b00011,
                    0b00100,
                    0b00100,
                    0b00100,
                    0b00011,
                    0b00000])

# Define a way to poll the sensor
def update_temp(celsius):

    if celsius is False:
        return sensor.get_temperature(W1ThermSensor.DEGREES_F)
    elif celsius is True:
        return sensor.get_temperature(W1ThermSensor.DEGREES_C)


gpio.setup(relay_pin, GPIO.OUT)
# We're using Active Low
gpio.output(relay_pin, GPIO.HIGH)

# Start the PID
pid = PID.PID()
pid.SetPoint = target_temp

pid.setSampleTime(1)

# Start the rotary encoder
encoder1 = rotary_encoder.RotaryEncoder.Worker(rc1_a_pin, rc1_b_pin)
encoder1.start()

try:
    while 1:
        encoder1_delta = encoder1.get_delta()
        if encoder1_delta != 0:
            pid.SetPoint = (encoder1_delta * .25) + pid.SetPoint

        temp = update_temp(celsius_unit)
        pid.update(temp)
        output = pid.output
        if output >= 0:
            gpio.output(relay_pin, GPIO.HIGH)
            lcd.set_color(1.0, 0.0, 0.0)  # Red
        else:
            gpio.output(relay_pin, GPIO.LOW)
            lcd.set_color(0.0, 0.0, 1.0)  # Blue

        lcd.clear()
        lcd.message('TEMP:{0:0.1f}\x01  \nGOAL:{1:0.1f}\x01'.format(temp, pid.SetPoint))

        # Provide some feedback at the terminal level
        # print("PID OUTOUT IS: " + str(output) +
        #       "and the temperature is: " + str(round(temp, 1)))
except KeyboardInterrupt:
    gpio.output(relay_pin, GPIO.HIGH)
    lcd.clear()
    if plat is 5:
        import CHIP_IO.Utilities as UT
        UT.unexport_all()
    pass
