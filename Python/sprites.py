# coding=utf8

from ctypes import c_uint32, addressof
from bearlibterminal import terminal as blt

def test_sprites():
    blt.set("window.title='Omni: sprites'")

    blt.set("U+E000: ../Media/Background.jpg")
    blt.set("U+E001: ../Media/EasternDragon.png, resize=128x128, resize-filter=nearest")
    blt.set("U+E002: ../Media/FiveElements.bmp, resize=128x128, resize-filter=bilinear")

    c = (c_uint32 * 4)(
            blt.color_from_argb(128, 192, 64, 64),
            blt.color_from_argb(128, 64, 192, 64),
            blt.color_from_argb(128, 64, 64, 192),
            blt.color_from_argb(128, 192, 192, 64))

    blt.set("U+E003: %d, raw-size=2x2, resize=128x128, resize-filter=bicubic" % addressof(c))

    blt.clear()

    blt.color("black")
    blt.puts(2, 1, "[color=black]This primarily serves as a quick test of image format support")
    blt.puts(2, 3, "1. Background is loaded from a JPEG file")
    blt.puts(2, 5, "2. Dragon sprite is loaded from a PNG file\n   image is upscaled 2x with nearest neighbourhood filter")
    blt.puts(2, 8, "3. Five elements diagram is loaded from BMP file\n   image is downscaled with bilinear filer")
    blt.puts(2, 11, "4. Color gradient is loaded from 2x2 in-memory buffer\n   image is upscaled 64x with bicubic filter")

    blt.color("white")
    blt.put(0, 0, 0xE000) # Background
    blt.put(5, 14, 0xE001) # Dragon
    blt.put(5+18*1, 14, 0xE002) # FiveElements
    blt.put(5+18*2, 14, 0xE003) # Gradient

    blt.refresh()

    key = None
    while key not in (blt.TK_CLOSE, blt.TK_ESCAPE):
        key = blt.read()

    blt.set("U+E000: none; U+E001: none; U+E002: none; U+E003: none")



if __name__ == "__main__":
    blt.open()
    blt.set("window: size=80x25, cellsize=auto, title='Omni: menu'; font: default")
    blt.color("white")
    test_sprites()
    blt.close()