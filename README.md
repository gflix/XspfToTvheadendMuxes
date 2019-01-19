# XspfToTvheadendMuxes
Generates IPTV muxes from a XSPF playlist for Tvheadend

This simple tool allows to import XSPF playlists for IPTV streams to Tvheadend.
It was especially made for the Telekom Entertain TV product by using the playlists
taken from https://iptv.blog/artikel/multicastadressliste/ .

Build instructions

automake -Wall -i
./configure
make
sudo make install

Usage

First retrieve the list of networks which are already defined within Tvheadend:

xspf-to-tvheadend-muxes -u USERNAME -p PASSWORD tvheadend.server -n

Pick the network which was created for IPTV streams (i.e. "Magenta TV") and import the
muxes as follows:

xspf-to-tvheadend-muxes -u USERNAME -p PASSWORD tvheadend.server eth0 playlist.xspf

Modify the arguments to fit to your needs.
