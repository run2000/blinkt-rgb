#!/usr/bin/env python

import sys
import blinkt 

v = 10 # value -- brightness
r = 255
g = 255
b = 255
pixels = '11111111' # x-axis


def hex_to_rgb(value):
    value = value.lstrip('#')
    if len(value) < 6:
        usage()

    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))

def usage():
    print("Usage: {} [<value 0-100>] <#rrggbb> [<pixels [11111111]>]".format(sys.argv[0]))
    sys.exit(1)


if len(sys.argv) == 4:

    # Try #rrggbb value
    v = int(sys.argv[1])
    r, g, b = hex_to_rgb(sys.argv[2])
    pixels = sys.argv[3].rjust(8, '0')


elif len(sys.argv) == 3:

    # Try #rrggbb value
    v = int(sys.argv[1])
    r, g, b = hex_to_rgb(sys.argv[2])

elif len(sys.argv) == 2:

    # Try #rrggbb value
    r, g, b = hex_to_rgb(sys.argv[1])

else:
    usage()

# Exit if any of r, g, b are greater than 255
if max(r, g, b) > 255:
    usage()

# Exit if more than 8 pixels given
if len(pixels) > 8:
    usage()

# Exit if value > 100 or < 0
if v > 100 or v < 0:
    usage()

print("Setting Blinkt to value {v}, colour {r},{g},{b}, pixels {pixels}".format(r=r, g=g, b=b, v=v, pixels=pixels))

blinkt.set_clear_on_exit(False)

i = 8
for c in pixels:
    i-= 1
    if (c == '1'):
        blinkt.set_pixel(i, r, g, b, float(v) / 100)

blinkt.show()

