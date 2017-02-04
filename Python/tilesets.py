# coding=utf8

from bearlibterminal import terminal as blt

def test_tilesets():
    blt.set("window.title='Omni: tilesets'")
    blt.composition(True)

    # Load tilesets
    blt.set("U+E100: ../Media/Runic.png, size=8x16")
    blt.set("U+E200: ../Media/Tiles.png, size=32x32, align=top-left")
    blt.set("U+E300: ../Media/fontawesome-webfont.ttf, size=24x24, spacing=3x2, codepage=../Media/fontawesome-codepage.txt")
    blt.set("zodiac font: ../Media/Zodiac-S.ttf, size=24x36, spacing=3x3, codepage=437")

    blt.clear()
    blt.color("white")

    blt.puts(2, 1, "[color=orange]1.[/color] Of course, there is default font tileset.")

    blt.puts(2, 3, "[color=orange]2.[/color] You can load some arbitrary tiles and use them as glyphs:")
    blt.puts(2+3, 4,
        "Fire rune ([color=red][U+E102][/color]), "
        "water rune ([color=lighter blue][U+E103][/color]), "
        "earth rune ([color=darker green][U+E104][/color])")

    blt.puts(2, 6, "[color=orange]3.[/color] Tiles are not required to be of the same size as font symbols:")
    blt.put(2+3+0, 7, 0xE200+7)
    blt.put(2+3+5, 7, 0xE200+8)
    blt.put(2+3+10, 7, 0xE200+9)

    blt.puts(2, 10, "[color=orange]4.[/color] Like font characters, tiles may be freely colored and combined:")
    blt.put(2+3+0, 11, 0xE200+8)
    blt.color("lighter orange")
    blt.put(2+3+5, 11, 0xE200+8)
    blt.color("orange")
    blt.put(2+3+10, 11, 0xE200+8)
    blt.color("dark orange")
    blt.put(2+3+15, 11, 0xE200+8)

    blt.color("white")
    order = [11, 10, 14, 12, 13]
    for i in range(len(order)):
        blt.put(30 + i * 4, 11, 0xE200 + order[i]);
        blt.put(30 + (len(order)+1) * 4, 11, 0xE200 + order[i])

    blt.put(30 + len(order) * 4, 11, 0xE200 + 15)

    blt.puts(2, 14, "[color=orange]5.[/color] And tiles can even come from TrueType fonts like this:")
    for i in range(6):
        blt.put(5 + i * 5, 15, 0xE300 + i)

    blt.puts(5, 18, "...or like this:\n[font=zodiac]D F G S C")

    blt.refresh()

    key = None
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE):
        key = blt.read()

    # Clean up
    blt.set("U+E100: none; U+E200: none; U+E300: none; zodiac font: none")
    blt.composition(False)


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_tilesets()
    blt.close()