# coding=utf-8

from __future__ import division
from ctypes import c_uint32, addressof
from bearlibterminal import terminal as blt
from collections import namedtuple

map_ = [
    "                             ",
    " ------                      ", #       -  Wall
    " |....|      ############    ", #       #  Unlit hallway
    " |....|      #          #    ", #       .  Lit area
    " |.$..+########         #    ", #       $  Some quantity of gold
    " |....|       #      ---+--- ", #       +  A door
    " ------       #      |.....| ", #       |  Wall
    "              #      |.!...| ", #       !  A magic potion
    "              #      |.....| ", #
    "              #      |.....| ", #       @  The adventurer
    "   ----       #      |.....| ", #
    "   |..|       #######+.....| ", #       D  A red dragon
    "   |..+###    #      |.....| ", #       <  Stairs to a higher level
    "   ----  #    #      |.?...| ", #       ?  A magic scroll
    "         ######      ------- ",
    "                             "
]


symbol = namedtuple("symbol", "color tile")

palette = {
    '-': symbol(0xFFAAAAAA, 8),
    '|': symbol(0xFFAAAAAA, 8),
    '.': symbol(0xFF808080, 20),
    '#': symbol(0xFF808080, 20),
    '+': symbol(0xFFFF8000, 21),
    '!': symbol(0xFFFF00FF, 22),
    'D': symbol(0xFFFF0000, 6),
    '?': symbol(0xFF008000, 23),
    '$': symbol(0xFFFFFF00, 29),
    '<': symbol(0xFFFFFFFF, 9)
}


def test_dynamic_sprites():
    blt.set("window.title='Omni: dynamic sprites'")
    blt.set("U+E000: ../Media/Tiles.png, size=32x32, align=top-left")

    map_width = len(map_[0])
    map_height = len(map_)

    x0 = y0 = 0
    view_height, view_width = 10, 14
    minimap_scale = 4
    panel_width = (blt.state(blt.TK_WIDTH) - view_width * 4 - 1) * blt.state(blt.TK_CELL_WIDTH)
    margin = (panel_width - map_width * minimap_scale) // 2

    def draw_map():
        blt.color("white")
        for y in range(y0, y0 + view_height):
            for x in range(x0, x0 + view_width):
                code = map_[y][x]
                if code in palette:
                    s = palette[code]
                    blt.put((x - x0) * 4, (y - y0) * 2, 0xE000 + s.tile)

    def argb_from_color(col):
        return (col & 0xFF000000) >> 24, (col & 0xFF0000) >> 16, (col & 0xFF00) >> 8, col & 0xFF

    def blend_colors(one, two):
        a1, r1, g1, b1 = argb_from_color(one)
        a2, r2, g2, b2 = argb_from_color(two)
        f = a2 / 255
        r = int(r1 * (1 - f) + r2 * f)
        g = int(g1 * (1 - f) + g2 * f)
        b = int(b1 * (1 - f) + b2 * f)
        return blt.color_from_argb(a1, r, g, b)
    
    def make_minimap():
        minimap = [palette[code].color if code in palette else 0xFF000000 for row in map_ for code in row]

        for y in range(y0, y0 + view_height):
            for x in range(x0, x0 + view_width):
                minimap[y * map_width + x] = blend_colors(minimap[y * map_width + x], 0x60FFFFFF)

        minimap = (c_uint32*len(minimap))(*minimap)
        blt.set(
            "U+E100: %d, raw-size=%dx%d, resize=%dx%d, resize-filter=nearest" % (
            addressof(minimap),
            map_width, map_height,
            map_width*4, map_height*4)
        )

    while True:
        blt.clear()

        draw_map()
        blt.color("light gray")
        for x in range(80): blt.put(x, view_height * 2, 0x2580)
        for y in range(view_height * 2): blt.put(view_width * 4, y, 0x2588)

        make_minimap()
        blt.color("white")
        blt.put_ext(view_width * 4 + 1, 0, margin, margin, 0xE100)

        blt.puts(1, view_height * 2 + 1, "[color=orange]Tip:[/color] use arrow keys to move viewport over the map")

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break
        elif key == blt.TK_RIGHT and x0 < map_width-view_width:
            x0 += 1
        elif key == blt.TK_LEFT and x0 > 0:
            x0 -= 1
        elif key == blt.TK_DOWN and y0 < map_height-view_height:
            y0 += 1
        elif key == blt.TK_UP and y0 > 0:
            y0 -= 1

    blt.set("U+E000: none; U+E100: none;")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_dynamic_sprites()
    blt.close()