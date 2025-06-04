import cv2
import numpy as np

# 1. Cargar imagen en escala de grises
img = cv2.imread('Caballo.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("No se encontró la imagen.")
    exit()

# 2. Filtro lineal: suavizado
blur = cv2.blur(img, (5, 5))  # Media simple
gaussian = cv2.GaussianBlur(img, (5, 5), 0)  # Filtro Gaussiano

# 3. Filtro morfológico: apertura y cierre
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apertura (elimina ruido F+ — puntos blancos)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Cierre (elimina ruido F- — puntos negros)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 4. Morfología avanzada: TopHat y BlackHat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)     # resalta detalles más claros
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel) # resalta detalles más oscuros

# 5. Mostrar resultados
cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Opening (remueve F+)", opening)
cv2.imshow("Closing (remueve F-)", closing)
cv2.imshow("TopHat (blanco sobre fondo)", tophat)
cv2.imshow("BlackHat (negro sobre fondo)", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
