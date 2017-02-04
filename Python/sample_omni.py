from bearlibterminal import terminal as blt

from speed import test_speed
from basic_output import test_basic_output
from default_font import test_default_font
from tilesets import test_tilesets
from sprites import test_sprites
from manual_cellsize import test_manual_cellsize
from auto_generated import test_auto_generated
from multiple_fonts import test_multiple_fonts
from text_alignment import test_text_alignment
from formatted_log import test_formatted_log
from layers import test_layers
from extended_basics import test_extended_basics
from extended_smooth_scroll import test_extended_smooth_scroll
from dynamic_sprites import test_dynamic_sprites
from keyboard import test_keyboard
from mouse import test_mouse
from text_input import test_text_input
from input_filtering import test_input_filtering
from window_resize import test_window_resize
from pick import test_pick

def reset():
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu';"
            "font: default;"
            "input: filter={keyboard}")
    blt.color("white")
   

def main():
    blt.open()

    entries = (
        ("Basic output", test_basic_output),
        ("Default font", test_default_font),
        ("Tilesets", test_tilesets),
        ("Sprites", test_sprites),
        ("Manual cellsize", test_manual_cellsize),
        ("Auto-generated tileset", test_auto_generated),
        ("Multiple fonts", test_multiple_fonts),
        ("Text alignment", test_text_alignment),
        ("Formatted log", test_formatted_log),
        ("Layers", test_layers),
        ("Extended 1: basics", test_extended_basics),
        #("Extended 2: inter-layer animation", TestExtendedInterlayer),
        ("Extended 2: smooth scroll", test_extended_smooth_scroll),
        ("Dynamic sprites", test_dynamic_sprites),
        ("Speed", test_speed),
        ("Input 1: keyboard", test_keyboard),
        ("Input 2: mouse", test_mouse),
        ("Input 3: text input", test_text_input),
        ("Input 4: filtering", test_input_filtering),
        ("Window resizing", test_window_resize),
        ("Examining cell contents", test_pick)
    )

    reset()

    while True:
        blt.clear()
        for (i,e) in enumerate(entries):
            shortcut = '123456789abcdefghijklmnopqrstuvwxyz'[i]
            blt.puts(2, 1+i, "[color=orange]%c.[/color] %s%s" % (shortcut, "" if e[1] else "[color=gray]", e[0]))
            
        blt.puts(2, 23, "[color=orange]ESC.[/color] Exit")
        blt.refresh()

        key = blt.read()

        if key in (blt.TK_ESCAPE, blt.TK_CLOSE):
            break
        elif blt.TK_1 <= key <= blt.TK_9 or blt.TK_A <= key <= blt.TK_Z:
            index = key - blt.TK_1 if key >= blt.TK_1 else 9 + key - blt.TK_A
            if 0 <= index < len(entries) and entries[index][1]:
                entries[index][1]()
                reset()

    blt.close()

if __name__ == "__main__":
    main()