# coding=utf8

from __future__ import division

import PyBearLibTerminal as blt
import random

fps = 40
speed_cap = 25
map_size = 64
tile_size = 32

def sgn(x):
    return (0 < x) - (x < 0)

def test_extended_smooth_scroll():
    random.seed()

    blt.set("window.title='Omni: extended output / smooth scroll'")
    blt.set("input.filter={keyboard+}")
    blt.composition(True)

    # Load resources
    blt.set("U+E000: ../Media/Tiles.png, size=32x32, alignment=top-left")

    screen_width = blt.state(blt.TK_WIDTH) * blt.state(blt.TK_CELL_WIDTH);
    screen_height = blt.state(blt.TK_HEIGHT) * blt.state(blt.TK_CELL_HEIGHT);
    hspeed = vspeed = 0
    hoffset = voffset = 0

    map_ = [[0] * map_size for _ in range(map_size)]
    
    for _ in range(map_size * map_size // 10):
        x = random.randrange(map_size)
        y = random.randrange(map_size)
        map_[y][x] = random.randrange(8)

    while True:
        hoffset -= hspeed
        voffset -= vspeed

        blt.clear()

        tx = hoffset % tile_size
        ty = voffset % tile_size
        ix = (hoffset - tx) // tile_size
        iy = (voffset - ty) // tile_size
        jx = (-ix) % map_size if ix < 0 else map_size - (ix % map_size)
        jy = (-iy) % map_size if iy < 0 else map_size - (iy % map_size)
        hc = (screen_width + 2*tile_size - tx - 1) // tile_size        
        vc = (screen_height + 2*tile_size - ty - 1) // tile_size

        blt.print_(2, 1, "speed: %d, %d" % (hspeed, vspeed))
        blt.print_(2, 2, "offset: %d/%d, %d/%d" % (ix, jx, iy, jy))

        for y in range(vc + 1):
            my = (jy + y) % map_size
            for x in range(hc + 1):
                mx = (jx + x) % map_size
                c = map_[my][mx]
                blt.put_ext(0, 0, (x - 1) * tile_size + tx, (y - 1) * tile_size + ty, 0xE000 + c)

        blt.refresh()

        if blt.has_input():
            key = blt.read()
            if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
                break

        if blt.state(blt.TK_LEFT):
            if hspeed > -speed_cap: hspeed -= 1
        elif blt.state(blt.TK_RIGHT):
            if hspeed < speed_cap: hspeed += 1
        else:
            hspeed -= sgn(hspeed)

        if blt.state(blt.TK_UP):
            if vspeed > -speed_cap: vspeed -= 1
        elif blt.state(blt.TK_DOWN):
            if vspeed < speed_cap: vspeed += 1
        else:
            vspeed -= sgn(vspeed)

        blt.delay(1000//fps)

    blt.set("U+E000: none")
    blt.set("input.filter={keyboard}")
    blt.composition(False)



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_extended_smooth_scroll()
    blt.close()