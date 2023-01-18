import gc

import esp
import network

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
    print(f'Listening on: {station.ifconfig()[0]}')
