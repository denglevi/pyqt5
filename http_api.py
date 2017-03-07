# encoding=utf-8
import urllib.request
import urllib.parse
import simplejson


class HttpAPI:
    host = 'http://localhost'

    # host = 'http://150.95.150.47'

    def __init__(self):

        return

    def login(self, username, password):
        try:
            data = urllib.parse.urlencode({'username': username, 'password': password})
            data = data.encode('utf-8')
            res = urllib.request.urlopen(self.host + '/api/login', data)
            res = res.read().decode('utf-8')
            res = simplejson.loads(res)
            if res['success']:
                return True, res['data']

            return False, res['msg']
        except Exception as e:
            return False, str(e)
        return True
