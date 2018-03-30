#!/usr/bin/env python2
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import sys
sys.path.append('core/')
from impo import *
from globalvars import *

try:
    csrf_main()

except urllib2.HTTPError as e:
	print R+' [-] HTTP Authentication Error!'
	print R+' [!] Error Code : ' +O+ str(e.code)

except KeyboardInterrupt:
	print R+' [-] User Interrupt!'
	print R+' [!] Aborted!'
