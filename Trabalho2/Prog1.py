from cmath import pi
import cv2 as cv
import numpy as np
import scipy.ndimage as scp
import math

def main():

    img = cv.imread('Trabalho2/imagens/pcb.jpg', 0)

    cv.imshow('img', img)
    cv.waitKey(0)

    _, img = cv.threshold(img, 128, 255, cv.THRESH_BINARY)

    # fazendo fechamento para separar os buracos

    bola = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE,(31,31)))

    # aplicando fill e subraindo para obter as bolas

    bola_aux = scp.binary_fill_holes(bola)
    bola_aux = bola_aux * 255
    bola_aux = np.asarray(bola_aux, dtype='uint8')

    bola = bola_aux - bola

    cv.imshow('img', bola)
    cv.waitKey(0)

    # contando quantas bolas tem

    contornos, _ = cv.findContours(bola, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    diam = [math.sqrt(cv.contourArea(i)/math.pi)*2 for i in contornos]

    print(f'Quandidade de circulos: {len(contornos)}')
    print(f'Diametros de cada circulo: {" ".join(map(str, diam))}')

if __name__ == '__main__':
    main()
