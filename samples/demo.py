import urllib2

reponse = urllib2.urlopen("http://www.baidu.com")
print reponse.read()
