import cv2 
import numpy as np

from PIL import Image

cap = cv2.VideoCapture(0)
#cap = cv2.imrea md('foto.png')

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("foto.png", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

"""
	#Finalmente liberamos o soltamos la cámara
"""

cap.release()
img = cv2.imread('images.jpg')
#img = cv2.imread("foto.png")
cv2.imshow("IMAGEN ORIGINAL", img)

#conversion a escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("IMAGEN EN ESCALA DE GRISES",gray_img) 
_, thresh = cv2.threshold(gray_img,127,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow("IMAGEN EN BINARIO", thresh)
cv2.imwrite("foto2.png",thresh)
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
img_contours = sorted(img_contours, key = cv2.contourArea)

for i in img_contours:
    if cv2.contourArea(i) > 100:
        break

mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [i], -1, 255, -1)
new_img = cv2.bitwise_and(img, img, mask=mask)

#cv2.imshow("resultado",new_img)
#cv2.imwrite("foto2.png",new_img)

img = cv2.imread( 'foto2.png', 1 )

img_r = Image.open('foto2.png').convert('RGB')

width, height = img_r.size

# Make into Numpy array
na = np.array(img_r)

# Get colours and corresponding counts
colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)
img = cv2.imread('foto2.png', cv2.IMREAD_GRAYSCALE)
##n_white_pix = np.sum(img == 255)
##print('Numero de pixeles blancos:', n_white_pix)

print( "Ancho: " + str(width) + "px" )
print( "Alto: " + str(height) + "px")

print("Colores: ")
print( colours )

print("Conteo en px: ")
print( counts[1] )

mm = counts[1]

print( "Medida en mm²: " )
print( mm )
