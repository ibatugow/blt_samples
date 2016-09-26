# coding=utf8

from __future__ import division
import PyBearLibTerminal as blt

def test_input_filtering():
    blt.set("window.title='Omni: input filtering'")

    events = (
        ["0123456789", 1], # 0 - disabled, 1 - keypress, 2 - both keypress and keyrelease
        ["close",      1],
        ["escape",     1],
        ["q",          0],
        ["abc",        0],
        ["keyboard",   0],
        ["mouse-left", 0],
        ["mouse",      0],
    )

    colors = ("dark gray", "white", "lightest blue")

    def apply_input_filter():
        ss = ""
        for event in events:
            if event[1] == 0: continue # disabled
            ss += event[0] # keypress
            if event[1] == 2: ss += "+" # keyrelease too
            ss += ", "

        blt.set("input.filter={%s}" % ss)

    apply_input_filter()

    event_counter = 0

    proceed = True
    while proceed:
        blt.clear()
        blt.color("white")

        h = blt.print_(
            2, 1,
            "[bbox=76]Modify input filter by pressing corresponding numbers (digits are added "
            "to filter automatically). Gray color ([color=%s]like this[/color]) means that "
            "event is disabled. Regular white color means keypress is enabled. Blueish color "
            "([color=%s]like this[/color]) means both keypress and keyrelease are enabled.\n\n"
            "Both CLOSE and ESCAPE close this demo." % (colors[0], colors[2]))

        for i, event in enumerate(events):
            blt.print_(
                2, 1 + h + 1 + i,
                "[color=orange]%i[/color]. [color=%s]%s" %
                    (i, colors[event[1]], event[0]))

        blt.print_(
            2, 1 + h + 1 + len(events) + 1,
            "Events read: [color=orange]%i" % event_counter)

        blt.refresh()

        while True:
            key = blt.read()
            event_counter += 1

            if key in (blt.TK_CLOSE,blt.TK_ESCAPE):
                proceed = False
                break
            elif blt.TK_1 <= key <= blt.TK_9:
                index = (key - blt.TK_1) + 1
                if index < len(events):
                    event = events[index]
                    event[1] = (event[1] + 1) % 3
                apply_input_filter()

            if not (proceed and blt.has_input()): break

    blt.set("input.filter={keyboard}")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_input_filtering()
    blt.close()