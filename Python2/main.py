# 
# THE SOdsf
import os
import sys
sys.path.append(u'/Users/A1/Documents/python3/KQR/')
import qrGenerator
import qrReader
import qrCamReader

u"""
this is the main
"""

	 	

def start_app(logged):
	clear = lambda: os.system(u'clear')
	clear()
	while logged== False:
		clear = lambda: os.system(u'clear')
		clear()
		print u"\t\n Welcome to \n Key Quick Response tags \n Management Keys System\n"
		print u"Log In \n"
		user = raw_input(u"user: ")
		password = raw_input(u"password: ")
		if user==u"admin" and password==u"1234":
			logged = True

	clear = lambda: os.system(u'clear')
	clear()

	print u"\t\n Welcome to \n Key Quick Response tags \n Management Keys System\n"
	print u"Menu:  \n1:QR code generator\n2:QR reader\n3:QR livecam reader (beta)\n4:Exit \n"

	data = u""
	while data != 1 or data != 2 or data != 3:
		data = raw_input(u"type: ")

		if data == u"1":
			qrGenerator.collect_data()
			start_app(True)
		elif data ==u"2":
			qrReader.main()
			start_app(True)
		elif data ==u"3":
			qrCamReader.main()
			start_app(True)
		elif data ==u"4":
			clear = lambda: os.system(u'clear')
			clear()
			exit()
		else:
			print u"Wrong input"
			start_app()

start_app(False)