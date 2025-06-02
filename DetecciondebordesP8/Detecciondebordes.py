import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('IVECO.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (350, 200))  # Cambia a las dimensiones que desees (ancho, alto)


# Verificar que se cargó correctamente
if img is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Aplicar detección de bordes

# 1. Laplaciano (detecta cambios rápidos en todas direcciones)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# 2. Sobel X (detecta bordes verticales)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

# 3. Sobel Y (detecta bordes horizontales)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

# 4. Canny (algoritmo multietapa, muy preciso)
canny = cv2.Canny(img, 150, 250)  # puedes ajustar los umbrales

# Mostrar resultados
titulos = ['Imagen Original', 'Laplaciano', 'Sobel X', 'Sobel Y', 'Canny']
imagenes = [img, laplacian, sobelx, sobely, canny]

plt.figure(figsize=(14, 10))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
