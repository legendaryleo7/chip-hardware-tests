
# Multi Platform Sous Vide



#Prerequisites

<a href="https://github.com/xtacocorex/Adafruit_Python_GPIO">Adafruit GPIO Library</a>

````
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/xtacocorex/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
````

ivPID
https://github.com/ivmech/ivPID

DS18b20 Library
https://github.com/timofurrer/w1thermsensor

Adafruit Python CharLCD Library
https://github.com/adafruit/Adafruit_Python_CharLCD

# Additional Prerequisites for Raspberry Pi
<a href="https://pypi.python.org/pypi/RPi.GPIO">RPi.GPIO</a>
````
sudo apt-get update
sudo apt-get install -y python3 python3-pip python-dev
sudo pip3 install rpi.gpio
````
# Additional Prerequisites for BeagleBone Black
<a href="https://pypi.python.org/pypi/Adafruit_BBIO">Adafruit_BBIO</a>
````
sudo ntpdate pool.ntp.org
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip -y
#easy_install -U distribute //debian only
sudo pip install Adafruit_BBIO
````

# Additional Prerequisites for CHIP
<a href="https://github.com/xtacocorex/CHIP_IO">CHIP_IO</a>

````
sudo ntpdate pool.ntp.org
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip -y
git clone git://github.com/xtacocorex/CHIP_IO.git
cd CHIP_IO
sudo python setup.py install
cd ..
sudo rm -rf CHIP_IO
````

#Usage

`````
sudo modprobe w1_therm
sudo python sous-vide-multi-platform.py

``````
