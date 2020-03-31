import os

import numpy as np
import sounddevice as sd

import time


def wifi(order):
    os.system("networksetup -setairportpower airport " + str(order))


def print_sound(indata, outdata, frames, time, status):
    time_duration = 0
    try:
        volume_norm = int(np.linalg.norm(indata) * 10)

        if volume_norm < 7:  # Adjustable
            time_duration += 1
            if time_duration > 160:  # Adjustable
                wifi("on")
                print("Wifi has been cut!")
                time.sleep(3)  # Adjustable
                wifi("off")
                print("Wifi has been back to online!")
        else:
            print("|" * volume_norm)
            time_duration = 0
    except:
        pass


with sd.Stream(callback=print_sound):
    while True:
        pass
