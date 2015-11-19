import urllib
import urllib2
import cookielib

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = {"username": '3901120228', "password": "huangyibo"}
data = urllib.urlencode(postdata)
loginurl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login"
req = urllib2.Request(loginurl, data)
try:
	response = opener.open(req)
	cookie.save(ignore_discard=True, ignore_expires=True)
	gradeUrl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre"
	response = opener.open(gradeUrl)
	print response.read()
except urllib2.HTTPError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
except urllib2.URLError, e:
	print e.reason
else:
	print 'OK'
