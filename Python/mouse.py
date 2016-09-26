# coding=utf8

from __future__ import division

from collections import namedtuple
import PyBearLibTerminal as blt

class Rect(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __contains__(self, pos):
        x,y = pos
        return self.x <= x <= self.x + self.width and \
               self.y <= y <= self.y + self.height

    def fill(self, c = 0x2588):
        for i in range(self.x, self.x + self.width + 1):
            for j in range(self.y, self.y + self.height + 1):
                blt.put(i, j, c)


double_click_area = Rect(1, 11, 17, 4)

def test_mouse():
    blt.set("window.title='Omni: mouse input'")
    blt.set("input.filter={keyboard, mouse+}")
    blt.composition(True)

    precise_mouse = False
    cursor_visible = True
    mlx = -1; mly = -1
    mrx = -1; mry = -1
    scroll = 0
    plate = False

    # Flush input
    while blt.has_input():
        blt.read()

    counter = 0

    proceed = True
    while proceed:
        blt.clear()

        blt.color("white")
        blt.print_(1, 1, "Received [color=orange]%d[/color] %s" % (counter, "event" if counter == 1 else "events"))

        blt.color("white")
        blt.print_(
            1, 3,
            "Buttons: "
            "[color=%s]left "
            "[color=%s]middle "
            "[color=%s]right "
            "[color=%s]x1 "
            "[color=%s]x2 " % (
                "orange" if blt.state(blt.TK_MOUSE_LEFT) else "dark gray",
                "orange" if blt.state(blt.TK_MOUSE_MIDDLE) else "dark gray",
                "orange" if blt.state(blt.TK_MOUSE_RIGHT) else "dark gray",
                "orange" if blt.state(blt.TK_MOUSE_X1) else "dark gray",
                "orange" if blt.state(blt.TK_MOUSE_X2) else "dark gray"))

        n = blt.print_(
            1, 4,
            "Cursor: [color=orange]%d:%d[/color] [color=dark gray]cells[/color]"
            ", [color=orange]%d:%d[/color] [color=dark gray]pixels[/color]" % (
                blt.state(blt.TK_MOUSE_X),
                blt.state(blt.TK_MOUSE_Y),
                blt.state(blt.TK_MOUSE_PIXEL_X),
                blt.state(blt.TK_MOUSE_PIXEL_Y)))

        blt.print_(
            1, 5,
            "Wheel: [color=orange]%d[/color] [color=dark gray]delta[/color]"
            ", [color=orange]%d[/color] [color=dark gray]cumulative" % (
                blt.state(blt.TK_MOUSE_WHEEL), scroll))

        blt.print_(
            1, 7, "[color=%s][U+25CF][/color] Precise mouse movement" % ("orange" if precise_mouse else "black"))

        blt.put(1, 7, 0x25CB)

        blt.print_(
            1, 8, "[color=%s][U+25CF][/color] Mouse cursor is visible" % ("orange" if cursor_visible else "black"))

        blt.put(1, 8, 0x25CB)

        blt.print_(double_click_area.x, double_click_area.y - 1, "Double-click here:")
        blt.color("darker orange" if plate else "darker gray")
        double_click_area.fill()

        mx = blt.state(blt.TK_MOUSE_X)
        my = blt.state(blt.TK_MOUSE_Y)
        blt.color(0x60FFFFFF)
        for x in range(blt.state(blt.TK_WIDTH)): blt.put(x, my, 0x2588)
        for y in range(blt.state(blt.TK_HEIGHT)): blt.put(mx, y, 0x2588)

        blt.color(0x8000FF00)
        blt.put(mlx, mly, 0x2588)

        blt.color(0x80FF00FF)
        blt.put(mrx, mry, 0x2588)

        blt.refresh()

        while True:
            code = blt.read()
            counter += 1

            if code in (blt.TK_ESCAPE, blt.TK_CLOSE):
                proceed = False

            elif code == blt.TK_MOUSE_LEFT:
                x = blt.state(blt.TK_MOUSE_X)
                y = blt.state(blt.TK_MOUSE_Y)

                if x == 1 and (y == 7 or y == 8):
                    if y == 7:
                        precise_mouse = not precise_mouse
                        blt.set("input.precise-mouse=%s" % ("true" if precise_mouse else "false"))
                    else:
                        cursor_visible = not cursor_visible
                        blt.set("input.mouse-cursor=%s" % ("true" if cursor_visible else "false"))
                elif (x,y) in double_click_area:
                    clicks = blt.state(blt.TK_MOUSE_CLICKS)
                    if clicks > 0 and clicks % 2 == 0:
                        plate = not plate
                else:
                    mlx = x
                    mly = y

            elif code == blt.TK_MOUSE_RIGHT:
                mrx = blt.state(blt.TK_MOUSE_X)
                mry = blt.state(blt.TK_MOUSE_Y)

            elif code == blt.TK_MOUSE_SCROLL:
                scroll += blt.state(blt.TK_MOUSE_WHEEL)

            elif code == blt.TK_SPACE:
                cursor_visible = not cursor_visible
                blt.set("input.mouse-cursor=%s" % ("true" if cursor_visible else "false"))
    
            if not (proceed and blt.has_input()): break

    blt.color("white")
    blt.composition(False);
    blt.set("input: precise-mouse=false, mouse-cursor=true, filter={keyboard}")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_mouse()
    blt.close()