import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.helios import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.extensions.led import LED


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[4],
        pins[5],
        pins[6],
        pins[7],
        pins[8],
        pins[9],
        pins[10],
    )
    row_pins = (
        pins[11],
        pins[12],
        pins[13],
        pins[14],
        pins[15],
        pins[16],
        pins[17],
        pins[18],
    )

    # fmt: off
    coord_mapping = [
        00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12,  13,
        14,  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        28,   29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,    40,
                42, 43, 44,   45,    46, 47, 48, 49, 50, 51, 52,
    ]
    # fmt: on

    diode_orientation = DiodeOrientation.COLUMNS

    leds = LED(led_pin=[board.GP17])
    _KMKKeyboard.extensions.append(leds)
