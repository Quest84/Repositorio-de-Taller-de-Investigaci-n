from PIL import Image
import numpy as np
import math

# Open image and ensure RGB
im = Image.open('test.png').convert('RGB')

# Make into Numpy array
na = np.array(im)

# Get colours and corresponding counts
colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)

print("Colores: ")
print( colours )

print("Conteo en px: ")
print( counts[0] )

mm = 0
mm = counts[0]

print( "Medida en mm²: " )
mm = math.sqrt(mm)
print( mm )
