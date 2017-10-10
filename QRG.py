import qrcode
import os
   #https://prasopensource.wordpress.com/2013/01/18/generating-qrcodes-from-python/
def create_QRtag(data, QR_size, QR_border):
    #gets input from user to encode into qrcode
    #data = input("Type to create QRCode: ") 
    #initialize settings for Output Qrcode
    print("#initialize settings for Output Qrcode")
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=QR_size, border=QR_border,) 

    #adds the data to the qr cursor
    print("#adds the data")
    qr.add_data(data) 
    print("#create QRtag")
    qr.make(fit=True)
    img = qr.make_image()
    file_extension = "JPEG"
    file_name = data+'.'+file_extension

    #will open the file, if file does not exist, it will be created and opened.
    image_file = open(file_name,'w+') 
    #write qrcode encoded data to the image file.
    print("#create file")
    img.save(image_file,file_extension.upper()) 
    #close the opened file handler.
    print("#QRtag imagen saved")
    img.show()     
    print("#QRtag will display")
    image_file.close() 

def collect_data():
    clear = lambda: os.system('clear')
    clear()

    data = input("Data to QRCode: ")
    box_size = input("Size of tag (press Enter to default 15mm): ")
    if box_size =="":
        box_size = 2
    else:
        box_size = int(float(box_size)/7.41)
    border = input("Size of border (press Enter to default 1.5mm): ") 
    if border =="":
        border = 1
    else:
        border = int(float(border)/1.41)

    create_QRtag(data, box_size, border)

    back_main = input("Type any key to comeback main menu: ")
    




