import cv2
import numpy as np

# 1. Cargar imagen
img = cv2.imread('cubista.jpg')
if img is None:
    print("No se encontró la imagen.")
    exit()

# 2. Seleccionar ROI manualmente
roi = cv2.selectROI("Imagen a segmentar ",img,fromCenter=False, showCrosshair=True)
x, y, w, h = roi

# 3. Crear una imagen negra del mismo tamaño que la original
roi_only = np.zeros_like(img)

# 4. Copiar solo el ROI seleccionado
roi_only[y:y+h, x:x+w] = img[y:y+h, x:x+w]

# 5. Convertir a escala de grises para detectar esquinas
gray = cv2.cvtColor(roi_only, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 6. Detectar esquinas dentro del ROI (Shi-Tomasi)
corners = cv2.goodFeaturesToTrack(gray, maxCorners= 30,qualityLevel=0.1,minDistance=1)

if corners is not None:
    corners = corners.astype(int) 
    for i in corners:
        x_corner, y_corner = i.ravel()
        cv2.circle(roi_only, (x_corner, y_corner), 3, (0, 255, 0), -1)

# 7. Mostrar el resultado
cv2.destroyAllWindows()
cv2.imshow("Solo ROI con esquinas detectadas", roi_only)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Guardar si se desea
cv2.imwrite("roi_con_esquinas.jpg", roi_only)
