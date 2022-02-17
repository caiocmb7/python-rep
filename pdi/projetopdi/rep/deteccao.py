import numpy as np
import cv2.cv2 as cv2


def error_detection(imagem, iterations):
    im = imagem.copy()
    mediaprev = 0
    it = 0
    for it in range(iterations):
        if it != 0:
            mediaprev = np.mean(im)
        kernel = np.ones((it*2+3))
        cv2.erode(im, kernel, im)

    for i in range(len(im)):
        for j in range(len(im[0])):
            if im[i][j] >= mediaprev:
                im[i][j] = 255
            else:
                im[i][j] = 0

    kernel = np.ones((it*2+5, it*2+5), dtype="uint8")
    im = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)

    return im


def edging(src, areas):
    edged = cv2.Canny(areas, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area <= 9000:  # colocar os valores min e max de area
            cv2.drawContours(src, contour, -1, (0, 0, 255), 3)
    return src


# carregando a imagem
img1 = cv2.imread("assets/images/erro_jeans2.jpg")
cv2.imshow('original', img1)  # mostrando a imagem original

# processamento
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
res = error_detection(img, 4)
final = edging(img1, res)

# mostrando os erros detectados
cv2.imshow('detectada', final)
cv2.waitKey()
