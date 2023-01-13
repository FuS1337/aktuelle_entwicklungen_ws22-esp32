# This file is executed on every boot (including wake-boot from deepsleep)
import wlantest

wlantest.connwlan("WLAN-NAME","WLAN-PASSWORT")
