import cv2

def mostrar_imagen(ruta_imagen, nuevo_ancho, nuevo_alto, modo_gris):
    # Cargar la imagen en color o en escala de grises según la opción seleccionada
    if modo_gris:
        imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)  # Carga en escala de grises
    else:
        imagen = cv2.imread(ruta_imagen, cv2.IMREAD_COLOR)  # Carga en color

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    # Redimensionar la imagen manteniendo proporciones
    imagen_redimensionada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))

    # Mostrar la imagen en una ventana
    titulo = "Motorivecogris" if modo_gris else "Imagen en Color"
    cv2.imshow(titulo, imagen_redimensionada)

    # Esperar a que se presione una tecla para cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ruta de la imagen
ruta = r"C:\Users\USUARIO\Documents\GitHub\Vision artifical 2025\6G_21310196_p1\Motoriveco.jpg"

# Definir el nuevo tamaño (ancho x alto en píxeles)
ancho = 500
alto = 300

# Cambia a True para escala de grises o False para color
modo_gris = True  # Cambia a False para ver en color

# Llamar a la función con la opción de escala de grises o color
mostrar_imagen(ruta, ancho, alto, modo_gris)
