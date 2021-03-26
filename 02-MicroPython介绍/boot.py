
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

while wlan.ifconfig()[0] == '0.0.0.0' and i < 10:
    i = i + 1
    time.sleep(1)
    if wlan.ifconfig()[0] == '0.0.0.0':
        print('connect ...')

print('connect Wifi successfully!')
print(wlan.ifconfig())

webrepl.start()

