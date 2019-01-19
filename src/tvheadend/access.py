import json
import requests
from requests.auth import HTTPDigestAuth

DEFAULT_TVHEADEND_PORT = 9981

class Access(object):

    def __init__(self, host, username, password):
        if not isinstance(host, str):
           raise TypeError('Access: invalid arguments')

        host_parts = host.split(':')
        if len(host_parts) == 1:
            self.host = host_parts[0]
            self.port = DEFAULT_TVHEADEND_PORT
        elif len(host_parts) == 2:
            self.host = host_parts[0]
            self.port = int(host_parts[1])
        else:
            raise ValueError('Access: invalid host argument')

        self.username = username
        self.password = password

    def api_url(self, endpoint):
        if not isinstance(endpoint, str):
            raise TypeError('invalid endpoint')

        return 'http://%s:%d/api/%s' % (self.host, self.port, endpoint)

    def request(self, endpoint):
        url = self.api_url(endpoint)
        auth = None
        if self.username and self.password:
            auth = HTTPDigestAuth(self.username, self.password)

        response = requests.get(url, auth=auth)

        if response.status_code != 200:
            raise IOError('request to endpoint "%s" returned code %d, expecting 200' %
                          (endpoint, response.status_code))

        return json.loads(response.text)
