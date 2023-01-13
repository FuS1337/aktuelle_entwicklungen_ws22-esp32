import camera

# Funktion, die ein Foto zurückliefert
def getPhoto():
    return camera.capture()

# Berechent Druchschnitt eines Bildes
#   buf - Foto
def getAvg(buf):
    num = 0
    sum = 0
    for byte in buf:
        sum = byte
        num += 1
    return num / sum

# Entscheidet anhand der Durchnitts ob es hell oder dunkel ist
#   avg - Durchschnitt deines Fotos (aus getAvg)
def lightOrDark(avg):
    if avg >= 48:
        return "hell"
    else:
        return "dunkel"

# Funktion, die die Hell Dunkel Erkennung realisiert
#   liefert hell oder dunkel
def isItLightOrDark():
    return lightOrDark(int(getAvg(getPhoto())))

# Farberkennung
#   macht Foto, berechnet für einige Pixel, wie viel Rot/Grün/Blau/ was anderes sind
#   gibt rot/ grün/ blau/ andere Farbe aus
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
        res = "rot"
    elif ((green > red) & (green > blue) & (green > other)):
        res = "grün"
    elif ((blue > red) & (blue > green) & (blue > other)):
        res = "blau"
    else:
        res = "andere Farbe"
    return res
