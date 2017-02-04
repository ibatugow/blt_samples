# coding=utf8

from __future__ import division

__all__ = ['test_text_alignment']

from bearlibterminal import terminal as blt

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

    names =	{
        blt.TK_ALIGN_LEFT: "TK_ALIGN_LEFT",
        blt.TK_ALIGN_CENTER: "TK_ALIGN_CENTER",
        blt.TK_ALIGN_RIGHT: "TK_ALIGN_RIGHT",
        blt.TK_ALIGN_TOP: "TK_ALIGN_TOP",
        blt.TK_ALIGN_MIDDLE: "TK_ALIGN_MIDDLE",
        blt.TK_ALIGN_BOTTOM: "TK_ALIGN_BOTTOM",
	}
    horizontal_align = blt.TK_ALIGN_LEFT
    vertical_align = blt.TK_ALIGN_TOP

    frame = update_geometry()

    while True:
        blt.clear()

        # Background square
        blt.bkcolor("darkest gray")
        blt.clear_area(*frame)
        blt.bkcolor("none")

        # Comment
        blt.puts(
            frame.left,
            frame.top - padding_v - 2,
            "Use arrows to change text alignment.\n"
            "Current alignment is [c=orange]%s[/c] | [c=orange]%s[/c]." % 
            (names[vertical_align], names[horizontal_align])
        )

        #Text origin
        x, y = frame.left, frame.top

        blt.color("white")
        blt.puts(
            x, y,
            lorem_ipsum,
            frame.width, frame.height, vertical_align | horizontal_align
        )
        
        blt.puts(80-14, 3, "[c=orange][U+2588]")
        blt.puts(80-14, 3, "12345\nabc\n-=#=-", align=vertical_align | horizontal_align)

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

        elif key == blt.TK_LEFT:
            horizontal_align = blt.TK_ALIGN_CENTER if horizontal_align == blt.TK_ALIGN_RIGHT else blt.TK_ALIGN_LEFT

        elif key == blt.TK_RIGHT:
            horizontal_align = blt.TK_ALIGN_CENTER if horizontal_align == blt.TK_ALIGN_LEFT else blt.TK_ALIGN_RIGHT

        elif key == blt.TK_UP:
            vertical_align = blt.TK_ALIGN_MIDDLE if vertical_align == blt.TK_ALIGN_BOTTOM else blt.TK_ALIGN_TOP

        elif key == blt.TK_DOWN:
            vertical_align = blt.TK_ALIGN_MIDDLE if vertical_align == blt.TK_ALIGN_TOP else blt.TK_ALIGN_BOTTOM
            
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