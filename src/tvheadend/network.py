TAG_NETWORKNAME = 'networkname'
TAG_UUID = 'uuid'

class Network(object):

    def __init__(self, data):
        self.load(data)

    def load(self, data):
        if not isinstance(data, dict):
            raise TypeError('Network: invalid arguments')

        if not TAG_UUID in data or \
           not TAG_NETWORKNAME in data or \
           not isinstance(data[TAG_UUID], str) or \
           not isinstance(data[TAG_NETWORKNAME], str):
           raise ValueError('Network: invalid data object')

        self.uuid = data[TAG_UUID]
        self.network_name = data[TAG_NETWORKNAME]
