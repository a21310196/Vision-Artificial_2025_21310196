import cv2
import numpy as np

img_rgb = cv2.imread('Bomberman.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('bombabomberman.jpg ', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (250  , 150, 255), 2)

cv2.imshow('MatchBOMBA', img_rgb)
cv2.imshow('bombabomberman',template)

cv2.waitKey(0)  # Espera hasta que presiones una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV
