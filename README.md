PyDHT
=====

DHT 11 v.2 Temperature/Humidity GPIO driver.
Features
--------
* Temperature and humidity measurements
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
pip install pydht2
```

Usage
-----
You can specify board mode and data pin
By default board mode is BCM and pin = 4 GPIO
```
>>> import pydht
>>> pydht.get(board_mode='BCM', pin=4)
{'humidity': 33, 'temperature': 25}
```
