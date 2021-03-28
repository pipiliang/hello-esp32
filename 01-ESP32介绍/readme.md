## 1. 简介
ESP32是一个由 Espressif 提供的热门的WiFi/蓝牙单片机的片上系统（SoC），大部分I/O引脚由两侧排针引出以便于连接。开发者可以根据需要（as needed）将这些引脚连接到外围设备。当使用面包板时，标准化的排针也令开发变得容易且方便。

详见：[ESP32 快速参考](https://docs.singtown.com/micropython/zh/latest/esp32/esp32/quickref.html)。

<div align="center">
<img src="./../images/esp32.jpg" width="50%">
</div>

## 2. 功能说明
以下列表和图表介绍了ESP32-DevKitC板的关键组件、接口和控制

ESP-WROOM-32
标准ESP-WROOM-32 模块焊接在ESP32-DevKitC 板

EN
POWERON_RESET 重置按钮：按下此按钮可以重置系统

Boot
下载按钮：按住Boot按钮并按下EN按钮初始化固件下载模式。然后用户可以通过串口下载固件。

USB
USB接口。是给板子供电以及ESP-WROOM-32与PC通信的接口。

I/O
ESP-WROOM-32 的大部分I/O引脚已由板上的两侧排针引出。用户可以对ESP32进行编程来实现各种功能，比如PWM,ADC,DAC,I2C,I2S,SPI 等。