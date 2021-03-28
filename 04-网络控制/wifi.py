import network
import time


class WIFI:

    def __init__(self, ssid, passwd):
        self.ssid = ssid
        self.passwd = passwd
        self.wlan = None

    def connect(self):
        if not self.wlan or self.wlan.isconnected():
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
            self.wlan.connect(self.ssid, self.passwd)
            i = 0
            while not self.wlan.isconnected() and i < 100:
                i = i + 1
                time.sleep(1)
                if not self.wlan.isconnected():
                    print('connect ...')

        if self.wlan.isconnected():
            print('connect Wifi successfully!')
            print(self.wlan.ifconfig())
        else:
            print('connect Wifi failed!')

    def disconnect(self):
        if self.wlan:
            self.wlan.disconnect()

