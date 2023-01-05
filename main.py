###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import time
import camera
import wlantest
import webtest
import upip
#import qrcode

try:
  import urequests as requests
except:
  import requests


def getPhoto():
    #camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    return camera.capture()

def printJpg(buf, name):
    pritn(buf)
    with open(name, "wb") as f:
        f.write(buf)
        
def getAvg(buf):
    num = 0
    sum = 0
    for byte in buf:
        sum = byte
        num += 1
    return num / sum

def lightOrDark(avg):
    if avg >= 48:
        return "Light"
    else:
        return "Dark"


def isItLightOrDark():
    return lightOrDark(int(getAvg(getPhoto())))
    
"""
--- Hell/ Dunkel Erkennung ---

print('Is it Dark or Light?')
camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
while True:
    print("checking ...")
    print(isItLightOrDark())
    time.sleep(3)

--- Display website ---
webtest.web(isItLightOrDark())

--- install requests ---
upip.install("micropython-urequests")
"""

wlantest.connwlan("","")
camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)

webtest.web("test")
