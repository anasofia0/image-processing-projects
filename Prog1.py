import cv2 as cv
import numpy as np

"""
    Funcoes auxiliares
"""


def show_img(img, nome=''):
    cv.imshow(nome, img)
    cv.waitKey(0)


def dist_euclid_centro(img):
    row, col = img.shape
    u, v = np.meshgrid([i for i in range(col)], [i for i in range(row)])
    return np.add(np.power(np.subtract(u, int(col/2)), 2), np.power(np.subtract(v, int(row/2)), 2))

"""
    Funcoes dec_int e edge_improvd
"""


def dec_int(img):

    show_img(img)

    img = np.delete(img, [i for i in range(0, img.shape[0], 2)], 0)
    img = np.delete(img, [i for i in range(0, img.shape[1], 2)], 1)

    show_img(img)

    img = np.repeat(img, 2, 0)
    img = np.repeat(img, 2, 1)

    show_img(img)

    return img


def edge_improv(img, sigma):




def main():

    img = 'imagens/test80.jpg'
    img = cv.imread(img)

    img_mod_1 = dec_int(img)
    img_mod_1 = edge_improv(img_mod_1, 10)
    show_img(img_mod_1)
    # cv.destroyAllWindows()

    x, y = (img.shape[0], img.shape[1])

    show_img(img, 'Original')
    # cv.destroyAllWindows()
    img_mod_2 = cv.resize(img, (y//2, x//2), cv.INTER_CUBIC)
    show_img(img_mod_2)
    img_mod_2 = cv.resize(img_mod_2, (y, x), cv.INTER_CUBIC)
    show_img(img_mod_2, 'Interpolada')
    img_mod_2 = edge_improv(img_mod_2, 3)
    show_img(img_mod_2, 'Filtro')


if __name__ == '__main__':
    main()
