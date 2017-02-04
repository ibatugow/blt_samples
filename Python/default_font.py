# coding=utf8

from bearlibterminal import terminal as blt
from wgl4 import wgl4_ranges, wgl4_set

def test_default_font():
    blt.set("window: size=80x25, cellsize=auto, title='Omni: WGL4'; font=default")

    hoffset = 40
    current_range = 0

    while True:
        blt.clear()
        blt.puts(2, 1, "[color=white]Select unicode character range:")

        for i, r in enumerate(wgl4_ranges):
            selected = i == current_range
            blt.color("orange" if selected else "light_gray")
            blt.puts(1, 2 + i, "%s%s" % ("[U+203A]" if selected else " ", r.name))

        r = wgl4_ranges[current_range]
        for j in range(16):
            blt.puts(hoffset + 6 + j * 2, 1, "[color=orange]%X" % j)

        y = 0
        for code in range(r.start, r.end + 1):
            if code % 16 == 0: blt.puts(hoffset, 2 + y, "[color=orange]%04X:" % code)

            blt.color("white" if code in wgl4_set else "dark gray")
            blt.put(hoffset + 6 + (code % 16) * 2, 2 + y, code)

            if (code+1) % 16 == 0: y += 1

        blt.color("white")
        blt.puts(hoffset, 20, "[color=orange]TIP:[/color] Use ↑/↓ keys to select range")
        blt.puts(hoffset, 22, "[color=orange]NOTE:[/color] Character code points printed in\ngray are not included in the WGL4 set.")

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break
        elif key == blt.TK_UP:
            if current_range > 0: current_range -= 1
        elif key == blt.TK_DOWN:
            if current_range < len(wgl4_ranges)-1: current_range += 1

if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_default_font()
    blt.close()