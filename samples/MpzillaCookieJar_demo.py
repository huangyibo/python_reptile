import urllib2
import cookielib

# create MozillaCookieJar Object
cookie = cookielib.MozillaCookieJar()
# read cookie content into variable from file
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)
# build request 
req = urllib2.Request("http://www.baidu.com")
# use build_opener method of urllib2 to build opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# use opener object to open
response = opener.open(req)
print response.read()

