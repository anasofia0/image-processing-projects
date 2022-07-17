import cv2 as cv
import numpy as np

"""
    Funcoes auxiliares
"""

def show_img(img, nome = ''):
    cv.imshow(nome, img)
    cv.waitKey(0)

def dist_euclid_centro(img):
    row, col = img.shape
    u, v = np.meshgrid([i for i in range(col)], [i for i in range(row)])
    return np.add(np.power(np.subtract(u, int(col/2)), 2), np.power(np.subtract(v, int(row/2)), 2))

def filtro_butterworth(img, raio, N):

    dist = dist_euclid_centro(img)
    h = np.divide(1, np.add(1, np.power(np.divide(dist, raio), 2*N)))
    return img*h

def filtro_gaussano(img, raio):
    dist = dist_euclid_centro(img)
    h = np.exp((-1)*np.divide(np.power(dist, 2), 2*raio**2))

    return img*h

"""
    Funcoes dec_int e edge_improvd
"""

def dec_int(img):

    show_img(img)

    img = np.delete(img, [i for i in range(0,img.shape[0], 2)], 0)
    img = np.delete(img, [i for i in range(0,img.shape[1], 2)], 1)

    show_img(img)

    img = np.repeat(img, 2, 0)
    img = np.repeat(img, 2, 1)

    show_img(img)

    return img

def edge_improv(img):

    return cv.GaussianBlur(img, (3,3), 0)

    # img_mod = img.copy()

    # B = img[:,:,0]
    # G = img[:,:,1]
    # R = img[:,:,2]

    # B_freq = np.fft.fft2(B)
    # G_freq = np.fft.fft2(G)
    # R_freq = np.fft.fft2(R)

    # B_freq_shift = np.fft.fftshift(B_freq)
    # G_freq_shift = np.fft.fftshift(G_freq)
    # R_freq_shift = np.fft.fftshift(R_freq)
    
    # B_img_filtro = filtro_butterworth(B_freq_shift, 10000, 2)
    # G_img_filtro = filtro_butterworth(G_freq_shift, 10000, 2)
    # R_img_filtro = filtro_butterworth(R_freq_shift, 10000, 2)

    # B_inv_freq = np.fft.ifftshift(B_img_filtro)
    # G_inv_freq = np.fft.ifftshift(G_img_filtro)
    # R_inv_freq = np.fft.ifftshift(R_img_filtro)

    # B_img_mod = np.fft.ifft2(B_inv_freq)
    # G_img_mod = np.fft.ifft2(G_inv_freq)
    # R_img_mod = np.fft.ifft2(R_inv_freq)

    # img_mod[:,:,0] = np.real(B_img_mod)
    # img_mod[:,:,1] = np.real(G_img_mod)
    # img_mod[:,:,2] = np.real(R_img_mod)

    # return img_mod


def main():

    img = 'imagens/test80.jpg'
    img = cv.imread(img)

    img_mod_1 = dec_int(img)
    img_mod_1 = edge_improv(img_mod_1)
    show_img(img_mod_1)
    cv.destroyAllWindows()

    x, y = (img.shape[0], img.shape[1])

    show_img(img, 'Original')
    cv.destroyAllWindows()
    img_mod_2 = cv.resize(img, (y//2, x//2), cv.INTER_CUBIC)
    show_img(img_mod_2)
    img_mod_2 = cv.resize(img_mod_2, (y, x), cv.INTER_CUBIC)
    show_img(img_mod_2, 'Interpolada')
    img_mod_2 = edge_improv(img_mod_2)
    show_img(img_mod_2, 'Filtro')


if __name__ == '__main__':
    main()