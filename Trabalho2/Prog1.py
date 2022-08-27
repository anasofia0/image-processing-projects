import cv2 as cv
import numpy as np

def acha_buraco(img):

    _, img = cv.threshold(img, 128, 255, cv.THRESH_BINARY)

    

def main():

    img = cv.imread('imagens/pcb.jpg',0)

    cv.imshow('img', img)
    cv.waitKey(0)

    acha_buraco(img)


if __name__ == '__main__':
    main()
