#!/usr/bin/env python
# -*- coding: latin-1 -*-

import colorsys
import signal
import time
import socket
import subprocess

from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd


print("""Unicorn HAT HD: date_time

This program shows a scrolling calendar/clock on the Pimorony unicorn hd hat


Press Ctrl+C to exit!

""")
try:
    while True:
        cmd = "date +'%u'"
        dow = subprocess.check_output(cmd, shell = True )
	if '1' in dow: TIME1=u'luned\u00EC'.encode('latin-1')
	elif '2' in dow: TIME1=u'marted\u00EC'.encode('latin-1')
	elif '3' in dow: TIME1=u'mercoled\u00EC'.encode('latin-1')
	elif '4' in dow: TIME1=u'gioved\u00EC'.encode('latin-1')
	elif '5' in dow: TIME1=u'venerd\u00EC'.encode('latin-1')
	elif '6' in dow: TIME1=u'sabato'.encode('latin-1')
	else: TIME1=u'domenica'.encode('latin-1')
        cmd = "date +'%d %B'"
        TIME2 = subprocess.check_output(cmd, shell = True )
        cmd = "date +'%H:%M'"
        TIME3 = subprocess.check_output(cmd, shell = True )
	cmd = "/usr/games/fortune -sn 80 it| tr '\n' ' '| tr '\t' ' '"
        SENTENCE = subprocess.check_output(cmd, shell = True )
        lines = [TIME1,TIME2,TIME3,SENTENCE]

        colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]


# Use `fc-list` to show a list of installed fonts on your system,
# or `ls /usr/share/fonts/` and explore.

#FONT = ("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 12)
        FONT = ("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 12)

# sudo apt install fonts-droid
#	FONT = ("/usr/share/fonts/truetype/droid/DroidSans.ttf", 12)

# sudo apt install fonts-roboto
#	FONT = ("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf", 10)

        unicornhathd.rotation(90)
        unicornhathd.brightness(0.5)


        width, height = unicornhathd.get_shape()

        text_x = width
        text_y = 0


        font_file, font_size = FONT

        font = ImageFont.truetype(font_file, font_size)

        text_width, text_height = width, 0

        for line in lines:
            w, h = font.getsize(line)
            text_width += w + width
            text_height = max(text_height,h)

        text_width += width + text_x + 1

        image = Image.new("RGB", (text_width,max(16, text_height)), (0,0,0))
        draw = ImageDraw.Draw(image)

        offset_left = 0

        for index, line in enumerate(lines):
            draw.text((text_x + offset_left, text_y), line, colours[index], font=font)

            offset_left += font.getsize(line)[0] + width

        unicornhathd.clear()

        for scroll in range(text_width - width):
           for x in range(width):
             for y in range(height):
                 pixel = image.getpixel((x+scroll, y))
                 r, g, b = [int(n) for n in pixel]
                 unicornhathd.set_pixel(width-1-x, y, r, g, b)

           unicornhathd.show()
           time.sleep(0.02)

except KeyboardInterrupt:
    unicornhathd.off()
