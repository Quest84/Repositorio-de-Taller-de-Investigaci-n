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

serialObj = serial.Serial( '/dev/ttyUSB0' )

target = "15"
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

            _, thresh = cv2.threshold( gray_img, 127, 255, 
                    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU )
            
            #cv2.imshow( "Imagen binaria", thresh )
            cv2.imwrite( "binaria.png", thresh )

            exit()
            
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
    #thread2 = Thread( target = main_tk, args = (12,))
    thread = Thread( target = arduino_loop, args = (12,))
    #thread2.start()
    thread.start()
    #tk.mainloop()
    exit()
