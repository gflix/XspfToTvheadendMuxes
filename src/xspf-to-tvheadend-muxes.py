#!/usr/bin/env python3

import sys
sys.path.append('@LIBDIR@/xspf-to-tvheadend-muxes')

from argparse import ArgumentParser
from tvheadend.access import Access, DEFAULT_TVHEADEND_PORT
from tvheadend.network import Network

def get_tvheadend_networks(access):
    if not isinstance(access, Access):
        raise TypeError('invalid arguments')

    raw_networks = access.request('mpegts/network/grid')

    if not isinstance(raw_networks, dict) or \
       not 'entries' in raw_networks or \
       not isinstance(raw_networks['entries'], list):
        raise TypeError('received invalid network list')

    networks = []

    for raw_network in raw_networks['entries']:
        networks.append(Network(raw_network))

    return networks

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
    tvheadend_networks = get_tvheadend_networks(tvheadend_access)

    if (arguments.networks):
        for network in tvheadend_networks:
            print(network.network_name)

        sys.exit(0)

    sys.exit(0)
