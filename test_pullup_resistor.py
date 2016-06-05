import CHIP_IO.GPIO as GPIO


GPIO.setup("XIO-P0", GPIO.IN)


GPIO.setup("XIO-P1", GPIO.IN)



#def readinput():
if GPIO.input("XIO-P0"):
  print(1)
else:
  print(0)
  
if GPIO.input("XIO-P1"):
  print(1)
else:
  print(0)
