import urllib
import urllib2

values = {}
values['username'] = "1287879608@qq.com"
values['password'] = "huangyibo"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print reponse.read()
