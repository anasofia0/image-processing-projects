import cv2 as cv
import numpy as np

"""
    Funcoes auxiliares
"""

def show_img(img, nome=''):
    cv.imshow(nome, img)
    cv.waitKey(0)

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


def edge_improv(img):

    kernel = np.array([[1,1,1],
                        [1,1,1],
                        [1,1,1]])/9
    
    blurr = cv.filter2D(img,-1,kernel)

    kernel = np.array([[-1,-1,-1],
                        [-1,9,-1],
                        [-1,-1,-1]])
    
    edge_imp = cv.filter2D(blurr,-1,kernel)
    
    return edge_imp


def main():

    img = 'images/test80.jpg'
    img = cv.imread(img)

    img_mod_1 = dec_int(img)
    img_mod_1 = edge_improv(img_mod_1)
    show_img(img_mod_1)
    # cv.destroyAllWindows()

    x, y = (img.shape[0], img.shape[1])

    show_img(img, 'Original')
    # cv.destroyAllWindows()
    img_mod_2 = cv.resize(img, (y//2, x//2), cv.INTER_CUBIC)
    show_img(img_mod_2)
    img_mod_2 = cv.resize(img_mod_2, (y, x), cv.INTER_CUBIC)
    show_img(img_mod_2, 'Interpolada')
    img_mod_2 = edge_improv(img_mod_2)
    show_img(img_mod_2, 'Filtro')


if __name__ == '__main__':
    main()
