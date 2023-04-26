#!/bin/python3

import os
import sys


"""
read terminal output
https://stackoverflow.com/q/3503879/12688015
"""

design = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep energy-full-design").read()
current = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep energy-full:").read()

design = int(''.join(i for i in design if i.isdecimal()))
current = int(''.join(i for i in current if i.isdecimal()))

print(f'Design: {design//10000}')
print(f'Current: {current//10000}')
print(f"Current max battery capacity: {round(current/design, 2)}")

