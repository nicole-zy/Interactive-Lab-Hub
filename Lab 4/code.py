import time
import board
import busio
import random

import adafruit_mpr121
from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import os
import RPi.GPIO as GPIO

from PIL import Image, ImageDraw, ImageFont
from subprocess import call, Popen

cwd = os.getcwd()


def handle_speak(val):
    subprocess.run(["sh", "GoogleTTS_demo.sh", val])
    # call(f"espeak -ven -k5 -s150 --stdout '{val}' | aplay", shell=True)
    time.sleep(0.5)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

    # Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
y = top
a = "Welcome to \n Dance Dance \n Revolution Game\n The game begins now"
handle_speak("Welcome to Dance Dance revolution game.")
handle_speak("The game begins now.")


draw.text((x, y), a, font=font, fill="#FFFFFF")
y += font.getsize(a)[1]
disp.image(image, rotation)
time.sleep(2)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

left = mpr121[6]
right = mpr121[11]

while True:
#     for i in range(12):
#         if mpr121[i].value:
#             print(f"Banana {i} touched!")
#     time.sleep(0.25)  # Small delay to keep from spamming output messages.
   
    direction = random.randint(1, 2)
    if direction == 1:
        b = "left"
        draw.text((x, y), b, font=font, fill="#FFFFFF")
        y = font.getsize(b)[1]
        disp.image(image, rotation)
        time.sleep(0.1)
        while not (left.value or right.value):
            time.sleep(0.01)
        if right.value:
            c = "\n Game Over"
            draw.text((x, y), c, font=font, fill="#FF00FF")
            y += font.getsize(c)[1]
            disp.image(image, rotation)
            handle_speak("Game over")
            break
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)
    else:
        d ="Right"
        draw.text((x, y), d, font=font, fill="#FFFFFF")
        y = font.getsize(d)[1]
        disp.image(image, rotation)
        time.sleep(0.1)
        while not (left.value or right.value):
            time.sleep(0.01)
        if left.value:
            e = "\n Game Over"
            draw.text((x, y), e, font=font, fill="#FF00FF")
            y += font.getsize(e)[1]
            disp.image(image, rotation)
            handle_speak("Game over")
            break
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)
disp.image(image, rotation)
