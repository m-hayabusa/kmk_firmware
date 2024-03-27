import digitalio
import board
import time
from kmk.bootcfg import bootcfg
from kmk.quickpin.pro_micro.helios import pinout as pins

testmode = True

input = digitalio.DigitalInOut(pins[17])
for pin in [6, 8]:
    key = digitalio.DigitalInOut(pins[pin])
    key.direction = digitalio.Direction.OUTPUT
    key.value = True
    time.sleep(0.01)
    testmode = testmode and input.value
    key.value = False
input.deinit()

testmode = testmode or digitalio.DigitalInOut(board.GP11).value


class always:
    value = True


bootcfg(
    sense=always,
    storage=testmode,
    cdc=testmode,
    consumer_control=False,
    keyboard=True,
    midi=False,
    mouse=False,
    nkro=False,
    pan=False,
)
