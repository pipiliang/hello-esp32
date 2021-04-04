from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(scl=Pin(21), sda=Pin(22))
screen = SSD1306_I2C(128, 64, i2c)


def show(message):
    screen.fill(0)
    screen.text('hello esp32!', 0, 0)
    screen.text(message, 0, 15)
    screen.show()


