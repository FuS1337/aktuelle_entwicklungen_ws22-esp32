# This file is executed on every boot (including wake-boot from deepsleep)
import wlantest
# mit Wlan verbinden
wlantest.connwlan("WLAN-NAME","WLAN-PASSWORT")
