
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import time
import webrepl

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ssid', 'passwd')

i = 0
while not wlan.isconnected() and i < 100:
    i = i + 1
    time.sleep(1)
    if not wlan.isconnected():
        print('connect ...')

print('connect Wifi successfully!')
print(wlan.ifconfig())

webrepl.start()

