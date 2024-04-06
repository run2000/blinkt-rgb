#!/usr/bin/env python

import sys

import blinkt 

r = 255
g = 255
b = 255
v = 10  # brightness


def hex_to_rgb(value):
    value = value.lstrip('#')
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))

def usage():
    print("Usage: {} <v> <r> <g> <b>".format(sys.argv[0]))
    sys.exit(1)


if len(sys.argv) == 5:

    # Exit if non integer value. int() will raise a ValueError
    try:
        v = int(sys.argv[1])
        r, g, b = [int(x) for x in sys.argv[2:]]
    except ValueError:
        usage()

elif len(sys.argv) == 4:

    # Exit if non integer value. int() will raise a ValueError
    try:
        r, g, b = [int(x) for x in sys.argv[1:]]
    except ValueError:
        usage()

elif len(sys.argv) == 3:

    try:
        v = int(sys.argv[1])
        # Try #rrggbb value
        r, g, b = hex_to_rgb(sys.argv[2])
    except ValueError:
        usage()

elif len(sys.argv) == 2:

    # Try #rrggbb value
    r, g, b = hex_to_rgb(sys.argv[1])

else:
    usage()

# Exit if any of r, g, b are greater than 255
if max(r, g, b) > 255:
    usage()

# Exit if value is > 100 or < 0
if v > 100 or v < 0:
    usage()

print("Setting Blinkt to value {v}, colour {r},{g},{b}".format(v=v, r=r, g=g, b=b))

blinkt.set_clear_on_exit(False)

blinkt.set_all(r, g, b, float(v) / 100)

blinkt.show()
