# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt

def test_window_resize():
    blt.set("window: title='Omni: window resizing', resizeable=true, minimum-size=27x5")

    symbol = 0x2588

    while True:
        blt.clear()
        w = blt.state(blt.TK_WIDTH)
        h = blt.state(blt.TK_HEIGHT)
        for x in range(w):
            blt.put(x, 0, symbol if x % 2 else '#')
            blt.put(x, h - 1, symbol if x % 2 else '#')
        for y in range(h):
            blt.put(0, y, symbol if y % 2 else '#')
            blt.put(w - 1, y, symbol if y % 2 else '#')
        blt.puts(3, 2, "Terminal size is %dx%d" % (w, h))
        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

    blt.set("window: resizeable=false")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_window_resize()
    blt.close()