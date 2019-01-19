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

    @staticmethod
    def to_request_data(data):
        if isinstance(data, dict):
            request_data = {}

            for key in data.keys():
                entry = data[key]

                if isinstance(entry, str):
                    request_data[key] = entry
                elif isinstance(entry, dict):
                    request_data[key] = json.dumps(entry, sort_keys=True)
                else:
                    raise TypeError('data entry not supported')

            return request_data
        else:
            return None

    def request(self, endpoint, data=None):
        url = self.api_url(endpoint)
        auth = None
        if self.username and self.password:
            auth = HTTPDigestAuth(self.username, self.password)

        request_data = self.to_request_data(data)
        if not request_data:
            response = requests.get(url, auth=auth)
        else:
            response = requests.post(url, auth=auth, data=request_data)

        if response.status_code != 200:
            raise IOError('request to endpoint "%s" returned code %d, expecting 200' %
                          (endpoint, response.status_code))

        return json.loads(response.text)
