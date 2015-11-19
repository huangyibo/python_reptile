__author__ = 'huangyibo'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

# define QSBK class
class QSBK:

	# init method, define some variables
	def __init__(self):
		self.pageIndex =1
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
		# init headers
		self.headers = { 'User-Agent': self.user_agent}
		# a list to store page content items
		self.stories = []
		#the variable to control whether program is going on
		self.enable = False

	# the method to get html page code : pageIndex
	def getPage(self, pageIndex):
		try:
			url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
		# build request
		request = urllib2.Request(url,headers=self.headers)




	# get PageItems method : pageIndex as param
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)







	# loadPage to self.stories
	def loadPage(self):
		# load new page if the pages is less than 2 
		if self.enable == True:
			if len(self.stories) < 2:


	# start method 
	def start(self):
		print u"reading QiuShiBaiKe, enter to read new item, Q to quit"
		# enable self.enable to True
		self.enable = True


spider = QSBK()
spider.start()











			
		except urllib2.URLError, e:
		










