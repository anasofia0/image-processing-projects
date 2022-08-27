import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def main():

    img = cv.imread('imagens/morf_test.png',cv.IMREAD_GRAYSCALE)

    cv.imshow('img', img)
    cv.waitKey(0)
    
    # aplicando fechamento, para obter o fundo

    fundo = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE,(9,9)))

    cv.imshow('img', fundo)
    cv.waitKey(0)

    # subtraindo da imagem original e invertendo o resultado 

    img = fundo - img
    img = 255 - img

    # aplicando black hat

    img = cv.morphologyEx(img, cv.MORPH_BLACKHAT, cv.getStructuringElement(cv.MORPH_ELLIPSE,(9,9)))

    cv.imshow('img', img)
    cv.waitKey(0)

    # binarizando a imagem

    _,img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imshow('img', img)
    cv.waitKey(0)

    # aplicando ditalacao, abertura e erosao

    img = cv.dilate(img,cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)),iterations = 1)

    img = cv.morphologyEx(img, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)))

    cv.imshow('img', 255 - img)
    cv.waitKey(0)

    img = cv.erode(img,cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)),iterations = 1)

    # invertendo imagem

    img = 255 - img

    cv.imshow('img', img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
