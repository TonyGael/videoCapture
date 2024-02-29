# importamos las librerias
import cv2

# Creamos la Video Captura
cap = cv2.VideoCapture(0)

# ciclo para ejecutar nuestros Frames
while True:
    # leemos fotogramas
    ret, frame = cap.read()

    print(ret)

    # proyectamos los frames
    cv2.imshow("VIDEO CAPTURA", frame)

    # paramos con lectura de teclado
    teclado = cv2.waitKey(1)
    if teclado == 27: # 27 = escape en ASCII
        break

# cerramos la video captura
cap.release()

# cerramos la ventana
cv2.destroyAllWindows()