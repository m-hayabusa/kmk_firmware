from keyboard.hardware import KMKKeyboard
from kmk.extensions.lock_status import LockStatus


class LEDLockStatus(LockStatus):
    def __init__(self, keyboard: KMKKeyboard):
        super().__init__()
        self.keyboard = keyboard

    def set_lock_leds(self):
        if self.get_caps_lock():
            self.keyboard.leds.set_brightness(50, leds=[0])
        else:
            self.keyboard.leds.set_brightness(0, leds=[0])

    def after_hid_send_initialize(self, sandbox):
        super().after_hid_send(sandbox)
        self.set_lock_leds()
        self.after_hid_send = self.after_hid_send_main

    def after_hid_send_main(self, sandbox):
        super().after_hid_send(sandbox)
        if self.report_updated:
            self.set_lock_leds()

    after_hid_send = after_hid_send_initialize
