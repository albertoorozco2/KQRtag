u''' RTQR - QR tag reader, is a module that is capable of use the webcam as reader for qr tags , when a QR tag is readed the module stops and display the data stored in the system, 
this prototype version is using variables set in the code, but eventually will be store and retrive from a database from cloud '''
from __future__ import absolute_import
import os
from PIL import Image
import zbar
import time


import cv2

keys_data = {u"b'cct0001'" : u"\n    Name: Oconolly room \n    Description: main dor on the righ side",
             u"b'cct0002'" : u"\n    Name: reception room \n    Description: second door in the main entrance",
             u"b'cct0003'" : u"\n    Name: locker in room \n    Description: red locker on the right", 
             u"b'cct0004'" : u"\n    Name: main door\n     Description: the big door ", 
             u"b'cct0005'" : u"\n    Name: front desk\n     Description: big draw"}
u'''
temporal key values in the code to retrieve the data when a QR tag is readed

'''
def main():


    u'''
    A simple function that captures webcam video utilizing OpenCV. The video is then broken down into frames which
    are constantly displayed. The frame is then converted to grayscale for better contrast. Afterwards, the image
    is transformed into a numpy array using PIL. This is needed to create zbar image. This zbar image is then scanned
    utilizing zbar's image scanner and will then print the decodeed message of any QR or bar code and quit the reader.
        <br><br>this function is from <a href="https://github.com/allenywang/Real-Time-QR-Recognizer-Reader-and-Decoder"> allenywang - Real Time QR Recognizer Reader and Decoder
<a/>.

    '''

    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    clear = lambda: os.system(u'clear')

    print u'\n\n\n\n    Place QR infront of the camera'

    capture = cv2.VideoCapture(0)
    stop = u""
    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord(u'q'):
            cv2.destroyAllWindows()
            break

        if stop != u"":
            cv2.destroyAllWindows()
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow(u'Current', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #mumpy array ^^^


        #code for python2
        # # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        # image = Image.fromarray(gray)
        # width, height = image.size
        # zbar_image = zbar.Image(width, height, 'Y800', image.tostring())

        # # Scans the zbar image.
        # scanner = zbar.ImageScanner()
        # scanner.scan(zbar_image)


        #fixed for python3
        image = gray # whatever function you use to read an image file into a numpy array
        scanner = zbar.Scanner()
        results = scanner.scan(image)
        for result in results:
            #print(result.type, result.data, result.quality, result.position) 
            clear = lambda: os.system(u'clear')
            clear()
            print u"\n\n\n\n\n    "
            print u"    "+unicode(result.data)
            if unicode(result.data) in keys_data:
                print u'    key in database KQRtag'
                print u"    "+keys_data.get(unicode(result.data))
            else:
                print unicode(result.data)
                print u'no key with the QRtag'

            print u'\n\n5sec to comeback main menu'
            time.sleep(5)
            stop = unicode(result.data)

        # # Prints data from image.
        # for decoded in zbar_image:
        #     print(decoded.data)

    


if __name__ == u"__main__":
    main()
