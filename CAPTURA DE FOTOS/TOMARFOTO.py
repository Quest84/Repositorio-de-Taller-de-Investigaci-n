import cv2

cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("foto.png", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

"""
	Finalmente liberamos o soltamos la cámara
"""
cap.release()

img1 = cv2.imread('foto.png')

cv2.imshow("IMAGEN ORIGINAL", img1)
#CONVERSION DE RGB A GRISES
bordecanny= cv2.Canny(img1,100,200)
bordeCannynot= cv2. bitwise_not(bordecanny)
cv2.imshow("IMAGEN inversa", bordeCannynot)
#_,umbral =cv2.threshold(bordeCannynot,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imshow("CONVERSION A BINARIO",umbral)
#FILTRO
canny = cv2.Canny(img1, 50, 150)
cv2.imshow("CANNY",canny)

#contornos
# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", img1)

cv2.waitKey(0)
