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

	# the method to open debug model
	def openDebug(self):
		httpHandler = urllib2.HTTPHandler(debuglevel=1)
		httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
		opener = urllib2.build_opener(httpHandler,httpsHandler)
		urllib2.install_opener(opener)

	# the method to get html page code : pageIndex
	def getPage(self, pageIndex):
		try:
			url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
			# build request
			request = urllib2.Request(url,headers=self.headers)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"connect failed, the reason is :",e.reason
				return None

	# get PageItems method : pageIndex as param
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "load html page failed..."
			return None
		pattern = re.compile( '' , re.S)		
		items = re.findall(pattern, pageCode)
		pageStories = []
		for item in items:
			# whether have image
			hasImg = re.search("img", item[3])
			if not hasImg:
				replaceBR = re.compile("<br/>")
				text = re.sub(replaceBR,"\n", item[1])
				pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[3].strip()])
		return pageStories


	# loadPage to self.stories
	def loadPage(self):
		# load new page if the pages is less than 2 
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	# get a story by "enter": pageStories as page stories list, page as the current page number
	def getOneStory(self, pageStories,page):
		for item in pageStories:
			# wait for the input of user
			input = raw_input()
			# load page every time "enter"
			self.loadPage()
			if input == "Q"
				print "end to get story from QiuShiBaiKe..."
				self.enable = False
				return 
			print u"Page %d \t author:%s \t date:%s \t Goods:%s \t\n Content:%s" %(page, item[0],item[2],item[3],item[1])

	# start method 
	def start(self):
		print u"reading QiuShiBaiKe, enter to read new item, Q to quit"
		# enable self.enable to True
		self.enable = True
		nowPage = 0
		self.loadPage()
		while self.enable:
			pageStories = self.stories[0]
			nowPage += 1
			del self.stories[0]
			self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()











			
		except urllib2.URLError, e:
		










