import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
    Funcoes auxiliares
"""

def plot(plot1, plot2):

    plt.subplot(121),plt.imshow(plot1, cmap = 'gray'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(plot2, cmap = 'gray'), plt.xticks([]), plt.yticks([])
    plt.show()

def magnitude(img):

    freq = np.fft.fft2(img)
    freq_shift = np.fft.fftshift(freq)
    magnitude_spectrum = 20*np.log(np.abs(freq_shift))
    plot(img, magnitude_spectrum)

    return freq_shift

def edge_improv2(img):
    pass

def main():

    clown = cv.imread('imagens/clown.tif', 0)
    man = cv.imread('imagens/mandrill.tif')

    clown_freq_shif = magnitude(clown)
    man_freq_shift_B = magnitude(man[:,:,0])
    man_freq_shift_G = magnitude(man[:,:,1])
    man_freq_shift_R = magnitude(man[:,:,2])


    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)

if __name__ == '__main__':
    main()