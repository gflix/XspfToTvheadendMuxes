from xml.etree import ElementTree as etree

NAMESPACE = '{http://xspf.org/ns/0/}'
TAG_IMAGE = NAMESPACE + 'image'
TAG_LOCATION = NAMESPACE + 'location'
TAG_TITLE = NAMESPACE + 'title'
TAG_TRACK_NUM = NAMESPACE + 'trackNum'

class Track(object):

    def __init__(self, node):
        self.load(node)

    def load(self, node):
        if not isinstance(node, etree.Element):
            raise TypeError('Track: invalid arguments')

        self.title = node.find(TAG_TITLE).text
        self.track_number = int(node.find(TAG_TRACK_NUM).text)
        self.location = node.find(TAG_LOCATION).text
        self.image = node.find(TAG_IMAGE).text
