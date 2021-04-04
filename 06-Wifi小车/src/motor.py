from machine import Pin

'''
out1 out2 
in1  in2 status
1    0   
'''
p25 = Pin(25, Pin.OUT)  # Pin25 --> in2 (L2982N)
p26 = Pin(26, Pin.OUT)  # Pin26 --> in1 (L2982N)
p32 = Pin(32, Pin.OUT)  # Pin32 --> in4 (L2982N)
p33 = Pin(33, Pin.OUT)  # Pin33 --> in3 (L2982N)
on = 1
off = 0


def forward():
    # right p25:on, p26:off, p32:on, p33:off
    control(on, off, on, off)


def back():
    control(off, on, off, on)


def right():
    # right <-, left ->
    control(off, on, on, off)


def left():
    # right ->, left <-
    control(on, off, off, on)


def stop():
    # right ->, left <-
    control(off, off, off, off)


def control(v25, v26, v32, v33):
    # right
    p25.value(v25)
    p26.value(v26)
    # left
    p32.value(v32)
    p33.value(v33)
