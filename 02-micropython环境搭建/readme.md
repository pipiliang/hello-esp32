## 1. MicroPython 介绍

MicroPython是 Python 3 语言 的精简高效实现 ，包括Python标准库的一小部分，经过优化可在微控制器和受限环境中运行。

MicroPython包含了诸如交互式提示（REPL），任意精度整数，关闭，列表解析，生成器，异常处理等高级功能。 足够精简，适合运行在只有256k的代码空间和16k的RAM的芯片上。

MicroPython旨在尽可能与普通Python兼容，让您轻松将代码从桌面传输到微控制器或嵌入式系统。

## 2. 环境搭建
本章介绍 MircoPython 的环境搭建。

### 2.1 准备工作

- 板子：这里使用的乐鑫科技的 ESP32S(ESP32-WROOM-32)。
- 系统：Win10。
- Python：3.7.6。
- 固件：下载 [MicroPython 固件](http://www.micropython.org/download/)，需要选择 Espressif 的 ESP32 模块对应的通用固件。
- IDE：下载 [MircoPython IDE Mu](https://codewith.mu/en/download)。
- 串口工具：putty 或 xshell。

### 2.2 esptool 安装

esptool 是官方提供的工具，通过 pip 安装，使用以下命令：
```
$ pip install esptool==2.0
```
说明：最新版本没有安装成功，2.0 版本安装成功并测试通过。

### 2.2 安装固件

在安装新版 MicroPython 固件前，先将设备的 FlashROM 完全清除。使用以下命令：
```
$ esptool.py --chip esp32 --port COM3 erase_flash
```
参数说明：
- chip：芯片类型，使用 esp32
- port：这里使用串口连接，`我的电脑`->`管理`->`设备管理器`->`端口` 中查看。
- 也可以通过 `esptool.py -h` 查看帮助。

等待擦除完成。

执行以下命令上传 MircoPython 固件：
```
$ esptool.py --chip esp32 --port COM3 write_flash -z 0x1000 firmware.bin
```
参数说明：
- z: 开始地址
- firmware.bin：固件路径

看到以下信息，说明成功：
```
esptool.py v2.0
Connecting........___
Chip is ESP32D0WDQ6 (revision (unknown 0xa))
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 1446224 bytes to 941239...
Wrote 1446224 bytes (941239 compressed) at 0x00001000 in 83.2 seconds (effective 139.0 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting...
```

### 2.3 交互式命令行（串口）

### 2.4 IDE




