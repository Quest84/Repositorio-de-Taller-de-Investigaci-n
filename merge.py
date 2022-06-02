# Librerías para Tomar y filtrar la foto
import cv2
import numpy as np

from PIL import Image

# Librerías para Arduino y Threads
import serial
import time
from threading import Thread
from time import sleep
from tkinter import *

tk = Tk()

serialObj = serial.Serial( '/dev/ttyACM0' )

target = "30"
print( "Distance Target: " + target )

output = "test"

def arduino_loop( arg ):
    global output
    while True:
        temp = serialObj.readline()
        temp = str(temp)

        output = ''.join(filter(str.isdigit, temp))

        print( output )
        if output == target:
            print( "bingo!" )
            #Tomar la foto y procesarla
            cap = cv2.VideoCapture(0)

            leido, frame = cap.read()

            if leido == True:
                cv2.imwrite( "foto.png", frame )
                print( "Foto tomada a la distancia correcta" )
            else:
                print( "No se puede acceder a la camara" )
            
            cap.release()
            img = cv2.imread( 'foto.png' )

            #cv2.imshow( "Imagen Original", img )
            gray_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

            _, thresh = cv2.threshold( gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )
            
            #cv2.imshow( "Imagen binaria", thresh )
            cv2.imwrite( "binaria.png", thresh )
            img_contours = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )[-2]
            img_contours = sorted( img_contours, key = cv2.contourArea )

            for i in img_contours:
                if cv2.contourArea(i) > 100:
                    break

            mask = np.zeros( img.shape[:2], np.uint8 ) 
            cv2.drawContours( mask, [i], -1, 255, -1 )
            new_img = cv2.bitwise_and( img, img, mask=mask )

            #cv2.imshow("resultado", new_img)
            #cv2.imwrite("nueva.png", new_img)

            #img = cv2.imread( 'nueva.png', 1 )
            exit()
                
            #img_r = Image.open( 'nueva.png' ).convert('RGB')
            
def main_tk( arg ):
    global output
    global tk
    l = Label(tk)
    l.pack()

    e = Entry(tk)
    e.pack()

    def submit():
        l.configure( text = output )
        l.configure( text = e.get() )
        print( e.get() )

    Button( text="Click!", command=submit ).pack()

if __name__ == "__main__":
    thread2 = Thread( target = main_tk, args = (12,))
    thread = Thread( target = arduino_loop, args = (12,))
    thread2.start()
    thread.start()
    tk.mainloop()
