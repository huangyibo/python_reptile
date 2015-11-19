import urllib2
import cookielib

# set the target file to save cookie
filename = 'cookie.txt'
# delare a MozillaCookieJar Object to save Cookiem , and then write into file
cookie = cookielib.MozillaCookieJar(filename)
# use HTTPCookieProcessor Object of urllib2 to buid cookie handler
handler = urllib2.HTTPCookieProcessor(cookie)
# build opener by handler
opener = urllib2.build_opener(handler)
# build request 
response = opener.open('http://www.baidu.com')
# save cookie to file
cookie.save(ignore_discard=True, ignore_expires=True)

