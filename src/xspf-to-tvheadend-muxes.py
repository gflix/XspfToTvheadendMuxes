#!/usr/bin/env python3

import sys
sys.path.append('@LIBDIR@/xspf-to-tvheadend-muxes')

from argparse import ArgumentParser
from tvheadend.access import Access, DEFAULT_TVHEADEND_PORT
from tvheadend.network import Network
from xspf.playlist import Playlist
from xspf.track import Track

def get_tvheadend_networks(access):
    if not isinstance(access, Access):
        raise TypeError('invalid arguments')

    raw_networks = access.request('mpegts/network/grid')

    if not isinstance(raw_networks, dict) or \
       not 'entries' in raw_networks or \
       not isinstance(raw_networks['entries'], list):
        raise TypeError('received invalid network list')

    networks = {}

    for raw_network in raw_networks['entries']:
        network = Network(raw_network)
        networks[network.network_name] = network

    return networks

def create_mux(access, network, network_interface, track):
    if not isinstance(access, Access) or \
       not isinstance(network, Network) or \
       not isinstance(network_interface, str) or \
       not isinstance(track, Track):
        raise TypeError('invalid arguments')

    print('Creating mux "%s"...' % track.title)

    data = {
        'uuid': network.uuid,
        'conf': {
            'iptv_interface': network_interface,
            'iptv_muxname': track.title,
            'iptv_url': track.location,
            'name': track.title,
            'iptv_icon': track.image
        }
    }

    access.request('mpegts/network/mux_create', data)

def create_muxes(access, network, network_interface, playlist):
    if not isinstance(playlist, Playlist):
        raise TypeError('invalid arguments')

    for track in playlist.tracks:
        create_mux(access, network, network_interface, track)

if __name__ == '__main__':

    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        'host',
        metavar='HOST[:PORT]',
        help='host name and optional port for accessing Tvheadend (default: %d)' % DEFAULT_TVHEADEND_PORT)
    argument_parser.add_argument(
        'network',
        metavar='NETWORK',
        help='network to which the muxes are addes',
        nargs='?')
    argument_parser.add_argument(
        'interface',
        metavar='INTERFACE',
        help='network interface',
        nargs='?')
    argument_parser.add_argument(
        'xspf',
        metavar='XSPF',
        help='XSPF playlist',
        nargs='?')
    argument_parser.add_argument('-u', '--username', help='username')
    argument_parser.add_argument('-p', '--password', help='password')
    argument_parser.add_argument('-n', '--networks', help='list the available networks', action='store_true')

    arguments = argument_parser.parse_args()

    if not arguments.networks:
        if not arguments.network:
            raise ValueError('network argument is missing')

        if not arguments.interface:
            raise ValueError('network interface argument is missing')

        if not arguments.xspf:
            raise ValueError('XSPF argument is missing')

    tvheadend_access = Access(arguments.host, arguments.username, arguments.password)
    tvheadend_networks = get_tvheadend_networks(tvheadend_access)

    if (arguments.networks):
        for network_name in tvheadend_networks.keys():
            print(network_name)

        sys.exit(0)

    if not arguments.network in tvheadend_networks:
        raise ValueError('unknown network "%s"' % arguments.network)

    tvheadend_network = tvheadend_networks[arguments.network]

    playlist = Playlist(arguments.xspf)
    print(playlist.title)
    print(playlist.info)
    print(len(playlist.tracks))

    create_muxes(tvheadend_access, tvheadend_network, arguments.interface, playlist)

    sys.exit(0)
