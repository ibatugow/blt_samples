# coding=utf8

from __future__ import division

from ctypes import c_uint32, addressof
from bearlibterminal import terminal as blt

def test_layers():
    blt.set("window.title='Omni: layers'")

    pixel = c_uint32(blt.color_from_name("dark gray"))

    blt.set("U+E000: %d, raw-size=1x1, resize=48x48, resize-filter=nearest" % addressof(pixel))

    blt.clear()
    blt.color("white")

    blt.puts(2, 1, "[color=orange]1.[/color] Without layers:")
    blt.put(7, 3, 0xE000)   
    blt.puts(5, 4, "[color=dark green]abcdefghij")

    blt.puts(2, 8, "[color=orange]2.[/color] With layers:")
    blt.layer(1)
    blt.put(7, 10, 0xE000)
    blt.layer(0)
    blt.puts(5, 11, "[color=dark green]abcdefghij")

    blt.refresh()

    key = None
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE):
        key = blt.read()

    blt.set("U+E000: none")


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_layers()
    blt.close()