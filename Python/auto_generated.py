# coding=utf8

import PyBearLibTerminal as blt

def test_auto_generated():
    blt.set("window.title='Omni: auto-generated tileset'")

    hoffset = 40
    cell_width = blt.state(blt.TK_CELL_WIDTH)
    cell_height = blt.state(blt.TK_CELL_HEIGHT)
    def setup_cellsize(): blt.set("window.cellsize=%dx%d" % (cell_width, cell_height))

    while True:
        blt.clear()
        blt.color("white")

        blt.print_(2, 1, "[color=orange]Cell size:[/color] %dx%d" % (cell_width, cell_height))
        blt.print_(2, 3, "[color=orange]TIP:[/color] Use arrow keys\nto change cell size")

        for j in range(16):
            blt.print_(hoffset+6+j*2, 1, "[color=orange]%X" % j)

        y = 0
        for code in range(0x2500, 0x259F+1): 
            if code%16 == 0:
                blt.print_(hoffset, 2 + y * 1, " [color=orange]%04X" % code)

            blt.put(hoffset + 6 + (code%16) * 2, 2 + y * 1, code)

            if (code+1)%16 == 0: y += 1

        blt.print_(
            2, 6,
            u"┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐\n"
            u"│Z││A││ ││W││A││R││U││D││O│\n"
            u"└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘\n"
        )

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break
        elif key == blt.TK_LEFT and cell_width > 4:
            cell_width -= 1
            setup_cellsize()
        elif key == blt.TK_RIGHT and cell_width < 24:
            cell_width += 1
            setup_cellsize()
        elif key == blt.TK_DOWN and cell_height < 24:
            cell_height += 1
            setup_cellsize()
        elif key == blt.TK_UP and cell_height > 4:
            cell_height -= 1
            setup_cellsize()

    blt.set("window.cellsize=auto")


if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu' font: default")
    blt.color("white")
    test_auto_generated()
    blt.close()