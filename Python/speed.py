# coding=utf8

from __future__ import division     # for python 2.x
import PyBearLibTerminal as blt
from time import time
import random

def get_shifted_color(shift):
    f = (shift % 80)  / 80
    r = g = b = 0

    if f < 0.33: # From red to green (through orange)
        r = 255 * (1 - 3*f)
        g = 255 * (3*f    )
    elif f < 0.67: # From green to blue (through cyan)
        g = 255 * (2 - 3*f)
        b = 255 * (3*f - 1)
    else: # From blue to red (through magenta)
        b = 255 * (3 - 3*f)
        r = 255 * (3*f - 2)

    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255

    return (int(r), int(g), int(b))

def get_highlighted_color(c):
    c = (min(ch*2, 255) for ch in c)
    return blt.color_from_argb(255, *c)

def color_from_another(alpha, base):
    return (base & 0x00FFFFFF) | (alpha << 24)

def test_speed():
    blt.set("window.title='Omni: syncronous rendering'")
    blt.composition(True)

    shift_b = shift_ff = 0

    shifted_b = [get_highlighted_color(get_shifted_color(i)) for i in range(80)]
    shifted_f = [color_from_another(100, shifted_b[i]) for i in range(80)]

    fps_update_time = time()
    fps_counter = fps_value = 0
    vsync = True

    random.seed()
    r0 = [random.randrange(256) for _ in range(2000)]

    proceed = True
    d = 128
    while proceed:
        r1 = random.randrange(256)
        alpha = blt.color_from_argb(d, 255, 255, 255)
        shift_f = int(shift_ff)
        blt.clear()
        for y in range(25):
            s1 = shift_b + y
            s2 = shift_f + y
            yy = y * 80
            for x in range(80):
                blt.color(shifted_b[(s1 + x) % 80])
                blt.put(x, y, 0x2588)
                blt.color(shifted_f[(s2 - x) % 80])
                blt.put(x, y, 0x2588)
                blt.color(alpha)
                blt.put(x, y, ord('0') + (r1 + r0[yy + x]) % 10)

        blt.print_(2, 1, "[color=black]vsync: %s\nFPS: %d" % ("yes" if vsync else "no", fps_value))
        blt.print_(2, 4, "[color=black]Press TAB to switch vsync on an off")
        blt.refresh()

        fps_counter += 1
        tm = time()
        if tm > fps_update_time + 1:
            fps_value = fps_counter
            fps_counter = 0
            fps_update_time = tm

        while proceed and blt.has_input():
            code = blt.read()
            if code in (blt.TK_ESCAPE, blt.TK_CLOSE):
                proceed = False
            elif code == blt.TK_TAB:
                vsync = not vsync
                blt.set("output.vsync=%s" % ("true" if vsync else "false"))

        shift_b += 1
        d = abs(-40 + shift_b % 80) * 128 // 40
        shift_ff -= 1.25

    blt.set("output.vsync=true")
    blt.composition(False)

if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_speed()
    blt.close()


























