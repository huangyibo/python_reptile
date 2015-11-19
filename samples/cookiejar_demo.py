import cookielib
import urllib2

# delare a Cookiejar object instance to save cookie
cookie = cookielib.CookieJar()
# use the HTTPCookieProcessor object of urllib2 lib to build cookie processor
handler = urllib2.HTTPCookieProcessor(cookie)
# build opener by handler
opener = urllib2.build_opener(handler)
# open method of opener object is the same as urlopen method of urllib2 in which request is param
response = opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value


