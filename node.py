from machine import ADC, Pin, UART 
import time

def run():
    uart = UART(0, 115200)
    uart.init(115200, parity=None, stop=1)

    s0 = Pin(0,  Pin.OUT)
    s1 = Pin(4,  Pin.OUT)
    s2 = Pin(5,  Pin.OUT)
    s3 = Pin(16, Pin.OUT)
    enable = Pin(2, Pin.OUT)
    adc = ADC(0)

    s0.value(0)
    s1.value(0)
    s2.value(0)
    s3.value(0)
    
    enable.value(0) # 0 for enable mux

    channels = [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1]
            ]
    
    active_pads = 16
    values = []

    while True:
        for channel in range(active_pads):
            s0.value(channels[channel][0])
            s1.value(channels[channel][1])
            s2.value(channels[channel][2])
            s3.value(channels[channel][3])
            value = adc.read()
            values.append(value)
        uart.write(str(values)+'\n')
        values = []

