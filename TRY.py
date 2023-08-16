import ustruct
from machine import I2C, Pin
from ili934xnew import ILI9341, color565
from time import sleep

# set up I2C communication with the LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = ILI9341(i2c)

# open the image file and extract RGB values
with open('image.rgb', 'rb') as f:
    # read the image header
    header = f.read(6)
    width = ustruct.unpack('>H', header[0:2])[0]
    height = ustruct.unpack('>H', header[2:4])[0]
    pixel_size = ustruct.unpack('>H', header[4:6])[0]

    # read the pixel data and display RGB values on the LCD
    for y in range(height):
        for x in range(width):
            pixel_data = f.read(pixel_size)
            r, g, b = ustruct.unpack('BBB', pixel_data)
            lcd.pixel(x, y, color565(r, g, b))

# wait for a few seconds before closing the LCD display
sleep(5)
lcd.deinit()import ustruct
from machine import I2C, Pin
from ili934xnew import ILI9341, color565
from time import sleep

# set up I2C communication with the LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = ILI9341(i2c)

# open the image file and extract RGB values
with open('image.rgb', 'rb') as f:
    # read the image header
    header = f.read(6)
    width = ustruct.unpack('>H', header[0:2])[0]
    height = ustruct.unpack('>H', header[2:4])[0]
    pixel_size = ustruct.unpack('>H', header[4:6])[0]

    # read the pixel data and display RGB values on the LCD
    for y in range(height):
        for x in range(width):
            pixel_data = f.read(pixel_size)
            r, g, b = ustruct.unpack('BBB', pixel_data)
            lcd.pixel(x, y, color565(r, g, b))

# wait for a few seconds before closing the LCD display
sleep(5)
lcd.deinit()