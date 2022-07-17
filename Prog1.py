import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
    Funcoes auxiliares
"""

def dist_euclid_centro(img):
    row, col = img.shape
    u, v = np.meshgrid([i for i in range(col)], [i for i in range(row)])
    print(u.shape)
    return np.add(np.power(np.subtract(u, int(col/2)), 2), np.power(np.subtract(v, int(row/2)), 2))

def filtro_butterworth(img, raio, N):

    dist = dist_euclid_centro(img)
    h = np.divide(
                    1,
                    np.add(
                        1,
                        np.power(
                                    np.divide(
                                            dist,
                                            raio
                                            ),
                                    2*N
                                )
                        )
                )

    return img*h

"""
    Funcoes dec_int e edge_improve
"""

def dec_int(img, nome):

    cv.imshow(nome, img)
    cv.waitKey(0)

    img = np.delete(img, [i for i in range(0,img.shape[0], 2)], 0)
    img = np.delete(img, [i for i in range(0,img.shape[1], 2)], 1)

    cv.imshow(nome, img)
    cv.waitKey(0)

    img = np.repeat(img, 2, 0)
    img = np.repeat(img, 2, 1)

    cv.imshow(nome, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return img

def edge_improve(img, nome):

    img_mod = img.copy()

    B = img[:,:,0]
    G = img[:,:,1]
    R = img[:,:,2]

    B_freq = np.fft.fft2(B)
    G_freq = np.fft.fft2(G)
    R_freq = np.fft.fft2(R)

    B_freq_shift = np.fft.fftshift(B_freq)
    G_freq_shift = np.fft.fftshift(G_freq)
    R_freq_shift = np.fft.fftshift(R_freq)

    # dom_freq = 1000*np.log(np.abs(freq_shift))

    B_img_filtro = filtro_butterworth(B_freq_shift, 30000, 2)
    G_img_filtro = filtro_butterworth(G_freq_shift, 30000, 2)
    R_img_filtro = filtro_butterworth(R_freq_shift, 30000, 2)

    B_inv_freq = np.fft.ifftshift(B_img_filtro)
    G_inv_freq = np.fft.ifftshift(G_img_filtro)
    R_inv_freq = np.fft.ifftshift(R_img_filtro)

    B_img_mod = np.fft.ifft2(B_inv_freq)
    G_img_mod = np.fft.ifft2(G_inv_freq)
    R_img_mod = np.fft.ifft2(R_inv_freq)

    img_mod[:,:,0] = np.real(B_img_mod)
    img_mod[:,:,1] = np.real(G_img_mod)
    img_mod[:,:,2] = np.real(R_img_mod)

    cv.imshow('a', img_mod)
    cv.waitKey(0)


    # plt.subplot(121),plt.imshow(img)
    # plt.title(nome), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(img_mod)
    # plt.title(nome + ' dominio da frequencia'), plt.xticks([]), plt.yticks([])
    # plt.show()


def main():

    # img = input('image path: ')
    img = 'imagens/test80.jpg'
    nome = img.split('/')[-1]
    img = cv.imread(img)
    print(img.shape)
    img_mod = dec_int(img, nome)
    edge_improve(img_mod, nome)


if __name__ == '__main__':
    main()