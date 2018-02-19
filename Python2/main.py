# 
# THE SOdsf
import os
import sys
sys.path.append(u'/Users/A1/Documents/python3/KQR/')
import qrGenerator
import qrReader
import qrCamReader

"""
this is the main
"""

def start_app():
	clear = lambda: os.system(u'clear')
	clear()

	print u"\n_   _____________ \n| | / /  _  | ___ \\n| |/ /| | | | |_/ /\n|    \| | | |    / \n| |\  \ \/' / |\ \ \n\_| \_/\_/\_\_| \_|"
	print u"\t\n Welcome to \n Key Quick Response tags \n Management Keys System\n"
	print u"Menu:  \n1:QR code generator\n2:QR reader\n3:QR livecam reader (beta)\n4:Exit \n"

	data = u""
	while data != 1 or data != 2 or data != 3:
		data = raw_input(u"type: ")

		if data == u"1":
			qrGenerator.collect_data()
			start_app()
		elif data ==u"2":
			qrReader.main()
			start_app()
		elif data ==u"3":
			qrCamReader.main()
			start_app()
		elif data ==u"4":
			clear = lambda: os.system(u'clear')
			clear()
			exit()
		else:
			print u"Wrong input"
			start_app()

start_app()