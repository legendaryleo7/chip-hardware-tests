# chip-vide



#Prerequisites

<a href="https://github.com/xtacocorex/Adafruit_Python_GPIO">Adafruit GPIO Library</a>

````
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
````

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

Gaugette
https://github.com/legendaryleo7/py-gaugette/tree/CHIP-support

ivPID
https://github.com/ivmech/ivPID

DS18b20 Library
https://github.com/timofurrer/w1thermsensor

Adafruit Python CharLCD Library
https://github.com/adafruit/Adafruit_Python_CharLCD


