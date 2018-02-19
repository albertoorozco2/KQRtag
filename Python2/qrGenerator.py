
'''QRG is a module that integrate an input from the user to generate and store QR codes in JPG format.'''

import qrcode
import os
   
def collect_data():
    ''' function to collect data from the user to create the qr tag, the user type the data that want to be encoded in qr tag
    and the prefer size, by default the size of qr tag is 15mm and the border 1.5mm '''

    clear = lambda: os.system('clear')
    clear()

    data = eval(input("Data to QRCode: "))
    box_size = eval(input("Size of tag (press Enter to default 15mm): "))
    if box_size =="":
        box_size = 2
    else:
        box_size = int(float(box_size)/7.41)
    border = eval(input("Size of border (press Enter to default 1.5mm): ")) 
    if border =="":
        border = 1
    else:
        border = int(float(border)/1.41)

    create_QRtag(data, box_size, border)

    back_main = eval(input("Type any key to comeback main menu: "))
    



def create_QRtag(data, QR_size, QR_border):

    ''' 
    function to generate a qr tag, with the any data input and customizable size and border 
    <br>@param data: data to encode in the qr tag
    <br>@param QR_size: qr size for the qr tag
    <br>@param QR_border: border size around of the qr tag
    <br><br>this function is from <a href="https://prasopensource.wordpress.com/2013/01/18/generating-qrcodes-from-python/"> prasopensource: Generating QRCodes from Python<a/>.'''
    

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
    image_file = open("qrGenerated/"+file_name,'w+') 
    #write qrcode encoded data to the image file.
    print("#create file")
    img.save(image_file,file_extension.upper()) 
    #close the opened file handler.
    print("#QRtag imagen saved")
    img.show()     
    print("#QRtag will display")
    image_file.close() 




