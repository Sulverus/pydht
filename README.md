PyDHT
=====

DHT 11 v.2 Temperature/Humanity GPIO driver.
Features
--------
* Temperature and humanity mesurements
* BCM and breadboard modes support(not tested in breadboard)
* Check sum confirmation

requirements
------------
dht11 driver requires RPi.GPIO library

plug and install
----------------
1. Plug dht 11 into raspberry pi(VCC to 5v pin, GROUND to GND). For data pin you can use any GPIO data pin
Offical datasheets: http://www.dfrobot.com/wiki/index.php/DHT11_Temperature_and_Humidity_Sensor_V2_SKU:_DFR0067
2. Install pydht 
```
pip install pydht
```

usage
-----
You can specify boadrd mode and data pin
By default boadr mode is BCM and pin = 4 GPIO
```
>>> import pydht
>>> pydht.get(board_mode='BCM', pin=4)
{'humanity': 33, 'temperature': 25}
```
