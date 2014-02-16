PyDHT
=====

DHT 11 v.2 Temperature/Humanity GPIO driver.
Features
--------
* Temperature and humanity mesurements
* BCM and breadboard modes support(not tested in breadboard)
* Check sum confirmation

Requirements
------------
dht11 driver requires RPi.GPIO library

Plug and install
----------------
1. Plug dht 11 into raspberry pi(VCC to 5v pin, GROUND to GND). For data pin you can use any GPIO data pin
Offical datasheets: http://www.dfrobot.com/wiki/index.php/DHT11_Temperature_and_Humidity_Sensor_V2_SKU:_DFR0067
2. Install pydht 
```
pip install pydht
```

Usage
-----
You can specify board mode and data pin
By default board mode is BCM and pin = 4 GPIO
```
>>> import pydht2
>>> pydht.get(board_mode='BCM', pin=4)
{'humanity': 33, 'temperature': 25}
```
