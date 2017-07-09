# coding=utf-8

from __future__ import division
from bearlibterminal import terminal as blt

def test_basic_output():
    blt.set("window.title='Omni: basic output'")
    blt.clear()
    blt.color("white")

    # Wide color range
    n,_ = blt.puts(2, 1, "[color=orange]1.[/color] Wide color range: ")
    long_word = "antidisestablishmentarianism."
    long_word_length = len(long_word)
    for i in range(long_word_length):
        factor = i / long_word_length
        red = int((1 - factor) * 255)
        green = int(factor * 255)
        blt.color(blt.color_from_argb(255, red, green, 0))
        blt.put(2 + n + i, 1, long_word[i])

    blt.color("white")

    blt.puts(2, 3, "[color=orange]2.[/color] Backgrounds: [color=black][bkcolor=gray] grey [/bkcolor] [bkcolor=red] red ")

    blt.puts(2, 5, "[color=orange]3.[/color] Unicode support: Кириллица Ελληνικά α=β²±2°")

    blt.puts(2, 7, "[color=orange]4.[/color] Tile composition: a + [color=red]/[/color] = a[+][color=red]/[/color], a vs. a[+][color=red]¨[/color]")

    blt.printf(2, 9, "[color=orange]5.[/color] Box drawing symbols:")

    blt.puts(5, 11,
        "   ┌────────┐  \n"
        "   │!......s└─┐\n"
        "┌──┘........s.│\n"
        "│............>│\n"
        "│...........┌─┘\n"
        "│<.@..┌─────┘  \n"
        "└─────┘        \n"
    )

    blt.refresh()
    key = None
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE):
        key = blt.read()


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_basic_output()
    blt.close()