from PIL import Image
import numpy as np
import cv2
import math

# Open image and ensure RGB

#img = cv2.imread( 'square.png', 1 )

img_r = Image.open('binaria.png').convert('RGB')

width, height = img_r.size

# Make into Numpy array
na = np.array(img_r)

# Get colours and corresponding counts
colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)

print( "Ancho: " + str(width) + "px" )
print( "Alto: " + str(height) + "px")

print("Colores: ")
print( colours )

print("Conteo en px: ")
print( counts[1] )

mm = counts[1]

print( "Medida en mm²: " )
mm = math.sqrt(mm)

mm = (mm/40)*10
#mm = mm*mm
print( mm )

with open('Medidas.csv', 'a') as f:
    f.write( str(counts[1]) )
    f.write('\n')
