# coding=utf8

from __future__ import division

import PyBearLibTerminal as blt
from math import pi, sin, cos

def test_extended_basics():
    # Setup
    blt.set("window.title='Omni: extended output / basics'")
    blt.set("0xE000: ../Media/Tiles.png, size=32x32, align=top-left")
    blt.composition(True)

    cx, cy = 10, 5
    n_symbols = 10
    radius = 5
    angle = 0.0
    fps = 25
    transparent, opaque = 0x00FFFFFF, 0xFFFFFFFF

    m00 = [0xFFFF0000, 0xFF00FF00, 0xFF0000FF, 0xFFFFFF00]
    m01 = [opaque, opaque, transparent, transparent]

    m11 = [transparent, transparent, opaque, transparent]
    m12 = [transparent, opaque, transparent, transparent]
    m21 = [transparent, transparent, transparent, opaque]
    m22 = [opaque, transparent, transparent, transparent]

    while True:
        blt.clear()
        blt.color("white")

        blt.print_(2, 1, "[color=orange]1.[/color] put_ext(x, y, [color=orange]dx[/color], [color=orange]dy[/color], code)")
        for i in range(n_symbols):
            angle_delta = 2 * pi / n_symbols
            dx = cos(angle + i * angle_delta) * radius * blt.state(blt.TK_CELL_WIDTH)
            dy = sin(angle + i * angle_delta) * radius * blt.state(blt.TK_CELL_WIDTH) - 4
            blt.color("white" if i > 0 else "orange")
            blt.put_ext(cx, cy, int(dx), int(dy), ord('a')+i)

        angle += 2 * pi / (2 * fps)

        blt.print_(2, 9, "[color=orange]2.[/color] put_ext(x, y, dx, dy, code, [color=orange]corners[/color])")
        blt.put_ext(5, 11, 0, 0, 0xE000+19, m00)
        blt.put_ext(10, 11, 0, 0, 0xE000+19, m01)

        blt.print_(2, 14, "[color=orange]3.[/color] put_ext + composition")
        x1 = 5
        y1 = 16
        blt.put(x1+0, y1+0, 0xE000+19)
        blt.put(x1+0, y1+2, 0xE000+8)
        blt.put(x1+5, y1+0, 0xE000+19)
        blt.put(x1+9, y1+0, 0xE000+19)
        blt.put(x1+5, y1+2, 0xE000+19)
        blt.put(x1+9, y1+2, 0xE000+19)
        blt.put_ext(x1+5, y1+0, 0, 0, 0xE000+8, m11)
        blt.put_ext(x1+9, y1+0, 0, 0, 0xE000+8, m12)
        blt.put_ext(x1+5, y1+2, 0, 0, 0xE000+8, m21)
        blt.put_ext(x1+9, y1+2, 0, 0, 0xE000+8, m22)

        blt.refresh()

        if blt.has_input():
            key = blt.read()
            if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
                break

        blt.delay(1000 // fps)

    # Clean up
    blt.composition(False)
    blt.set("0xE000: none")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_extended_basics()
    blt.close()