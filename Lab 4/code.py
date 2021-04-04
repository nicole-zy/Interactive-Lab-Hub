import time
import board
import busio
import random

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

left = mpr121[6]
right = mpr121[11]

while True:
    for i in range(12):
        if mpr121[i].value:
            print(f"Banana {i} touched!")
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
   
    direction = random.randint(1, 2)
    if direction == 1:
      if right.value:
        print("Error - Game lost")
    else:
      if left.value:
        print("Error - Game lost")

