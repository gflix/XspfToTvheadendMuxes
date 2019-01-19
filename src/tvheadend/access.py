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
