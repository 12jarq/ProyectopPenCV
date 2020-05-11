import cv2
import numpy as np
from erosion.ImageStore import ImageStore


def kern_on():
    kernel = np.ones((6, 6), np.uint8)
    return kernel


def ero_img(img):
    erosion_img = cv2.erode(img, kern_on(), iterations=1)
    return erosion_img


if __name__ == '__main__':
    img = ImageStore.img_read("images/j.png")
    erosion = ero_img(img)
    ImageStore.save_img(img=erosion, name_img="Erosion")
    print('El proyecto corrrio exitosamente')
