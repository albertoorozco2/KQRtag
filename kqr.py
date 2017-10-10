import os
import QRG
import RTQR
import RTQRC

def start_app():
	clear = lambda: os.system('clear')
	clear()
	print("\n\nKK  KK  QQQQQ  RRRRRR  \nKK KK  QQ   QQ RR   RR \nKKKK   QQ   QQ RRRRRR  \nKK KK  QQ  QQ  RR  RR  \nKK  KK  QQQQ Q RR   RR \n\n\n")
	print("Welcome to KQR key system solution, \n choose an option:  \n1: to generate a QR code\n2: to read a QR tag\n3: to live reader QR tags")

	data = ""
	while data != 1 or data != 2 or data != 3:
		data = int(input("type: "))

		if data == 1:
			QRG.collect_data()
			start_app()
		elif data ==2:
			RTQR.main()
			print("comeback")
			start_app()
		elif data ==3:
			RTQRC.main()
		else:
			print("Wrong input")

start_app()