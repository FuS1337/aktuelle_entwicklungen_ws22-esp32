import camera


def capture_image():
    """ Nimmt ein Bild auf und returnt es """
    return camera.capture()


def get_image_average(buf):
    """ Berechnet Durchschnitt eines Bildes

    :param buf: Bild Bytes
    :return: Durchschnitt des Bildes ueber bytes
    """

    bytes_count = 0
    bytes_sum = 0
    for cur_byte in buf:
        bytes_sum = cur_byte
        bytes_count += 1

    return bytes_count / bytes_sum


def is_it_light_or_dark(light_threshold=48):
    """ Nimmt ein Bild auf und entscheidet, ob es hell oder dunkel ist.

    :param light_threshold: Threshold ab dem ein Wert als Hell gilt
    :return: "hell" oder "dunkel"
    """

    image_bytes_avg = get_image_average(capture_image())
    if image_bytes_avg >= light_threshold:
        return "hell"
    else:
        return "dunkel"


def get_current_main_color():
    """ Farberkennung
    macht Foto, berechnet fuer einige Pixel, wie viel Rot/Gruen/Blau/ was anderes sind

    :return: gibt rot/ gruen/ blau/ andere Farbe aus
    """

    buf = capture_image()
    red_count = 0
    green_count = 0
    blue_count = 0
    other_count = 0
    byte_1 = 0
    at_first_byte = True

    for cur_byte in buf[0:10_000]:
        if at_first_byte:
            byte_1 = cur_byte
            at_first_byte = False
        else:
            pixel = (byte_1 << 8) + cur_byte
            at_first_byte = True

            r = (pixel & 0b11111000_00000000) >> 8
            g = (pixel & 0b00000111_11000000) >> 3
            b = (pixel & 0b00000000_00011111) << 3

            if r > g and r > b:
                red_count += 1
            elif g > r and g > b:
                green_count += 1
            elif b > r and b > g:
                blue_count += 1
            else:
                other_count += 1

    if (red_count > green_count) and (red_count > blue_count) and (red_count > other_count):
        res = "rot"
    elif (green_count > red_count) and (green_count > blue_count) and (green_count > other_count):
        res = "gruen"
    elif (blue_count > red_count) and (blue_count > green_count) and (blue_count > other_count):
        res = "blau"
    else:
        res = "andere Farbe"

    return res

