import cv2

import numpy as np


class Erosion():
    @staticmethod
    def kern_on():
        kernel = np.ones((6, 6), np.uint8)
        return kernel
    @staticmethod
    def ero_img(img):
        erosion_img = cv2.erode(img,Erosion.kern_on(), iterations=1)
        return erosion_img
