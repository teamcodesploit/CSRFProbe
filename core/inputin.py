#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    XSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires XSRF-Probe
#https://github.com/the-Infected-Drake/XSRF-Probe

from colors import *

def inputin():

	web = raw_input(C+' [$] Enter target address :> '+G)

	if 'http' not in web:
		web = 'http://' + web
	return web
