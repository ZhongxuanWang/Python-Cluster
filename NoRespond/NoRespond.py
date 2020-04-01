import os

import numpy as np
import sounddevice as sd

import time

time_duration = 0


def wifi(order):
    os.system("networksetup -setairportpower airport " + str(order))
    return


def print_sound(indata, outdata, frames, time, status):
    global time_duration
    try:
        volume_norm = int(np.linalg.norm(indata) * 10)

        if volume_norm < 7:  # Adjustable
            time_duration += 1
            if time_duration > 300:  # Adjustable
                os.system("networksetup -setairportpower airport off")
                print("Wifi has been cut!")
                time_duration = 0
                for a in range(10000000000): a += 1
                os.system("networksetup -setairportpower airport on")
                print(" - - - Wifi has been back to online!")
        else:
            print("|" * volume_norm)
            time_duration = 0
    except:
        pass


with sd.Stream(callback=print_sound):
    while True:
        pass
