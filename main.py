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
    
    print(buf[0:500])
    print("------------")
    
    #  rgb(255,0,255)
    # 31 << 11 | 0 << 5 | 0 << 0    -> 63488
    # That is 5 bits for red, 6 bits for green, 5 bits for blue
    #  a = 31 << 11 | 0 << 5 | 0 << 0
    #get rgb565 Picture
    
    red = 0
    green = 0
    blue = 0
    other = 0
    for pixel in picture:
        if pixel <= 0x52BF and pixel >= 0x000C 
            blue += 1
        elif pixel <= 0xB7EF and pixel >= 0x01C0
            green += 1
        elif pixel <= 0xF9A6 and pixel >= 0xA000
            red += 1
        else:
            other += 1
    
    if ((red > green) & (red  blue) & (red > other)):
        res = "red"
    elif ((green > red) & (green > blue) & (green > other)):
        res = "green"
    elif ((blue > red) & (blue > green) & (blue > other)):
        res = "green"
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
