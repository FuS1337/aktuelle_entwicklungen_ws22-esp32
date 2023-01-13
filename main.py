###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import webtest
import camera

COLORNOTLIGHTDARK = True

if __name__ == "__main__":
    if COLORNOTLIGHTDARK:
        camera.init(0, format=camera.RGB565, fb_location=camera.PSRAM)
        webtest.web("Folgende Farbe wird erkannt: ", COLORNOTLIGHTDARK)
    else:
        camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
        webtest.web("Ist es hell oder dunkel: ", COLORNOTLIGHTDARK)
