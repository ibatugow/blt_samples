# coding=utf8

import PyBearLibTerminal as blt

def test_multiple_fonts():
    blt.set("window.title='Omni: multiple fonts in scene'")

    # Load several fonts
    blt.set("window.size=64x20; font: ../Media/VeraMono.ttf, size=10x20")
    blt.set("italic font: ../Media/VeraMoIt.ttf, size=10x20")
    blt.set("bold font: ../Media/VeraMoBd.ttf, size=10x20")
    blt.set("huge font: ../Media/VeraMono.ttf, size=20x40, spacing=2x2")

    blt.clear()
    blt.color("white")
    h = blt.print_(
        2, 1,
        "[wrap=60]If you [color=orange][font=italic]really[/font][/color] want, "
        "you can even put [color=orange][font=bold]emphasis[/font][/color] on a text. "
        "This works by loading several truetype tilesets with custom codepages to an "
        "unused code points and using [color=orange]font[/color] postformatting tag."
    )

    blt.print_(
        2, 1+h+1,
        "[font=huge][wrap=60]It's pretty easy to print in bigger fonts as well."
    )
    blt.refresh()

    key = 0
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE): key = blt.read()

    # Clean up
    blt.set("window.size=80x25; font: default; italic font: none; bold font: none; huge font: none")


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu' font: default")
    blt.color("white")
    test_multiple_fonts()
    blt.close()