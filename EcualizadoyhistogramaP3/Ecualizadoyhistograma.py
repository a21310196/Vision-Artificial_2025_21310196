import cv2
import matplotlib.pyplot as plt

# Aqui agregamos las imagenes a mostrar en el ecualizado
imagenes = [
    'Corta.jpg',
    'Engrapa.jpg',
    'Navaja.jpg',
    'Prit.jpg'
]

# Crear figura
plt.figure(figsize=(16, 12)) 

# Procesar cada imagen
for i, archivo in enumerate(imagenes):
    # Leer imagen en escala de grises
    img = cv2.imread(archivo, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: no se pudo cargar {archivo}")
        continue

    # Ecualizar histograma
    img_eq = cv2.equalizeHist(img)

    # Calcular histogramas
    hist_orig = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])

    fila = i * 4  # Posición base por imagen (4 columnas por fila)

    # Subplot 1: Imagen original
    plt.subplot(4, 4, fila + 1)
    plt.imshow(img, cmap='gray')
    plt.title(f'Original {i+1}')
    plt.axis('off')

    # Subplot 2: Histograma original
    plt.subplot(4, 4, fila + 2)
    plt.plot(hist_orig, color='black')
    plt.title('Histograma Original')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')

    # Subplot 3: Imagen ecualizada
    plt.subplot(4, 4, fila + 3)
    plt.imshow(img_eq, cmap='gray')
    plt.title('Ecualizada')
    plt.axis('off')

    # Subplot 4: Histograma ecualizado
    plt.subplot(4, 4, fila + 4)
    plt.plot(hist_eq, color='black')
    plt.title('Histograma Ecualizado')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
