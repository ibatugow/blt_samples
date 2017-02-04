# coding=utf8

from __future__ import division

from collections import namedtuple
from bearlibterminal import terminal as blt

mkey = namedtuple("mkey", "vk x y w h caption")


def fill_rectangle(x, y, w, h, color):
    blt.color(color)

    for i in range(x, x + w):
        for j in range(y, y + h):
            blt.put(i, j, 0x2588)

    for i in range(x, x + w):
        blt.put(i, y - 1, 0x2584)
        blt.put(i, y + h, 0x2580)

    for j in range(y, y + h):
        blt.put(x - 1, j, 0x2590)
        blt.put(x + w, j, 0x258C)

    blt.put(x - 1, y - 1, 0x2597)
    blt.put(x - 1, y + h, 0x259D)
    blt.put(x + w, y - 1, 0x2596)
    blt.put(x + w, y + h, 0x2598)


def test_keyboard():
    blt.set("window.title='Omni: basic keyboard input'")
    blt.set("input.filter={keyboard+}")
    blt.composition(True)

    #
    #	"┌───┐┌──┬──┬──┬──┐┌──┬──┬──┬──┐┌──┬───┬───┬───┐┌─────┬─────┬───────┐",
    #	"│ESC││F1│F2│F3│F4││F5│F6│F7│F8││F9│F10│F11│F12││PRSCR│SCRLK│ PAUSE │",
    #	"└───┘└──┴──┴──┴──┘└──┴──┴──┴──┘└──┴───┴───┴───┘└─────┴─────┴───────┘",
    #	"┌───┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─────┐┌────┬────┬────┐┌───┬───┬───┬───┐",
    #	"│ ` │1│2│3│4│5│6│7│8│9│0│─│=│BCKSP││INS │HOME│PGUP││NUM│ / │ * │ ─ │",
    #	"├───┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬────┤├────┼────┼────┤├───┼───┼───┼───┤",
    #	"│TAB │q│w│e│r│t│y│u│i│o│p│[│]│  E ││DEL │END │PGDN││ 7 │ 8 │ 9 │   │",
    #	"├────┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┐ N │└────┴────┴────┘├───┼───┼───┤ + │",
    #	"│CAPS │a│s│d│f│g│h│j│k│l│;│'│\│ T │                │ 4 │ 5 │ 6 │   │",
    #	"├─────┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴─┴───┤     ┌────┐     ├───┼───┼───┼───┤",
    #	"│SHIFT │z│x│c│v│b│n│m│,│.│/│ SHIFT│     │ UP │     │ 1 │ 2 │ 3 │ E │",
    #	"├────┬─┴┬┴─┴┬┴─┴─┴┬┴─┴┬┴─┼─┴─┬────┤┌────┼────┼────┐├───┴───┼───┤ N │",
    #	"│CTRL│LW│ALT│SPACE│ALT│RW│CTX│CTRL││LEFT│DOWN│RGHT││ 0     │ . │ T │",
    #	"└────┴──┴───┴─────┴───┴──┴───┴────┘└────┴────┴────┘└───────┴───┴───┘"
    #

    grid = [
        "┌───┐┌──┬──┬──┬──┐┌──┬──┬──┬──┐┌──┬───┬───┬───┐┌─────┬─────┬───────┐",
        "│   ││  │  │  │  ││  │  │  │  ││  │   │   │   ││     │     │       │",
        "└───┘└──┴──┴──┴──┘└──┴──┴──┴──┘└──┴───┴───┴───┘└─────┴─────┴───────┘",
        "┌───┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─────┐┌────┬────┬────┐┌───┬───┬───┬───┐",
        "│   │ │ │ │ │ │ │ │ │ │ │ │ │     ││    │    │    ││   │   │   │   │",
        "├───┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬────┤├────┼────┼────┤├───┼───┼───┼───┤",
        "│    │ │ │ │ │ │ │ │ │ │ │ │ │    ││    │    │    ││   │   │   │   │",
        "├────┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┐   │└────┴────┴────┘├───┼───┼───┤   │",
        "│     │ │ │ │ │ │ │ │ │ │ │ │ │   │                │   │   │   │   │",
        "├─────┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴─┴───┤     ┌────┐     ├───┼───┼───┼───┤",
        "│      │ │ │ │ │ │ │ │ │ │ │      │     │    │     │   │   │   │   │",
        "├────┬─┴┬┴─┴┬┴─┴─┴┬┴─┴┬┴─┼─┴─┬────┤┌────┼────┼────┐├───┴───┼───┤   │",
        "│    │  │   │     │   │  │   │    ││    │    │    ││       │   │   │",
        "└────┴──┴───┴─────┴───┴──┴───┴────┘└────┴────┴────┘└───────┴───┴───┘"
    ]

    keys = [mkey(*k) for k in [
        # Functional keys row
        # [vk, x, y, w, h, caption]
        [ blt.TK_ESCAPE, 1, 1, 3, 1, "ESC" ],
        [ blt.TK_F1, 6, 1, 2, 1, "F1" ],
        [ blt.TK_F2, 9, 1, 2, 1, "F2" ],
        [ blt.TK_F3, 12, 1, 2, 1, "F3" ],
        [ blt.TK_F4, 15, 1, 2, 1, "F4" ],
        [ blt.TK_F5, 19, 1, 2, 1, "F5" ],
        [ blt.TK_F6, 22, 1, 2, 1, "F6" ],
        [ blt.TK_F7, 25, 1, 2, 1, "F7" ],
        [ blt.TK_F8, 28, 1, 2, 1, "F8" ],
        [ blt.TK_F9, 32, 1, 2, 1, "F9" ],
        [ blt.TK_F10, 35, 1, 3, 1, "F10" ],
        [ blt.TK_F11, 39, 1, 3, 1, "F11" ],
        [ blt.TK_F12, 43, 1, 3, 1, "F12" ],
        [ blt.TK_PAUSE, 60, 1, 7, 1, " PAUSE " ],
        # First row
        [ blt.TK_GRAVE, 1, 4, 3, 1, " ` " ],
        [ blt.TK_1, 5, 4, 1, 1, "1" ],
        [ blt.TK_2, 7, 4, 1, 1, "2" ],
        [ blt.TK_3, 9, 4, 1, 1, "3" ],
        [ blt.TK_4, 11, 4, 1, 1, "4" ],
        [ blt.TK_5, 13, 4, 1, 1, "5" ],
        [ blt.TK_6, 15, 4, 1, 1, "6" ],
        [ blt.TK_7, 17, 4, 1, 1, "7" ],
        [ blt.TK_8, 19, 4, 1, 1, "8" ],
        [ blt.TK_9, 21, 4, 1, 1, "9" ],
        [ blt.TK_0, 23, 4, 1, 1, "0" ],
        [ blt.TK_MINUS, 25, 4, 1, 1, "-" ],
        [ blt.TK_EQUALS, 27, 4, 1, 1, "=" ],
        [ blt.TK_BACKSPACE, 29, 4, 5, 1, "BCKSP" ],
        # Second row
        [ blt.TK_TAB, 1, 6, 4, 1, "TAB" ],
        [ blt.TK_Q, 6, 6, 1, 1, "q" ],
        [ blt.TK_W, 8, 6, 1, 1, "w" ],
        [ blt.TK_E, 10, 6, 1, 1, "e" ],
        [ blt.TK_R, 12, 6, 1, 1, "r" ],
        [ blt.TK_T, 14, 6, 1, 1, "t" ],
        [ blt.TK_Y, 16, 6, 1, 1, "y" ],
        [ blt.TK_U, 18, 6, 1, 1, "u" ],
        [ blt.TK_I, 20, 6, 1, 1, "i" ],
        [ blt.TK_O, 22, 6, 1, 1, "o" ],
        [ blt.TK_P, 24, 6, 1, 1, "p" ],
        [ blt.TK_LBRACKET, 26, 6, 1, 1, "[[" ],
        [ blt.TK_RBRACKET, 28, 6, 1, 1, "]]" ],
        # Third row
        # { VK_, 1, 8, 5, 1, "a" ],
        [ blt.TK_A, 7, 8, 1, 1, "a" ],
        [ blt.TK_S, 9, 8, 1, 1, "s" ],
        [ blt.TK_D, 11, 8, 1, 1, "d" ],
        [ blt.TK_F, 13, 8, 1, 1, "f" ],
        [ blt.TK_G, 15, 8, 1, 1, "g" ],
        [ blt.TK_H, 17, 8, 1, 1, "h" ],
        [ blt.TK_J, 19, 8, 1, 1, "j" ],
        [ blt.TK_K, 21, 8, 1, 1, "k" ],
        [ blt.TK_L, 23, 8, 1, 1, "" ],
        [ blt.TK_SEMICOLON, 25, 8, 1, 1, ";" ],
        [ blt.TK_APOSTROPHE, 27, 8, 1, 1, "'" ],
        [ blt.TK_BACKSLASH, 29, 8, 1, 1, "\\" ],
        # Fourth row
        [ blt.TK_SHIFT, 1, 10, 6, 1, "SHIFT" ],
        [ blt.TK_Z, 8, 10, 1, 1, "z" ],
        [ blt.TK_X, 10, 10, 1, 1, "x" ],
        [ blt.TK_C, 12, 10, 1, 1, "c" ],
        [ blt.TK_V, 14, 10, 1, 1, "v" ],
        [ blt.TK_B, 16, 10, 1, 1, "b" ],
        [ blt.TK_N, 18, 10, 1, 1, "n" ],
        [ blt.TK_M, 20, 10, 1, 1, "m" ],
        [ blt.TK_COMMA, 22, 10, 1, 1, "," ],
        [ blt.TK_PERIOD, 24, 10, 1, 1, "." ],
        [ blt.TK_SLASH, 26, 10, 1, 1, "/" ],
        [ blt.TK_SHIFT, 28, 10, 6, 1, " SHIFT" ],
        # Fifth row
        [ blt.TK_CONTROL, 1, 12, 4, 1, "CTR" ],
        [ blt.TK_ALT, 9, 12, 3, 1, "ALT" ],
        [ blt.TK_SPACE, 13, 12, 5, 1, "SPACE" ],
        [ blt.TK_ALT, 19, 12, 3, 1, "ALT" ],
        [ blt.TK_CONTROL, 30, 12, 4, 1, "CTR" ],
        # Navigation
        [ blt.TK_INSERT, 36, 4, 4, 1, "INS" ],
        [ blt.TK_HOME, 41, 4, 4, 1, "HOME" ],
        [ blt.TK_PAGEUP, 46, 4, 4, 1, "PGUP" ],
        [ blt.TK_DELETE, 36, 6, 4, 1, "DEL" ],
        [ blt.TK_END, 41, 6, 4, 1, "END" ],
        [ blt.TK_PAGEDOWN, 46, 6, 4, 1, "PGDN" ],
        [ blt.TK_UP, 41, 10, 4, 1, " UP " ],
        [ blt.TK_LEFT, 36, 12, 4, 1, "LEFT" ],
        [ blt.TK_DOWN, 41, 12, 4, 1, "DOWN" ],
        [ blt.TK_RIGHT, 46, 12, 4, 1, "RGHT" ],
        # Numpad
        [ blt.TK_KP_DIVIDE, 56, 4, 3, 1, " / " ],
        [ blt.TK_KP_MULTIPLY, 60, 4, 3, 1, " * " ],
        [ blt.TK_KP_MINUS, 64, 4, 3, 1, " - " ],
        [ blt.TK_KP_7, 52, 6, 3, 1, " 7 " ],
        [ blt.TK_KP_8, 56, 6, 3, 1, " 8 " ],
        [ blt.TK_KP_9, 60, 6, 3, 1, " 9 " ],
        [ blt.TK_KP_PLUS, 64, 6, 3, 3, " + " ],
        [ blt.TK_KP_4, 52, 8, 3, 1, " 4 " ],
        [ blt.TK_KP_5, 56, 8, 3, 1, " 5 " ],
        [ blt.TK_KP_6, 60, 8, 3, 1, " 6 " ],
        [ blt.TK_KP_1, 52, 10, 3, 1, " 1 " ],
        [ blt.TK_KP_2, 56, 10, 3, 1, " 2 " ],
        [ blt.TK_KP_3, 60, 10, 3, 1, " 3 " ],
        [ blt.TK_KP_0, 52, 12, 7, 1, " 0 " ],
        [ blt.TK_KP_PERIOD, 60, 12, 3, 1, " . " ],
    ]]

    unavailable_keys = [mkey(*k) for k in [
        [ 0, 1, 8, 5, 1, "CAPS " ],
        [ 0, 6, 12, 2, 1, "LW" ],
        [ 0, 23, 12, 2, 1, "RW" ],
        [ 0, 26, 12, 3, 1, "CTX" ],
        [ 0, 48, 1, 5, 1, "PRSCR" ],
        [ 0, 54, 1, 5, 1, "SCRLK" ],
        [ 0, 52, 4, 3, 1, "NUM" ]
    ]]


    normal_text = 0xFFFFFFFF
    pressed_key = 0xFFBB6000
    pressed_key_text = 0xFF000000
    available_key_text = 0xFFBBBBBB
    unavailable_key_text = 0xFF404040
    grid_color = 0xFF606060

    while True:
        blt.clear()

        for k in keys:
            if blt.state(k.vk):
                fill_rectangle(6 + k.x, 1 + k.y, k.w, k.h, pressed_key)
                blt.color(pressed_key_text)
                blt.puts(6 + k.x, 1 + k.y, k.caption)
            else:
                blt.color(available_key_text)
                blt.puts(6 + k.x, 1 + k.y, k.caption)

        # Special case: Enter keys
        if blt.state(blt.TK_RETURN):
            # Main keyboard
            region = \
                u"▗▄▄▄▄▖\n" \
                u"▐████▌\n" \
                u"▝▜███▌\n" \
                u" ▐███▌\n" \
                u" ▝▀▀▀▘\n"
            #blt.color(pressed_key)
            blt.puts(6 + 29, 6, "[color=#%x]%s" % (pressed_key,region))

        if blt.check(blt.TK_KP_ENTER):
            # Numpad
            fill_rectangle(6 + 64, 1 + 10, 3, 3, pressed_key)

        # Main keyboard
        blt.color(pressed_key_text if blt.state(blt.TK_RETURN) else available_key_text)
        blt.put(6 + 32, 1+6+0, 'E')
        blt.put(6 + 32, 1+6+1, 'N')
        blt.put(6 + 32, 1+6+2, 'T')

        # Numpad
        blt.color(pressed_key_text if blt.state(blt.TK_KP_ENTER) else available_key_text)
        blt.put(6 + 65, 1+10+0, 'E')
        blt.put(6 + 65, 1+10+1, 'N')
        blt.put(6 + 65, 1+10+2, 'T')

        blt.color(grid_color)
        for i, line in enumerate(grid):
            blt.puts(6, 1 + i, line)

        blt.color(unavailable_key_text)
        for k in unavailable_keys:
            blt.puts(6 + k.x, 1 + k.y, k.caption)

        blt.color(normal_text)
        blt.puts(6, 1 + 15, "[color=orange]NOTE:[/color] keys printed in dark gray color are not available by design.")
        blt.puts(6, 1 + 17, "[color=orange]NOTE:[/color] for demonstration purposes Escape will not close this demo;")
        blt.puts(6, 1 + 18, "use Shift+Escape combination to exit.")

        blt.refresh()

        key = blt.read()
        if key == blt.TK_CLOSE or (key == blt.TK_ESCAPE and blt.state(blt.TK_SHIFT)):
            break

    blt.composition(False)
    blt.set("input.filter={keyboard}")




if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_keyboard()
    blt.close()
