#!/usr/bin/env python3

import numpy as np
import cv2 as cv
import sys

COLOR_RED = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)

def preprocessing(img):
    # conversao da imagem para escala de cinza
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # aplicacao de filtro gaussiano
    imgblur = cv.GaussianBlur(img_gray, (3,3), 0)
    # aplicacao de filtro laplaciano
    imglap = cv.Laplacian(imgblur, cv.CV_16S, ksize=3)
    # conversao para uint8
    imgabs = cv.convertScaleAbs(imglap)
    # equalizacao de histograma
    imgeq = cv.equalizeHist(imgabs)
    # filtro de media
    imgblur = cv.blur(imgeq, (5,5))
    # limiarizacao binaria
    ret,thresh1 = cv.threshold(imgblur,120,255,cv.THRESH_BINARY_INV)
    # opening
    kernel = np.ones((13,13),np.uint8)
    opening = cv.morphologyEx(thresh1, cv.MORPH_OPEN, kernel)
    # dilatacao
    kernel_dl = np.ones((3,3),np.uint8)
    dilation = cv.dilate(opening,kernel_dl,iterations = 1)
    
    return dilation

def detect(file):
    output = cv.imread(file)
    jeans = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
    jeans = cv.blur(jeans, (30,30))
    _, jeans = cv.threshold(jeans, 20, 255, cv.THRESH_BINARY)
    edges = cv.Canny(jeans, 50, 100)
    contours, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for idx, contour in enumerate(contours):
        length = cv.arcLength(contour, closed=True)
        if length < 150: continue

        x,y,w,h = cv.boundingRect(contour)
        ellipse = cv.fitEllipse(contour)
        cv.putText(
            output, f'{int(length)}',
            (x+(w//2),y+(h//2)), cv.FONT_HERSHEY_SIMPLEX, 1.5, COLOR_GREEN, 5
        )
        cv.ellipse(output, ellipse, COLOR_RED, 2)

    cv.imwrite(f'{file.split()[0]}_out.png', output)

def main():
    [detect(f) for f in sys.argv[1:]]

if __name__ == '__main__':
    main()
