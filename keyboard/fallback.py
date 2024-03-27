print("Fallback!\n")

from kmk.keys import KC
from kmk.extensions.led import AnimationModes
from kmk.extensions.keymap_extras.keymap_jp import *
from kmk.modules.layers import Layers
from keyboard.hardware import KMKKeyboard

keyboard = KMKKeyboard()
keyboard.debug_enabled = False
keyboard.modules.append(Layers())

_______ = KC.TRANSPARENT
XXXXXXX = KC.NO

KC.AT = KC.LBRC
KC.LBRC = KC.RBRC
KC.COLN = KC.QUOT
KC.RBRC = KC.NUHS
KC.ZNHN = KC.TILD
KC.CIRC = KC.EQUAL
KC.TILD = KC.RSFT(KC.CIRC)
KC.PIPE = KC.RSFT(KC.JYEN)

FN_L = KC.MO(1)
FN_R = KC.MO(2)
FN_2 = KC.MO(3)

# fmt: off
keyboard.keymap = [
    [
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,     KC.AT,   KC.LBRC,  KC.BSPC,
        KC.LCTL,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.COLN, KC.RBRC, KC.ENT,
        KC.LSFT,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RO,          KC.RSFT,
                        KC.LALT, KC.LGUI, FN_L,         KC.SPC,         FN_R,    KC.PSCR, KC.RALT, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
    ],
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.CIRC,  KC.DEL, 
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.PIPE,        _______,
                        _______, KC.ZNHN ,FN_L,         _______,        FN_2,    _______, _______, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.CIRC,  KC.DEL, 
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.PIPE,        _______,
                        _______, KC.ZNHN ,FN_2,         _______,        FN_R,    _______, _______, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
    [
        KC.TILD, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,   KC.DEL, 
        KC.CAPS,  _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,        _______,
                        _______, _______, _______,      _______,        _______,KC.RESET, _______, _______, _______, _______, _______,
    ]
]
# fmt: on

try:
    keyboard.leds.animation_mode = AnimationModes.BREATHING
    keyboard.leds.animation_speed = 1
    keyboard.leds.breathe_center = 1.5
except Exception as e:
    print(e)

if __name__ == "__main__":
    keyboard.go()
