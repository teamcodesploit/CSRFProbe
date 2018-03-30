#!/usr/bin/env python2
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import urllib2
from BeautifulSoup import BeautifulSoup
import Uri_Checker
import re
from colors import *

class Crawler_Handler():

	def __init__(self, start,opener):

		self.visited = []
		self.toVisit = []
		self.uriPatterns = []
		self.currentURI = '';
		self.opener = opener;
		self.toVisit.append(start)

	def next(self):
		self.currentURI = self.toVisit[0]
		self.toVisit.remove(self.currentURI)
		return self.currentURI

	def getVisited(self):
		return self.visited

	def getToVisit(self):
		return self.toVisit

	def noinit(self):
		if len(self.toVisit)>0:
			return True
		else:
			return False

	def addToVisit(self,Uri_Checker):
		self.toVisit.append(Uri_Checker)
		
	def process(self, root):
		url = self.currentURI

		try:
			query = self.opener.open(url)

		except urllib2.HTTPError, msg:
			print R+' [-] Request Error: '+msg.__str__()
			if url in self.toVisit:
				self.toVisit.remove(url)
			return

		if not re.search('html',query.info()['Content-Type']):
			return

		print GR+' [*] Making request to new location...'
		if hasattr(query.info(),'Location'):
			url=query.info()['Location']
		print C+' [*] Reading response...'
		response = query.read()

		try:
			print O+' [*] Trying to parse response...'
			soup = BeautifulSoup(response)

		except HTMLParser.HTMLParseError:
			print R+' [-] BeautifulSoup Error: '+url
			self.visited.append(url)

			if url in self.toVisit:
				self.toVisit.remove(url)
			return

		for m in soup.findAll('a',href=True):
			app=''
			if not re.match(r'javascript:',m['href']) or re.match('http://',m['href']):
				app = Uri_Checker.buildUrl(url,m['href'])
			if app!='' and re.search(root, app):
				while re.search(r'/\.\./',app):
					p = re.compile('/[^/]*/../')
					app = p.sub('/',app)
				p = re.compile('\./')
				app = p.sub('',app)

				uriPattern=removeIDs(app)
				if self.notExist(uriPattern) and app!=url:
					print G+' [+] Added :> ' +O+ app
					self.toVisit.append(app)
					self.uriPatterns.append(uriPattern)
		self.visited.append(url)
		return soup

	def getUriPatterns(self):
		return self.uriPatterns

	def notExist(self, test):

		if (test not in self.uriPatterns):
			return 1
		return 0

	def addUriPatterns(self,Uri_Checker):
		self.uriPatterns.append(Uri_Checker)

	def addVisited(self,Uri_Checker):
		self.visited.append(Uri_Checker)

def removeIDs(Uri_Checker):

	p = re.compile('=[0-9]+')
	Uri_Checker = p.sub('=',Uri_Checker)
	p = re.compile('(title=)[^&]*')
	Uri_Checker = p.sub('\\1',Uri_Checker)
	return Uri_Checker
