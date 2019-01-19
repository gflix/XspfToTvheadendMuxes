#!/usr/bin/env python3

import sys
sys.path.append('@LIBDIR@/xspf-to-tvheadend-muxes')

from argparse import ArgumentParser
from tvheadend.access import Access, DEFAULT_TVHEADEND_PORT
from tvheadend.network import Network

if __name__ == '__main__':

    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        'host',
        metavar='HOST[:PORT]',
        help='host name and optional port for accessing Tvheadend (default: %d)' % DEFAULT_TVHEADEND_PORT)
    argument_parser.add_argument('-u', '--username', help='username')
    argument_parser.add_argument('-p', '--password', help='password')
    argument_parser.add_argument('-n', '--networks', help='list the available networks', action='store_true')

    arguments = argument_parser.parse_args()

    tvheadend_access = Access(arguments.host, arguments.username, arguments.password)

    sys.exit(0)
