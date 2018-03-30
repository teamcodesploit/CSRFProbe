#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    XSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires XSRF-Probe
#https://github.com/the-Infected-Drake/XSRF-Probe

import urllib
from impo import *

def request(referer,action,form,opener):

	data = urllib.urlencode(form)
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)','Referer' : referer}
	try:
		return opener.open(action,data).read()

	except urllib2.HTTPError:
		print "HTTP Error 1: "+action
		return

	except ValueError:
		print "Value Error: "+action
		return

	except:
		return ''
