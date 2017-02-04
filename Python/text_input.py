# coding=utf8

from __future__ import division

from bearlibterminal import terminal as blt

key_names = {
    0: "",
    blt.TK_MOUSE_LEFT: "LMB",
    blt.TK_MOUSE_RIGHT: "RMB",
    blt.TK_MOUSE_MIDDLE: "MMB",
    blt.TK_CLOSE: "Close",
    blt.TK_BACKSPACE: "Backspace",
    blt.TK_TAB: "Tab",
    blt.TK_RETURN: "Enter",
    blt.TK_SHIFT: "Shift",
    blt.TK_CONTROL: "Ctrl",
    blt.TK_PAUSE: "Pause",
    blt.TK_ESCAPE: "Escape",
    blt.TK_PAGEUP: "Page Up",
    blt.TK_PAGEDOWN: "Page Down",
    blt.TK_END: "End",
    blt.TK_HOME: "Home",
    blt.TK_LEFT: "Left",
    blt.TK_UP: "Up",
    blt.TK_RIGHT: "Right",
    blt.TK_DOWN: "Down",
    blt.TK_INSERT: "Insert",
    blt.TK_DELETE: "Delete",
    blt.TK_F1: "F1",
    blt.TK_F2: "F2",
    blt.TK_F3: "F3",
    blt.TK_F4: "F4",
    blt.TK_F5: "F5",
    blt.TK_F6: "F6",
    blt.TK_F7: "F7",
    blt.TK_F8: "F8",
    blt.TK_F9: "F9",
    blt.TK_F10: "F10",
    blt.TK_F11: "F11",
    blt.TK_F12: "F12",
    blt.TK_KP_DIVIDE: "Keypad /",
    blt.TK_KP_MULTIPLY: "Keypad *",
    blt.TK_KP_MINUS: "Keypad -",
    blt.TK_KP_PLUS: "Keypad +",
    blt.TK_KP_ENTER: "Keypad Enter",
    blt.TK_KP_0: "Keypad 0",
    blt.TK_KP_1: "Keypad 1",
    blt.TK_KP_2: "Keypad 2",
    blt.TK_KP_3: "Keypad 3",
    blt.TK_KP_4: "Keypad 4",
    blt.TK_KP_5: "Keypad 5",
    blt.TK_KP_6: "Keypad 6",
    blt.TK_KP_7: "Keypad 7",
    blt.TK_KP_8: "Keypad 8",
    blt.TK_KP_9: "Keypad 9",
    blt.TK_KP_PERIOD: "Keypad .",
}

def draw_frame(x, y, w, h):
    blt.clear_area(x, y, w, h)

    for i in range(x, x + w):
        blt.put(i, y, u'─');
        blt.put(i, y+h-1, u'─');

    for j in range(y, y + h):
        blt.put(x, j, u'│')
        blt.put(x+w-1, j, u'│')

    blt.put(x, y, u'┌')
    blt.put(x + w - 1, y, u'┐')
    blt.put(x, y + h - 1, u'└')
    blt.put(x + w - 1, y + h - 1, u'┘')

def test_text_input():
    blt.set("window.title='Omni: text input'")
    blt.composition(False)

    max_chars = 32
    text = ""
    character = ' '
    result = 0
    char_result = 0

    while True:
        blt.clear()
        blt.color("white")

        blt.puts(2, 1, "Select different input tests by pressing corresponding number:")

        blt.puts(2, 3, "[color=orange]1.[/color] read_str")
        draw_frame(5, 4, max_chars + 2, 3)
        blt.puts(6, 5, "%s" % text)
        blt.puts(5 + max_chars + 2 + 1, 5, "[color=gray] %s" % ("OK" if result >= 0 else "Cancelled"))

        blt.puts(2, 8, "[color=orange]2.[/color] read_char")
        draw_frame(5, 9, 5, 3)
        blt.put(7, 10, character)
        blt.puts(11, 10, "[color=gray]%s" % key_names.get(char_result, str(char_result)))

        blt.refresh()

        key = blt.read()
        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

        elif key == blt.TK_1:
            blt.color("orange")
            draw_frame(5, 4, max_chars + 2, 3)
            result, text = blt.read_str(6, 5, text, max_chars)

        elif key == blt.TK_2:
            blt.color("orange")
            draw_frame(5, 9, 5, 3)

            while True:
                blt.put(7, 10, character)  
                blt.clear_area(11, 10, 16, 1)
                blt.puts(11, 10, "[color=gray]%s" % key_names.get(char_result, str(char_result)))
                blt.refresh()

                character = ' '
                key = blt.read()
                if key in (blt.TK_ESCAPE, blt.TK_CLOSE, blt.TK_RETURN):
                    break
                elif blt.check(blt.TK_WCHAR):
                    character = blt.state(blt.TK_WCHAR)
                    char_result = key
                elif key < blt.TK_KEY_RELEASED:
                    char_result = key



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_text_input()
    blt.close()