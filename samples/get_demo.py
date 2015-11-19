import urllib
import urllib2

values={}
values['username'] = "1287879608@qq.com"
values['password'] = "huangyibo"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print reponse.read()

