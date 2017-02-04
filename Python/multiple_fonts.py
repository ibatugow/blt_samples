# coding=utf8

from bearlibterminal import terminal as blt

def test_multiple_fonts():
    blt.set("window.title='Omni: multiple fonts in scene'")

    # Load several fonts
    blt.set("window.size=64x20; font: ../Media/VeraMono.ttf, size=10x20")
    blt.set("italic font: ../Media/VeraMoIt.ttf, size=10x20")
    blt.set("bold font: ../Media/VeraMoBd.ttf, size=10x20")
    blt.set("huge font: ../Media/VeraMono.ttf, size=20x40, spacing=2x2")

    blt.clear()
    blt.color("white")
    _,h = blt.puts( 
        2, 1,
        "If you [color=orange][font=italic]really[/font][/color] want, "
        "you can even put [color=orange][font=bold]emphasis[/font][/color] on a text. "
        "This works by loading several truetype tilesets with custom codepages to an "
        "unused code points and using [color=orange]font[/color] postformatting tag.",
        width=60
    )

    blt.puts(
        2, 1+h+1,
        "[font=huge]It's pretty easy to print in bigger fonts as well.",
        width=60
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