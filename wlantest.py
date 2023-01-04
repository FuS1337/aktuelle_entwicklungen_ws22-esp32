try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

def connwlan(ssid, password):
    #ssid = 'GWH.TEL-SM1T6X8K'
    station = network.WLAN(network.STA_IF)
    #print(station.scan())

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
      pass

    print('Connection successful')
    print(station.ifconfig())

    led = Pin(2, Pin.OUT)
