import CHIP_IO.GPIO as GPIO


GPIO.setup("XIO-P0", GPIO.IN)
GPIO.setup("XIO-P0", GPIO.HIGH)

GPIO.setup("XIO-P1", GPIO.IN)
GPIO.setup("XIO-P1", GPIO.HIGH)


while 1==1 :
  if GPIO.input("XIO-P0"):
    print(1)
  else:
    print(0)
  
  if GPIO.input("XIO-P1"):
    print(1)
  else:
    print(0)
