try:
  import usocket as socket
except:
  import socket
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

# Funktion um Wlanverbindungen herzustellen
#   ssid     - Wlanname
#   password - Passwort für das Wlan
def connwlan(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
      pass
    print('Connection successful')
    print(station.ifconfig())

