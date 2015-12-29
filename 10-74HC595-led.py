#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

SDI_PIN = 11
RCLK_PIN = 12
SRCLK_PIN = 13

OUT_PINS = [SDI_PIN,RCLK_PIN,SRCLK_PIN]

led_offsets = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OUT_PINS, GPIO.OUT, initial=GPIO.LOW)

def hc595_in(dat):
    for bit in range(0, 8):
        GPIO.output(SDI_PIN, 0x80 & (dat << bit))
        GPIO.output(SRCLK_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.OUTPUT(SRCLK_PIN, GPIO.LOW)

def hc595_out():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def loop():
    while True:
        for i in range(0, len(led_offsets)):
            hc595_in(led_offsets[i])
            hc595_out()
            time.sleep(0.1)

        for i in range(0, len(led_offsets)-1, -1, -1):
            hc595_in(led_offsets[i])
            hc595_out()
            time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
