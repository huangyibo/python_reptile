# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
headers = { 'User-Agent' : user_agent }

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)

try:
	request = urllib2.Request(url,headers =  headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	print content
#	pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?class="content">(.*?)<!--(.*?)-->'+'</div>(.*?)<div class="stats.*?number">(.*?)</i>', re.S)
	pattern = re.compile('<div.*?author.*?<a.*?<img.*?</a><a.*?<h2>(.*?)</h2>.*?</div>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?number">(.*?)</i>', re.S)
#	pattern = re.compile('<div.*?author.*?<a.*?<img.*?</a><a.*?</h2>(.*?)</h2>', re.S)
	print 're.compile end'
	items = re.findall(pattern, content)
	print items
	print 're.findall end'
	for item in items:
		print item[0]
#		hasImage = re.search('img', item[3])
#		if not hasImage:
#			print item[0],item[1],item[2],item[4]	
except urllib2.HTTPError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason 	
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason


