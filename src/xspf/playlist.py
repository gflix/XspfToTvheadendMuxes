from xml.etree import ElementTree as etree
from xspf.track import Track

NAMESPACE = '{http://xspf.org/ns/0/}'
TAG_INFO = NAMESPACE + 'info'
TAG_PLAYLIST = NAMESPACE + 'playlist'
TAG_TITLE = NAMESPACE + 'title'
TAG_TRACK = NAMESPACE + 'track'
TAG_TRACK_LIST = NAMESPACE + 'trackList'

class Playlist(object):

    def __init__(self, xspf):
        self.load(xspf)

    def load(self, xspf):
        if not isinstance(xspf, str):
            TypeError('Playlist: invalid arguments')

        self.title = None
        self.info = None
        self.tracks = []

        root = etree.parse(xspf).getroot()

        if root.tag != TAG_PLAYLIST:
            raise ValueError('Playlist: invalid XML file (%s)' % root.tag)

        self.title = root.find(TAG_TITLE).text
        self.info = root.find(TAG_INFO).text

        for track_node in root.findall('%s/%s' % (TAG_TRACK_LIST, TAG_TRACK)):
            self.tracks.append(Track(track_node))
