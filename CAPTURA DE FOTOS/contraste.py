import cv2
import numpy as np
from PIL import Image

alpha = 0.3
beta = 80
#imgGray = cv2.imread('foto.png',0)
img_path = "foto.png"
img2 = cv2.imread(img_path,0)
#img_path = (imgGray)
img = cv2.imread(img_path,0)
#img2 = cv2.imread(img_path)

def updateAlpha(x):
    global alpha, img, img2
    alpha = cv2.getTrackbarPos('Alpha', 'image')
    alpha = alpha * 0.01
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))
def updateBeta(x):
    global beta, img, img2
    beta = cv2.getTrackbarPos('Beta', 'image')
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))
# Crear ventana
cv2.namedWindow('image')
cv2.createTrackbar('Alpha', 'image', 0, 300, updateAlpha)
cv2.createTrackbar('Beta', 'image', 0, 255, updateBeta)
cv2.setTrackbarPos('Alpha', 'image', 100)
cv2.setTrackbarPos('Beta', 'image', 10)
while (True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow('imagen gris',img2)
cv2.destroyAllWindows()
