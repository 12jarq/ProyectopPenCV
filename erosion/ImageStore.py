import cv2


class ImageStore:
    @staticmethod
    def img_read(path_img):
        if isinstance(path_img,str):
            try:
                img = cv2.imread(path_img)
            except:
                print("Error de path")
            return img
        else:
            print("Formato no valido")
            return None



    @staticmethod
    def save_img(img, name_img):
        name_img = name_img + ".png"
        cv2.imwrite(name_img, img)