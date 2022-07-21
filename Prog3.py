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

def troca_fase(fur1, fur2):

    real1 = np.real(fur1)
    real2 = np.real(fur2)

    fase1 = np.angle(fur1)
    fase2 = np.angle(fur2)

    fur1 = np.vectorize(complex)(real1, fase2)
    fur2 = np.vectorize(complex)(real2, fase1)

    f_ishift = np.fft.ifftshift(fur1)
    img1 = np.fft.ifft2(f_ishift)
    img1 = np.real(img1)

    f_ishift = np.fft.ifftshift(fur2)
    img2 = np.fft.ifft2(f_ishift)
    img2 = np.real(img2)

    plot([img1, img2])

def edge_improv2(img):
    passa_alta = img - cv.GaussianBlur(img, (0, 0), sigma) + 127
    return img + passa_alta

def main():

    clown = cv.imread('imagens/clown.tif', 0)
    man = cv.imread('imagens/mandrill.tif', 0)

    print(clown.shape)

    f_clown = furr(clown)
    f_man = furr(man)

    troca_fase(f_clown, f_man)


if __name__ == '__main__':
    main()