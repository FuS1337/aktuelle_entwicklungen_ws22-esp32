# This file is executed on every boot (including wake-boot from deepsleep)
import wifi_connection

SSID = "WLAN-NAME"
WIFI_PW = "WLAN-PASSWORT"

# mit Wlan verbinden
wifi_connection.wifi_connect(SSID, WIFI_PW)
