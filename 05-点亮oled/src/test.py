from wifi import WIFI
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from httpserver import SimpleHttpServer
import ujson

i2c = I2C(scl=Pin(21), sda=Pin(22))
screen = SSD1306_I2C(128, 64, i2c)

ip = WIFI('ador', 'houziaipipi2015').connect()

screen.text(str(ip), 0, 0)
screen.show()


def show(message):
    screen.fill(0)
    screen.text(str(ip), 0, 0)
    screen.text(message, 0, 15)
    screen.show()


def listen(method, headers, body):
    body_json = ujson.loads(body)
    message = body_json.get("message", '--')
    show(message)
    return body


SimpleHttpServer('0.0.0.0', 9999, 1).start(listen)
