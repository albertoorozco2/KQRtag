''' RTQRC - live cam QR tag reader, this is a module that is capable of use the webcam as reader for qr tags , when a QR tag is readed, it display the data if it is stored in the system, 
otherwise display only the data readed from the QR tag and continued readed until q is press on the keyboard '''

#lybrary from https://github.com/allenywang/Real-Time-QR-Recognizer-Reader-and-Decoder
import os
from PIL import Image
import zbar


import cv2

keys_data = {"cct9999" : "\n    Name: Oconolly room \n    Description: main dor on the righ side",
             "cct0234" : "\n    Name: reception room \n    Description: second door in the main entrance",
             "cct0003" : "\n    Name: locker in room \n    Description: red locker on the right", 
             "cct0004" : "\n    Name: main door\n     Description: the big door ", 
             "cct0005" : "\n    Name: front desk\n     Description: big draw"}
'''
temporal key values in the code to retrieve the data when a QR tag is readed

'''

def main():
    '''
    A simple function that captures webcam video utilizing OpenCV. The video is then broken down into frames which
    are constantly displayed. The frame is then converted to grayscale for better contrast. Afterwards, the image
    is transformed into a numpy array using PIL. This is needed to create zbar image. This zbar image is then scanned
    utilizing zbar's image scanner and will then print the decodeed message of any QR or bar code. To quit the program,
    press q.
        <br><br>this function is from <a href="https://github.com/allenywang/Real-Time-QR-Recognizer-Reader-and-Decoder"> allenywang - Real Time QR Recognizer Reader and Decoder
<a/>.

    '''
    clear = lambda: os.system('clear')

    print('\n\n\n\n\n\n    Place QR infront of the camera')


    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    capture = cv2.VideoCapture(0)
    stop = ""
    while True:
        # To quit this program press q.
        if cv2.waitKey(1) | 0xFF == ord('q'):
            break

        if stop != "":
            cv2.destroyAllWindows()
            break
        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow('Current', frame)

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
            clear = lambda: os.system('clear')
            clear()
            print("\n\n\n\n\n")
            newstr = str(result.data).replace("b'", "").replace("'","")
            print("    "+newstr)
            print("\n\n")

            if newstr in keys_data:
                print('    key in database KQRtag')
                print("    "+keys_data.get(newstr))

            else:
                print('\n\n    no key with the QRtag')


            print("\n\n\n\n\n press Ctrl+C to quit program")



        # # Prints data from image.
        # for decoded in zbar_image:
        #     print(decoded.data)

    


if __name__ == "__main__":
    main()
