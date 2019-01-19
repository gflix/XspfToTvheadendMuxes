#!/usr/bin/env python3

import sys
sys.path.append('@LIBDIR@/xspf-to-tvheadend-muxes')

from pkg.xspf import Xspf

if __name__ == '__main__':
    xspf = Xspf()
    sys.exit(0)
