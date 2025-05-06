import cv2

# Cargar imagen
imagen = cv2.imread('Navaja.jpg')
imagen = cv2.resize(imagen, (800, 600))

# Verificar si se cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

#Escritura sobre la imagen(mera demostracion)
cv2.putText(
    imagen,
    'REGION DE INTERES',
    (50, 50),  # Posición (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,
    2,              # Tamaño del texto
    (150, 255, 0),    # Color: verde (BGR)
    2               # Grosor
)

#Esto es para el ROI y El rectangulo de interes
# Coordenadas: (x, y, ancho, alto)
x, y, w, h = 100, 100, 200, 150
cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 150, 0), 2)

# Extraer la ROI
roi = imagen[y:y+h, x:x+w]

# ----------- 🖼 Mostrar resultados -------------------------
cv2.imshow('Original', imagen)
cv2.imshow('ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()