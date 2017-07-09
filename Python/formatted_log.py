# coding=utf-8

from __future__ import division

__all__ = ['test_formatted_log']

from bearlibterminal import terminal as blt
from random import randint, choice
from math import ceil

vocabulary = [
    "ad", "adipisicing", "aliqua", "aliquip", "amet", "anim", "aute", "cillum",
    "commodo", "consectetur", "consequat", "culpa", "cupidatat", "deserunt",
    "do", "dolore", "dolor", "dolore", "duis", "ea", "eiusmod", "elit", "enim",
    "esse", "est", "et", "ex", "exercitation", "excepteur", "eu", "fugiat",
    "id", "in", "incididunt", "ipsum", "irure", "labore", "laboris", "laborum",
    "lorem", "magna", "minim", "mollit", "nisi", "non", "nostrud", "nulla",
    "occaecat", "officia", "pariatur", "proident", "qui", "quis", "reprehenderit",
    "sed", "sit", "sint", "sunt", "tempor", "ullamco", "ut", "velit", "veniam",
    "voluptate"]

colors = [
    "light orange",
    "orange",
    "dark orange",
    "darker orange",
    "light gray",
    "gray"]

alternative_fonts = []

def generate_random_message():
    words = []
    # Total number of sentences in a message: [1..10].
    n_sentences = randint(1,10)
    for j in range(n_sentences):
        # Total number of words in a sentence: [5..15].
        n_words = randint(5,15)
        for i in range(n_words):
            # Pick up a random word from the vocabulary above.
            word = choice(vocabulary)

            # First word in a sentence starts from capital letter.
            if i == 0: word = word.capitalize()

            # 1/10 chance to be randomly colored.
            colored = randint(1,10) == 1
            if colored: word = "[color=%s]%s[/color]" % (choice(colors), word)

            # 1/20 chance to have another font face.
            alt_font = len(alternative_fonts) > 0 and randint(1, 20) == 1
            if alt_font: word = "[font=%s]%s[/font]" % (choice(alternative_fonts), word)

            words.append(word)

        words[-1] += "."

    return " ".join(words)


padding_left = 4
padding_right = 4
padding_top = 2
padding_bottom = 2
mouse_scroll_step = 2 # 2 text rows per mouse wheel step.

class MessageList(object):
    def __init__(self):
        self.total_height = 1
        self.texts = []
        self.heights = []

    def update_heights(self, width):
        self.heights = [blt.measure(text, width)[1] for text in self.texts]
        # recompute total height, including the blank lines between messages
        self.total_height = sum(self.heights) + len(self.texts) - 1 

    def append(self, message):
        self.texts.append(message)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, key):
        return self.texts[key], self.heights[key]

messages = MessageList()


class FrameWithScrollbar(object):
    def __init__(self, contents):
        self.offset = 0
        self.width = 0
        self.height = 0
        self.scrollbar_height = 0
        self.scrollbar_column = 0
        self.scrollbar_offset = 0
        self.left = self.top = self.width = self.height = 0
        self.contents = contents

    def update_geometry(self, left, top, width, height):
        # Save current scroll position
        current_offset_percentage = self.offset / self.contents.total_height

        # Update frame dimensions
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        # Calculate new message list height
        self.contents.update_heights(width)

        # Scrollbar
        self.scrollbar_height = min(int(ceil(self.height * self.height / self.contents.total_height)), self.height)

        # Try to recover scroll position
        self.offset = int(self.contents.total_height * current_offset_percentage)
        self.offset = min(self.offset, self.contents.total_height - self.height)
        if self.contents.total_height <= self.height: self.offset = 0

    def scroll_to_pixel(self, py):
        py -= self.top * blt.state(blt.TK_CELL_HEIGHT)
        factor = py / (self.height * blt.state(blt.TK_CELL_HEIGHT))
        self.offset = int(self.contents.total_height * factor)
        self.offset = max(0, min(self.contents.total_height - self.height, self.offset))

    def scroll(self, dy):
        self.offset = max(0, min(self.contents.total_height - self.height, self.offset + dy))

    def draw(self):
        # Frame background
        blt.layer(0)
        blt.bkcolor("darkest gray")
        blt.clear_area(self.left, self.top, self.width, self.height)

        # Scroll bar
        blt.bkcolor("darker gray")
        blt.clear_area(self.left + self.width, self.top, 1, self.height)
        blt.bkcolor("none")
        blt.color("dark orange")
        self.scrollbar_column = self.left + self.width
        self.scrollbar_offset = int(
            (self.top + (self.height - self.scrollbar_height) * (self.offset / (self.contents.total_height - self.height))) * 
            blt.state(blt.TK_CELL_HEIGHT))
        for i in range(self.scrollbar_height):
            blt.put_ext(self.scrollbar_column, i, 0, self.scrollbar_offset, 0x2588)


frame = FrameWithScrollbar(messages)

def test_formatted_log():
    dragging_scrollbar = False
    dragging_scrollbar_offset = 0

    blt.set("window: title='Omni: message log', resizeable=true, minimum-size=20x8; font: default")
    blt.set("input: filter='keyboard, mouse+', precise-mouse=true")
    if blt.set("runic font: ../Media/Tigrex3drunes_16x16_437.PNG, size=16x16, codepage=437, spacing=2x1, transparent=auto"):
        alternative_fonts.append("runic")        
    if blt.set("stone font: ../Media/Aesomatica_16x16_437.png, size=16x16, codepage=437, spacing=2x1, transparent=#FF00FF"):
        alternative_fonts.append("stone")
    if blt.set("curvy font: ../Media/Cheepicus_16x16_437.png, size=16x16, codepage=437, spacing=2x1, transparent=auto"):
        alternative_fonts.append("curvy")

    prompt = \
        "Use arrow keys or mouse wheel to scroll the list up and down. " \
        "Try to resize the window.\n\n--- --- ---"
    messages.append(prompt)

    # Add a dozen of random messages
    for i in range(10):
        messages.append(generate_random_message())

    # Initial update
    frame.update_geometry(
        padding_left,
        padding_top,
        blt.state(blt.TK_WIDTH) - (padding_left + padding_right + 1),
        blt.state(blt.TK_HEIGHT) - (padding_top + padding_bottom))

    while True:
        blt.clear()
        frame.draw()
        blt.color("white")

        blt.layer(1)
        current_line = 0
        for text, height in messages:
            if current_line + height >= frame.offset:
                # stop when message is below frame
                if current_line - frame.offset > frame.height: break
                # drawing message
                blt.puts(padding_left, padding_top + current_line - frame.offset, text, frame.width)
            current_line += height + 1

        blt.crop(padding_left, padding_top, frame.width, frame.height)

        # Render
        blt.refresh()

        key = blt.read()

        if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
            break

        elif key == blt.TK_UP:
            frame.scroll(-1)
            
        elif key == blt.TK_DOWN:
            frame.scroll(1)

        elif key == blt.TK_MOUSE_SCROLL:
            # Mouse wheel scroll
            frame.scroll(mouse_scroll_step * blt.state(blt.TK_MOUSE_WHEEL))

        elif key == blt.TK_MOUSE_LEFT and blt.state(blt.TK_MOUSE_X) == frame.scrollbar_column:
            py = blt.state(blt.TK_MOUSE_PIXEL_Y)
            if frame.scrollbar_offset <= py <= frame.scrollbar_offset + frame.scrollbar_height * blt.state(blt.TK_CELL_HEIGHT):
                # Clicked on the scrollbar handle: start dragging
                dragging_scrollbar = True
                dragging_scrollbar_offset = py - frame.scrollbar_offset
            else:
                # Clicked outside of the handle: jump to position
                frame.scroll_to_pixel(blt.state(blt.TK_MOUSE_PIXEL_Y) - frame.scrollbar_height * blt.state(blt.TK_CELL_HEIGHT) // 2)

        elif key == blt.TK_MOUSE_LEFT | blt.TK_KEY_RELEASED :
            dragging_scrollbar = False

        elif key == blt.TK_MOUSE_MOVE:
            if dragging_scrollbar:
                frame.scroll_to_pixel(blt.state(blt.TK_MOUSE_PIXEL_Y) - dragging_scrollbar_offset)            

            while blt.peek() == blt.TK_MOUSE_MOVE:
                blt.read()

        elif key == blt.TK_RESIZED:
            frame.update_geometry(
                padding_left,
                padding_top,
                blt.state(blt.TK_WIDTH) - (padding_left + padding_right + 1),
                blt.state(blt.TK_HEIGHT) - (padding_top + padding_bottom))

    blt.set("window: resizeable=false")
    blt.set("runic font: none; stone font: none; curvy font: none")
    blt.set("input.precise-mouse=false;")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_formatted_log()
    blt.close()