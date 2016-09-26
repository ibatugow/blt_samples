# coding=utf8

from __future__ import division

__all__ = ['test_text_alignment']

import PyBearLibTerminal as blt

Left   = 0
Center = 1
Right  = 2
Top    = 0
Bottom = 2

lorem_ipsum = \
    "[c=orange]Lorem[/c] ipsum dolor sit amet, consectetur adipisicing elit, " \
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
    "[c=orange]Ut[/c] enim ad minim veniam, quis nostrud exercitation ullamco " \
    "laboris nisi ut aliquip ex ea commodo consequat. [c=orange]Duis[/c] aute " \
    "irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
    "fugiat nulla pariatur. [c=orange]Excepteur[/c] sint occaecat cupidatat " \
    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

padding_h = 4
padding_v = 2

from collections import namedtuple
Frame = namedtuple("Frame", "left top width height")

def update_geometry():
    return Frame( 
        left = padding_h,
        top = padding_v * 2 + 2,
        width = blt.state(blt.TK_WIDTH) - padding_h * 2,
        height = blt.state(blt.TK_HEIGHT) - padding_v * 3 - 2)

def test_text_alignment():
    blt.set("window: title='Omni: text alignment', resizeable=true, minimum-size=44x12")
    blt.composition(True)

    horizontal_names = ("left", "center", "right")
    vertical_names = ("top", "center", "bottom")
    horizontal = Left
    vertical = Top

    frame = update_geometry()

    while True:
        blt.clear()

        # Background square
        blt.bkcolor("darkest gray")
        blt.clear_area(*frame)
        blt.bkcolor("none")

        # Comment
        blt.print_(
            frame.left,
            frame.top - padding_v - 2,
            "Use arrows to change text alignment.\n"
            "Current alignment is [c=orange]%s-%s[/c]." % 
            (vertical_names[vertical], horizontal_names[horizontal])
        )

        #Text origin
        if horizontal == Right:
            x = frame.left + frame.width - 1
        elif horizontal == Center:
            x = frame.left + frame.width // 2
        else: # Left
            x = frame.left

        if vertical ==  Bottom:
            y = frame.top + frame.height - 1
        elif vertical == Center:
            y = frame.top + frame.height // 2
        else: # Top
            y = frame.top

        blt.color("darkest orange")
        blt.put(x, y, 0x2588)

        blt.color("white")
        blt.print_(
            x, y,
            "[wrap=%dx%d][align=%s-%s]%s" %
            (frame.width, frame.height,
             vertical_names[vertical], horizontal_names[horizontal],
            lorem_ipsum)
        )

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

        elif key == blt.TK_LEFT:
            horizontal = max(horizontal-1, Left)

        elif key == blt.TK_RIGHT:
            horizontal = min(horizontal+1, Right)

        elif key == blt.TK_UP:
            vertical = max(vertical-1, Top)

        elif key == blt.TK_DOWN:
            vertical = min(vertical+1, Bottom)
            
        elif key == blt.TK_RESIZED:
            frame = update_geometry()

    blt.composition(False)
    blt.set("window.resizeable=false")


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_text_alignment()
    blt.close()