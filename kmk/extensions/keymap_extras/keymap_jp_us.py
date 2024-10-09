try:
    from typing import Optional
except ImportError:
    pass

from keyboard.hardware import KMKKeyboard
from kmk.keys import KC, Key, KeyboardKey, ModifierKey

shifted = set()

class ShiftKey(ModifierKey):
    def __init__(
        self,
        key: Key
    ):
        self.code = key.code

    def on_press(self, keyboard: KMKKeyboard, coord_int: Optional[int] = None) -> None:
        keyboard.hid_pending = True
        keyboard.keys_pressed.add(self)
        shifted.add(self)

    def on_release(self, keyboard: KMKKeyboard, coord_int: Optional[int] = None) -> None:
        keyboard.hid_pending = True
        keyboard.keys_pressed.discard(self)
        shifted.discard(self)

class ShiftedKey(KeyboardKey):
    def __init__(
        self,
        keyOnBase: Key,
        keyOnShift: Key,
    ):
        self._baseShifted = False
        self._shiftShifted = False
    
        if not hasattr(keyOnBase, "code") or keyOnBase.code == -1:
            self._baseShifted = True
            self._base = keyOnBase.key.code
        else:
            self._base = keyOnBase.code

        if not hasattr(keyOnShift, "code") or keyOnShift.code == -1:
            self._shiftShifted = True
            self._shifted = keyOnShift.key.code
        else:
            self._shifted = keyOnShift.code
        
        self.code = self._base 

    def on_press(self, keyboard: KMKKeyboard, coord_int: Optional[int] = None) -> None:
        if len(shifted) > 0:
            if hasattr(self, "_shifted"):
                self.code = self._shifted
            if not self._shiftShifted:
                for shiftkey in shifted:
                    keyboard.keys_pressed.discard(shiftkey)
        else:
            if hasattr(self, "_shifted"):
                self.code = self._base
            if self._baseShifted:
                keyboard.keys_pressed.add(KC.LSFT)
                
        keyboard.keys_pressed.add(self)
        keyboard.hid_pending = True

    def on_release(self, keyboard: KMKKeyboard, coord_int: Optional[int] = None) -> None:
        keyboard.hid_pending = True
        keyboard.keys_pressed.discard(self)

        if self._baseShifted and not KC.LSFT in shifted:
            keyboard.keys_pressed.discard(KC.LSFT)

        if len(shifted) > 0:
            for shiftkey in shifted:
                keyboard.keys_pressed.add(shiftkey)


KC.LSFT = ShiftKey(KC.LSFT)
KC.RSFT = ShiftKey(KC.RSFT)

KC.N2 = ShiftedKey(KC.N2, KC.DOUBLE_QUOTE)
KC.N6 = ShiftedKey(KC.N6, KC.AMPERSAND)
KC.N7 = ShiftedKey(KC.N7, KC.QUOTE)
KC.N8 = ShiftedKey(KC.N8, KC.LEFT_PAREN)
KC.N9 = ShiftedKey(KC.N9, KC.RIGHT_PAREN)
KC.N0 = ShiftedKey(KC.N0, KC.N0)
KC.MINS = ShiftedKey(KC.MINS, KC.EQUAL)
KC.CIRC = ShiftedKey(KC.CIRC, KC.TILDE)
KC.AT = ShiftedKey(KC.AT, KC.GRAVE)
KC.SCLN = ShiftedKey(KC.SCOLON, KC.PLUS)
KC.COLN = ShiftedKey(KC.COLON, KC.ASTERISK)
KC.BSLS = ShiftedKey(KC.BSLS, KC.UNDERSCORE)
