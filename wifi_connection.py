import gc

import esp
import network

try:
    import usocket as socket
except ImportError:
    import socket

esp.osdebug(None)

gc.collect()


def wifi_connect(ssid, password):
    """ Funktion um WLAN-Verbindungen herzustellen

    :param ssid: SSID des WLANs bzw. Name
    :param password: Passwort für das WLAN
    """

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass

    print('Connection successful')
    print(f'Config: {station.ifconfig()}')

