import cv2 as cv
import numpy as np

def main():

    img = cv.imread('imagens/img_cells.jpg')
    img_orig = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # binarizando

    _,img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    cv.imshow('img', img)
    cv.waitKey(0)

    # preenchendo espaços desconexos

    img = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)),  iterations=2)

    cv.imshow('img', img)
    cv.waitKey(0)

    img = 255-img
    img_aux = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(img_aux, mask, (0,0), 255)
    img_aux = cv.bitwise_not(img_aux)
    img = img | img_aux

    cv.imshow('img', img)
    cv.waitKey(0)

    # regiao onde ha fundo

    fundo = cv.dilate(img, cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)), iterations=3)

    # regiao onde ha celula

    dist_transform = cv.distanceTransform(img, cv.DIST_L2, 3)
    _, celula = cv.threshold(dist_transform, 0.35*dist_transform.max(), 255, 0)

    celula = cv.morphologyEx(celula, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)))

    cv.imshow('img', celula)
    cv.waitKey(0)

    #regiao incerta

    celula = np.uint8(celula)
    incerta = cv.subtract(fundo, celula)

    # cv.imshow('img', fundo)
    # cv.waitKey(0)
    # cv.imshow('img', celula)
    # cv.waitKey(0)
    # cv.imshow('img', inceint32rta)
    # cv.waitKey(0)

    # classificando as regioes
    # _, 8, cv.CV_32SC1
    _, markers = cv.connectedComponents(celula)
    markers += 1
    markers[incerta==255] = 0
    print(markers.shape)
    print(img_aux.shape)

    markers = cv.watershed(img_orig, markers)
    img_orig[markers == -1] = [255,0,0]

    img_orig = img_orig.astype(np.uint8)

    cv.imshow('img', incerta)
    cv.waitKey(0)
    cv.imshow('img', img_orig)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
    # markers = markers.astype(np.uint8)

    # cv.applyColorMap(markers, cv.COLORMAP_JET)
    # cv.imshow('img', markers)
    # cv.waitKey(0)
