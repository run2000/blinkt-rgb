#!/usr/bin/env python

import sys

import blinkt 

verbose = False

def usage():
    print("Usage: {} <r> <g> <b>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) == 4:
    # Exit if non integer value. int() will raise a ValueError
    try:
        r, g, b = [int(x) for x in sys.argv[1:]]
    except ValueError:
        usage()

elif len(sys.argv) == 2:
    # Try #rrggbb value
    value = sys.argv[1].lstrip('#')
    try:
        r, g, b = tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        usage()

else:
    usage()

# Exit if any of r, g, b are greater than 255
if max(r, g, b) > 255:
    usage()

if verbose:
    print("Setting Blinkt to {r},{g},{b}".format(r=r, g=g, b=b))

blinkt.set_clear_on_exit(False)

blinkt.set_all(r, g, b)

blinkt.show()
