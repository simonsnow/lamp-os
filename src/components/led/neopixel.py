'''
NeoPixel driver based on the NeoPixel driver in MicroPython
Adds better support for RGB(W) types and for working with the
color types in this lib
'''
from machine import bitstream, Pin

class ColorOrder:
    GRBW = (1, 0, 2, 3)

class NeoPixel:
    TIMING_800kHz = (400, 850, 800, 450)
    TIMING_400hKz = (800, 1700, 1600, 900)

    def __init__(self, pin, n, bpp=4, color_order = ColorOrder.GRBW, timing=TIMING_800kHz):
        self.pin = Pin(pin)
        self.pin.init(self.pin.OUT)
        self.n = n
        self.bpp = bpp
        self.timing = timing
        self.color_order = color_order

    # send bitmap to the led strip
    def write(self, data):
        if self.bpp == 3:
            bitstream(self.pin, 0, self.timing, bytearray([int(item) for t in [(int(g), int(r), int(b)) for r, g, b, _ in data] for item in t]))
        else:
            bitstream(self.pin, 0, self.timing, bytearray([int(item) for t in [(int(g), int(r), int(b), int(w)) for r, g, b, w in data] for item in t]))
