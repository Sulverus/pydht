#coding: utf-8
import RPi.GPIO as GPIO
from time import sleep

TIMELIMIT = 20

class DHTException(Exception):
  pass

def get(**kwargs):
  """
  Safe sensor wrapper
  """
  sensor = None
  tick = 0
  driver = DHTReader(**kwargs)
  while not sensor and tick < TIMELIMIT:
    try:
      sensor = driver.receive_data()
    except DHTException:
      tick += 1
  return sensor

class DHTReader(object):
  """
  DHT T/H 11 v2 sensor GPIO driver
  """
  MODES = {'BCM': GPIO.BCM, 'BOARD': GPIO.BOARD}

  MAX_TICK = 100
  CONFIRM_TICK = 2
  CONFIRM_MAX = 10
  PREPARE_TICKS = 3
  READ_BITS = 1000
  
  OFFSET_TEMP = 2
  OFFSET_HUM = 0
  OFFSET_CHECK = 4

  def __init__(self, board_mode='BCM', pin=4):
    """
    Set board and  pin mode
    """
    if board_mode in self.MODES:
      self.run_mode = self.MODES[board_mode]
    else:
      raise DHTException('%s - Unknown board mode.' % board_mode)
    GPIO.setmode(self.run_mode)
    self.pin = pin

  def next_bit(self, buffer):
    """
    Get next bit for processing
    """
    value = buffer[0]
    del buffer[0]
    return value

  def process_bits(self, input_data):
    data = [0] * self.MAX_TICK
    j = 0
    state = 1
  
    #Drop high signals
    while state:
      state = self.next_bit(input_data)

    state = 1
    for i in xrange(0, self.MAX_TICK):
      cnt = 0
      while self.next_bit(input_data) == state:
        cnt += 1
        if cnt == self.CONFIRM_MAX:
          break

      state = self.next_bit(input_data)

      if cnt == self.CONFIRM_MAX:
        break

      if i > self.PREPARE_TICKS and  i % 2 == 0:
        data[j/8] <<= 1
        if cnt > self.CONFIRM_TICK:
          data[j/8] |= 1
        j+=1
    return data

  def micro_sleep(self, ticks):
    sleep(ticks/1000.0)

  def receive_data(self):
    #Set ouput, send high signal and wait for init
    GPIO.setup(self.pin, GPIO.OUT)
    GPIO.output(self.pin, GPIO.HIGH)
    self.micro_sleep(500)

    #Send low signal, wait for init and set pin in input mode
    GPIO.output(self.pin, GPIO.LOW)
    self.micro_sleep(10)
    GPIO.setup(self.pin, GPIO.IN)

    #Fast read all data input
    input_data = [GPIO.input(self.pin) for x in xrange(0, self.READ_BITS)]
    GPIO.cleanup()
  
    #Process recieved data
    data = self.process_bits(input_data)

    #Verify check sum and return sensors data
    if sum(data[0:self.OFFSET_CHECK - 1]) & 0xFF != data[self.OFFSET_CHECK] or not any(data):
      raise DHTException('Wrong check sum')
    return {'humanity': data[self.OFFSET_HUM], 'temperature': data[self.OFFSET_TEMP]}
