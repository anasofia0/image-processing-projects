import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
    Funcoes auxiliares
"""

def eq_hist(img):

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eq_img = cv.equalizeHist(img)

    cv.imshow('img', img)
    cv.imshow('eq_img', eq_img)
    cv.waitKey(0)

    cv.destroyAllWindows()

    return img, eq_img


def trans_gamma(img, c, gamma):
    return np.cast['uint8'](c*np.power(img/255,gamma))

def main():

    """
        Correcao gamma
    """
    
    car = cv.imread('imagens/car.png')
    crowd = cv.imread('imagens/crowd.png')
    uni = cv.imread('imagens/university.png')

    cv.imshow('original', car)
    car_gamma1, car_gamma2 = (1.5, 3)
    cv.imshow(f'gamma: {car_gamma1:.1f}', trans_gamma(car, 255, car_gamma1))
    cv.imshow(f'gamma: {car_gamma2:.1f}', trans_gamma(car, 255, car_gamma2))
    cv.waitKey(0)

    cv.destroyAllWindows()


    cv.imshow('original', crowd)
    crowd_gamma1, crowd_gamma2 = (0.5, 0.3)
    cv.imshow(f'gamma: {crowd_gamma1:.1f}', trans_gamma(crowd, 255, crowd_gamma1))
    cv.imshow(f'gamma: {crowd_gamma2:.1f}', trans_gamma(crowd, 255, crowd_gamma2))
    cv.waitKey(0)

    cv.destroyAllWindows()

    cv.imshow('original', uni)
    uni_gamma1, uni_gamma2 = (0.3, 0.4)
    cv.imshow(f'gamma: {uni_gamma1:.1f}', trans_gamma(uni, 255, uni_gamma1))
    cv.imshow(f'gamma: {uni_gamma2:.1f}', trans_gamma(uni, 255, uni_gamma2))
    cv.waitKey(0)

    cv.destroyAllWindows()

    """
        Equalizacao de histograma
    """

    car, eq_car = eq_hist(car)

    hist_car = cv.calcHist([car],[0], None, [256], (0,256))
    hist_car_cdf = np.cumsum(hist_car) / np.sum(hist_car)
    hist_eq_car = cv.calcHist([eq_car],[0], None, [256], (0,256))
    hist_eq_car_cdf = np.cumsum(hist_eq_car) / np.sum(hist_car)

    plt.subplot(221), plt.bar([i for i in range(256)], [i[0] for i in hist_car])
    # plt.subplot(221), plt.plot(hist_car)
    plt.title("histograma não normalizado"), plt.yticks([]), plt.xlim([0,256])
    plt.subplot(222), plt.bar([i for i in range(256)], hist_car_cdf)
    plt.title("CDF não normalizado"), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.bar([i for i in range(256)], [i[0] for i in hist_eq_car])
    plt.title("histograma normalizado"), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.bar([i for i in range(256)], hist_eq_car_cdf)
    plt.title("CDF normalizado"), plt.xticks([]), plt.yticks([])
    plt.show()

    eq_hist(crowd)
    eq_hist(uni)

if __name__ == '__main__':
    main()