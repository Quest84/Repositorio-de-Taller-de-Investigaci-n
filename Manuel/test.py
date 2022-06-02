import serial
import tkinter

# Inicializa el serial
#SerialObj = serial.Serial( '/dev/ttyACM0' )

Distance = "15"
print( "Distance target: " + Distance )

ventana = tkinter.Tk()
ventana.geometry( "500x500" )

label = tkinter.Label( ventana, text = "TestTestTest", bg = "white" )
label.pack( fill = tkinter.X )

def my_mainloop():
    Output = SerialObj.readline()
    Temp = str(Output)
 
    Temp = ''.join(filter(str.isdigit, Temp))
    print( Temp )
 
    if Distance == Temp:
        #print( "Bingo no." + str(x) + "\n" )
        print( "Bingo!" )
 
    ventana.after( 1, my_mainloop )

ventana.after( 1, my_mainloop )

ventana.mainloop()
