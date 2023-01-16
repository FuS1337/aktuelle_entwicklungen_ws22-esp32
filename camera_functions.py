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


def get_pixels_from_bytes(buf):
    """ Generator for fetching pixels from image bytes.
    Combines two bytes into a pixel and returns every fourth pixel.

    :param buf: Image as Bytes
    :return: Iterable of 16-Bit Pixels
    """

    counter = 0
    acc = None
    for cur_byte in buf:
        if counter == 0:
            acc = cur_byte
            counter += 1
        elif counter == 1:
            yield (acc << 8) | cur_byte
            counter += 1
        elif counter == 7:
            counter = 0
        else:
            counter += 1


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

    for cur_pixel in get_pixels_from_bytes(buf):  # total of 307_200 Bytes / 153_600 Pixels
        r = (cur_pixel & 0b11111000_00000000) >> 8
        g = (cur_pixel & 0b00000111_11000000) >> 3
        b = (cur_pixel & 0b00000000_00011111) << 3

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
