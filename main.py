###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import camera

import camera_functions
import webserver


class OperationDefinition:
    camera_params = None
    text = None
    operation = None

    def __init__(self, camera_params, text, operation):
        self.camera_params = camera_params
        self.text = text
        self.operation = operation


class Operations:
    """ Enum der angebotenen Funktionalitäten """
    COLOR = OperationDefinition(
        camera_params={
            "format": camera.RGB565,
            "fb_location": camera.PSRAM
        },
        text="Folgende Farbe wird erkannt: ",
        operation=camera_functions.get_current_main_color
    )
    LIGHT_OR_DARK = OperationDefinition(
        camera_params={
            "format": camera.JPEG,
            "fb_location": camera.PSRAM
        },
        text="Im Bild ist es aktuell ",
        operation=camera_functions.is_it_light_or_dark
    )


OPERATION_TO_DO = Operations.LIGHT_OR_DARK
""" Entscheidet mit welcher funktionalität der Server laufen soll. """


def main():
    """ Startet den Webserver und legt fest ob Farben-Erkennung oder Hell-Dunkel-Erkennung genutzt werden soll """

    # Initialise Camera
    camera.init(0, **OPERATION_TO_DO.camera_params)
    # Start Server in endless loop
    webserver.start_webserver(OPERATION_TO_DO.text, OPERATION_TO_DO.operation)


if __name__ == "__main__":
    main()

