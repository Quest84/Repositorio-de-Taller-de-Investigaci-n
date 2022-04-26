import serial
import time
from threading import Thread
from time import sleep
from tkinter import *
tk = Tk()

serialObj = serial.Serial( '/dev/ttyACM0' )
target = "15"
print( "Distance Target: " + target )

output = "test"

def arduino_loop(arg):
    global output
    while True:
        temp = serialObj.readline()
        temp = str(temp)

        output = ''.join(filter(str.isdigit, temp))
        
        print( output )

        if output == target:
            print( "Bingo!" )

def main_tk(arg):
    global output
    global tk
    l = Label(tk)
    l.pack()

    e = Entry(tk)
    e.pack()
    
    def submit():
        l.configure( text  = output )
        l.configure(text = e.get())
    
    Button(text="Click!",command=submit).pack()
 
if __name__ == "__main__":
    thread2 = Thread(target = main_tk, args = (12,))
    thread = Thread(target = arduino_loop, args = (12,))
    thread2.start()
    thread.start()
    tk.mainloop()
    
