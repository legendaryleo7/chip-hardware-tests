<<<<<<< HEAD
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

<a href="https://github.com/legendaryleo7/py-gaugette/tree/CHIP-support">Gaugette</a>
````
git clone -b CHIP-support https://github.com/legendaryleo7/py-gaugette.git
cd CHIP-support
sudo python setup.py install
````


ivPID
https://github.com/ivmech/ivPID

DS18b20 Library
https://github.com/timofurrer/w1thermsensor

Adafruit Python CharLCD Library
https://github.com/adafruit/Adafruit_Python_CharLCD

#Usage
chip-vide-simple.py

This script will print the PID value and current temperature every 5 seconds. It will also set the GPIO pin to HIGH to turn off the relay, and to LOW to turn it on as mandated by the PID output.
`````
sudo modprobe w1_therm
#Control-C out of this command if it hangs. It should still work.
sudo python chip-vide-simple.py
#Enter a target temperature
``````

=======
# chip-vide

This is a multi-platform Sous Vide script that utilizes the Adafruit Python GPIO Library. 


#Prerequisites

<a href="https://github.com/xtacocorex/Adafruit_Python_GPIO">Adafruit GPIO Library</a>

````
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/xtacocorex/Adafruit_Python_GPIO.git
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

<a href="https://github.com/timofurrer/w1thermsensor">W1ThermSensor</a>
````
pip install w1thermsensor
````

ivPID
https://github.com/ivmech/ivPID

Adafruit Python CharLCD Library
https://github.com/adafruit/Adafruit_Python_CharLCD

#Usage
chip-vide-simple.py

This script will print the PID value and current temperature every 5 seconds. It will also set the GPIO pin to HIGH to turn off the relay, and to LOW to turn it on as mandated by the PID output.
`````
sudo modprobe w1_therm
#Control-C out of this command if it hangs. It should still work.
sudo python chip-vide-simple.py
#Enter a target temperature
``````

>>>>>>> 71e9c51131eb101002e66820b90d6157b3100a38
