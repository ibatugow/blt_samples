# coding=utf8

import PyBearLibTerminal as blt

def test_manual_cellsize():
    blt.set("window.title='Omni: manual cellsize'")

    font_name = "../Media/VeraMono.ttf"
    font_size = 12
    cell_width = 8
    cell_height = 16

    def setup_font(): blt.set("font: %s, size=%d" % (font_name, font_size))
    def setup_cellsize(): blt.set("window: cellsize=%dx%d" % (cell_width, cell_height))

    setup_cellsize()
    setup_font()

    while True:
        blt.clear()
        blt.color("white")

        blt.print_(2, 1, "Hello, world!")
        blt.print_(2, 3, "[color=orange]Font size:[/color] %d" % font_size)
        blt.print_(2, 4, "[color=orange]Cell size:[/color] %dx%d" % (cell_width, cell_height))
        blt.print_(2, 6, "[color=orange]TIP:[/color] Use arrow keys to change cell size")
        blt.print_(2, 7, "[color=orange]TIP:[/color] Use Shift+Up/Down arrow keys to change font size")

        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break
        elif key == blt.TK_LEFT and not blt.state(blt.TK_SHIFT) and cell_width > 4:
            cell_width -= 1
            setup_cellsize()
        elif key == blt.TK_RIGHT and not blt.state(blt.TK_SHIFT) and cell_width < 24:
            cell_width += 1
            setup_cellsize()
        elif key == blt.TK_DOWN and not blt.state(blt.TK_SHIFT) and cell_height < 24:
            cell_height += 1
            setup_cellsize()
        elif key == blt.TK_UP and not blt.state(blt.TK_SHIFT) and cell_height > 4:
            cell_height -= 1
            setup_cellsize()
        elif key == blt.TK_UP and blt.state(blt.TK_SHIFT) and font_size < 64:
            font_size += 1
            setup_font()
        elif key == blt.TK_DOWN and blt.state(blt.TK_SHIFT) and font_size > 4:
            font_size -= 1
            setup_font()
    
    blt.set("font: default; window.cellsize=auto")    

if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu' font: default")
    blt.color("white")
    test_manual_cellsize()
    blt.close()