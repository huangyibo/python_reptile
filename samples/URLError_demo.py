import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)

request = urllib2.Request('http://www.xxxyyy324543.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason
