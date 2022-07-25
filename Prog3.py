import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
    Funcoes auxiliares
"""

def plot(plots, n=2, titulos = ['', '']):

    if(n == 2):
        plt.subplot(121), plt.imshow(plots[0], cmap = 'gray'), plt.title(titulos[0]), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(plots[1], cmap = 'gray'), plt.title(titulos[1]), plt.xticks([]), plt.yticks([])

    elif(n == 3):
        plt.subplot(131), plt.imshow(plots[0], cmap = 'gray'), plt.title(titulos[0]), plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(plots[1], cmap = 'gray'), plt.title(titulos[1]), plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(plots[2], cmap = 'gray'), plt.title(titulos[2]), plt.xticks([]), plt.yticks([])

    plt.show()

def furr(img):

    freq = np.fft.fft2(img)
    freq_shift = np.fft.fftshift(freq)
    magnitude = 20*np.log(np.abs(freq_shift))
    fase = np.angle(freq_shift)
    plot([img, magnitude, fase], n=3, titulos=['imagem', 'magnitude', 'fase'])

    return freq_shift

def troca_fase(img1, img2):

    freq1 = np.fft.fft2(img1)
    freq2 = np.fft.fft2(img2)
    
    mag1 = np.abs(freq1)
    mag2 = np.abs(freq2)

    vec_fase = np.vectorize(lambda i: np.cos(i)+1j*np.sin(i))

    troca1 = mag1*vec_fase(np.angle(freq2))
    troca2 = mag2*vec_fase(np.angle(freq1))

    img1 = np.fft.ifft2(troca1)
    img1 = np.real(img1)

    img2 = np.fft.ifft2(troca2)
    img2 = np.real(img2)

    plot([img1, img2])

def edge_improv2(img):
    blur = cv.GaussianBlur(img, (3, 3), 0)
    img_mod = cv.addWeighted(img, 2, blur, -1, 0)
    return img_mod

def main():

    clown = cv.imread('imagens/clown.tif', 0)
    man = cv.imread('imagens/mandrill.tif', 0)

    furr(clown)
    furr(man)

    troca_fase(clown, man)

    test = cv.imread('imagens/test80.jpg')
    test = np.delete(test, [i for i in range(0, test.shape[0], 2)], 0)
    test = np.delete(test, [i for i in range(0, test.shape[1], 2)], 1)
    test = np.repeat(test, 2, 0)
    test = np.repeat(test, 2, 1)
    cv.imshow('', test)
    cv.waitKey(0)
    cv.imshow('', edge_improv2(cv.GaussianBlur(test, (3, 3), 0)))
    cv.waitKey(0)

if __name__ == '__main__':
    main()