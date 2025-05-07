import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('bookpage.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=0.5, fy=0.5)
if img is None:
    print("Error: No se pudo cargar la imagen")
    exit()

# Umbral fijo para métodos básicos
umbral = 127
max_valor = 255

# 1. Binary
_, th_binary = cv2.threshold(img, umbral, max_valor, cv2.THRESH_BINARY)

# 2. Binary Invertido
_, th_binary_inv = cv2.threshold(img, umbral, max_valor, cv2.THRESH_BINARY_INV)

# 3. Truncado
_, th_trunc = cv2.threshold(img, umbral, max_valor, cv2.THRESH_TRUNC)

# 4. To Zero
_, th_tozero = cv2.threshold(img, umbral, max_valor, cv2.THRESH_TOZERO)

# 5. To Zero Invertido
_, th_tozero_inv = cv2.threshold(img, umbral, max_valor, cv2.THRESH_TOZERO_INV)

# 6. Umbral adaptativo - Media
th_mean = cv2.adaptiveThreshold(img, max_valor, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)

# 7. Umbral adaptativo - Gaussiano
th_gauss = cv2.adaptiveThreshold(img, max_valor, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# 8. Otsu (automático)
_, th_otsu = cv2.threshold(img, 0, max_valor, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ---------- Mostrar en una sola ventana con matplotlib ----------
titulos = [
    'Original', 'Binary', 'Binary Inv', 'Trunc',
    'To Zero', 'To Zero Inv', 'Adapt Mean', 'Adapt Gauss', 'Otsu'
]
imagenes = [
    img, th_binary, th_binary_inv, th_trunc,
    th_tozero, th_tozero_inv, th_mean, th_gauss, th_otsu
]
plt.figure(figsize=(12,8))

for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i], fontsize=10)
    plt.axis('off')

plt.tight_layout(pad=2.0)  # Ajusta los márgenes entre subplots
plt.show()