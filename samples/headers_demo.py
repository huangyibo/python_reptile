import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': '1287879608@qq.com', 'password': 'huangyibo'}
headers = {"User-Agent": user_agent, 'Referer': 'http://www.zhihu.com/articles' }
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
request.get_method = lambda: 'PUT' # or 'DELETE'

# set Debug Log
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen(request)
print response.read()



