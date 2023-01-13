import camera

def getPhoto():
    return camera.capture()
        
def getAvg(buf):
    num = 0
    sum = 0
    for byte in buf:
        sum = byte
        num += 1
    return num / sum

def lightOrDark(avg):
    if avg >= 48:
        return "hell"
    else:
        return "dunkel"


def isItLightOrDark():
    return lightOrDark(int(getAvg(getPhoto())))

def whatIsTheMainColor():
    res = "err"
    buf = getPhoto()
    red = 0
    green = 0
    blue = 0
    other = 0    
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
