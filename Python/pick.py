# coding=utf8

from __future__ import division
from random import seed, randrange, choice
from string import ascii_lowercase
from bearlibterminal import terminal as blt

def test_pick():
    blt.set("window.title='Omni: examining cell contents'")
    blt.set("input.filter={keyboard, mouse}")

    blt.clear()
    blt.color("white")
    blt.puts(2, 1, "Move mouse over characters:")

    blt.bkcolor("darkest gray")
    blt.clear_area(2, 3, 76, 19)
    blt.bkcolor("none")

    colors = ("red", "orange", "yellow", "green", "cyan", "light blue", "violet")
    combining = (0x02C6, 0x02C9, 0x02DC, 0x2014, 0x2044, 0x2017, 0x203E)

    seed()
    for i in range(100):
        combined = randrange(5) == 0
        n = randrange(2, 4) if combined else 1
        x = randrange(2, 78)
        y = randrange(3, 22)

        blt.color(choice(colors))
        blt.put(x, y, choice(ascii_lowercase))

        blt.composition(True)
        for i in range(1,n):
            blt.color(choice(colors))
            blt.put(x, y, choice(combining))
        blt.composition(False)

    blt.color("white")

    while True:
        x = blt.state(blt.TK_MOUSE_X)
        y = blt.state(blt.TK_MOUSE_Y)

        blt.clear_area(2, 23, 76, 1)
        if 2 <= x < 78 and 3 <= y < 22:
            n = 0

            while True:
                code = blt.pick(x, y, n)

                if code == 0: break

                color = blt.pick_color(x, y, n)
                blt.puts(2 + n * 2, 23, u"[color=#%x]%c" % (color, code))
                n += 1

            if n == 0:
                blt.puts(2, 23, "Empty cell")

        blt.refresh()

        key = blt.read();
        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

    blt.set("input.filter={keyboard}")


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_pick()
    blt.close()