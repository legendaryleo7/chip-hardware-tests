# chip-hardware-tests

This is just a series of tests to test different peripherals on the CHIP.

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

