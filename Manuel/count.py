from PIL import Image
import numpy as np
import cv2
import math

# Open image and ensure RGB

img = cv2.imread( 'iphone.png', 1 )

img_tmp = cv2.resize( img, ( 0.0 ), fx = 0.3, fy = 0.3 )

cv2.imwrite( 'iphone_resize.png', img_tmp )

img_r = Image.open('iphone_resize.png').convert('RGB')

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
print( counts[0] )

mm = counts[0]

print( "Medida en mm²: " )
mm = math.sqrt(mm)
print( mm )
