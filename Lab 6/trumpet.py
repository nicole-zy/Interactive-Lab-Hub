import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import time
import board
import busio

import adafruit_mpr121
import paho.mqtt.client as mqtt
import uuid


topic = 'IDD/#'
song = 0
notes_rock_you = [1, 3, 2, 1]
notes = []
message = ''

# this is the callback that gets called each time a message is received
def on_message(cleint, userdata, msg):
    message = msg.payload.decode('UTF-8')
    print(message)
    if message == 'Rock you':
        print('same')
        song = 0
        notes = notes_rock_you
	# you can filter by topics
	# if msg.topic == 'IDD/some/other/topic': do thing

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)
# you can subsribe to as many topics as you'd like
# client.subscribe('some/other/topic')


# Configuration for CS and DC pins (these are PiTFT defaults):
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

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)


def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)


draw.rectangle((0, 0, width, height), outline=0, fill=0)
x = 0
y = top
text = ''
while True:
    d = message
    draw.text((x, y), d, font=font, fill="#FFFFFF")
    y += font.getsize(d)[1]
    disp.image(image, rotation)
    time.sleep(1)
	
#     if not notes_rock_you:
#         display = "Song finished"
#         client.loop()
#     else:
#         display = notes
    
#     if message == 'Rock you':
#         for i in notes_rock_you:
#             text += str(i)
#         d = message
#         draw.text((x, y), d, font=font, fill="#FFFFFF")
#         y += font.getsize(d)[1]
#         disp.image(image, rotation)
#         time.sleep(1)
#         draw.rectangle((0, 0, width, height), outline=0, fill=0)
#         d = text
#         draw.text((x, y), d, font=font, fill="#FFFFFF")
#         y += font.getsize(d)[1]
#         disp.image(image, rotation)
#         time.sleep(0.1)
#         draw.rectangle((0, 0, width, height), outline=0, fill=0)
# #     draw.text((25, 5), display, font=font, fill="#0000FF")
#         if notes_rock_you:
#             client.publish("IDD/music", notes_rock_you[0])
#             notes_rock_you.pop(0)
# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()
