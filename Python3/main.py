# 
# THE SOdsf
import os
import sys
sys.path.append('/Users/A1/Documents/python3/KQR/')
import qrGenerator
import qrReader
import qrCamReader

"""
this is the main
"""

	 	

def start_app():
	logged = False

	clear = lambda: os.system('clear')
	clear()

	while logged== False:
		clear = lambda: os.system('clear')
		clear()
		print("\t\n\n██╗  ██╗ ██████╗ ██████╗          \t\n██║ ██╔╝██╔═══██╗██╔══██╗         \t\n█████╔╝ ██║   ██║██████╔╝         \t\n██╔═██╗ ██║▄▄ ██║██╔══██╗         \t\n██║  ██╗╚██████╔╝██║  ██║         \t\n╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝  ")
		print("\t\n Welcome to \n Key Quick Response tags \n Management Keys System\n")
		print("Log In \n")
		user = input("user: ")
		password = input("password: ")
		if user=="admin" and password=="1234":
			logged = True

	clear = lambda: os.system('clear')
	clear()

	print("\t\n\n██╗  ██╗ ██████╗ ██████╗          \t\n██║ ██╔╝██╔═══██╗██╔══██╗         \t\n█████╔╝ ██║   ██║██████╔╝         \t\n██╔═██╗ ██║▄▄ ██║██╔══██╗         \t\n██║  ██╗╚██████╔╝██║  ██║         \t\n╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝  ")
	print("\t\n Welcome to \n Key Quick Response tags \n Management Keys System\n")
	print("Menu:  \n1:QR code generator\n2:QR reader\n3:QR livecam reader (beta)\n4:Exit \n")

	data = ""
	while data != 1 or data != 2 or data != 3:
		data = input("type: ")

		if data == "1":
			qrGenerator.collect_data()
			start_app()
		elif data =="2":
			qrReader.main()
			start_app()
		elif data =="3":
			qrCamReader.main()
			start_app()
		elif data =="4":
			clear = lambda: os.system('clear')
			clear()
			exit()
		else:
			print("Wrong input")
			start_app()

start_app()