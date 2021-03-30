## 1. Wifi


### 1.1 STA

```python
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ssid', 'passwd')

i = 0
while not wlan.isconnected() and i < 100:
    i = i + 1
    time.sleep(1)
    if not wlan.isconnected():
        print('connect wifi, wait a moment ...')

print('connect Wifi successfully!')
print(wlan.ifconfig())
```

### 1.2 AP


## 2. 通过Http访问 

使用 MicroPython 实现一个简单的 HttpServer，运行在 EPS32 上，使用浏览器进行访问。

这里我们将客户端页面部署到 Gitee Pages 上，通过固定的网址访问客户端，避免了安装 APP 的烦恼，但是，在不同浏览器上表现出不同行为：

- 小米浏览器 (手机端): 无问题
- 华为浏览器 (手机端): 无问题
- chrome (PC端): 跨域问题，可以通过设置解决，详见：[chrome-cors-error-on-request-to-localhost-dev-server-from-remote-site](https://stackoverflow.com/questions/66534759/chrome-cors-error-on-request-to-localhost-dev-server-from-remote-site
)
- safari (PC端): 跨域问题，还不清楚如何解决
- edge (PC端): 无问题
- 其他: 未测试
