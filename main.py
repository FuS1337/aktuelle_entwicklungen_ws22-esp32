###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import time
import camera
import wlantest
import webtest
import upip
import binascii
from machine import Pin

try:
  import urequests as requests
except:
  import requests


def getPhoto():
    return camera.capture()

def printJpg(buf, name):
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
    
def whatIsTheMainColor():
    res = "err"
    buf = getPhoto()
    
    red = 0
    green = 0
    blue = 0
    other = 0
    
    # pls give me more ram =(
    # print(hex(int.from_bytes(buf, "big")) & 0xFFFF)
    
    old = ""
    fst = True
    for i in buf[0:10000:1]:
        if fst:
            old = i
            fst = False
        else:
            pixel = (old << 8) + i
            fst = True
            r = (pixel & 0b1111100000000000) >> 8
            g = (pixel & 0b11111000000) >> 3
            b = (pixel & 0b11111) << 3
            if r > g and r > b:
                red += 1
            elif g > r and g > b:
                green+= 1
            elif b > r and b > g:
                blue += 1
            else:
                other += 1
    if ((red > green) & (red > blue) & (red > other)):
        res = "red"
    elif ((green > red) & (green > blue) & (green > other)):
        res = "green"
    elif ((blue > red) & (blue > green) & (blue > other)):
        res = "blue"
    else:
        res = "other"
    return res
    
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

--- start Webservice ---
     webtest.web("test")
"""

def init():
    wlantest.connwlan("","")
    # format=camera.JPEG
    camera.init(0, format=camera.RGB565, fb_location=camera.PSRAM)

if __name__ == "__main__":
     init()
     webtest.web(whatIsTheMainColor())
