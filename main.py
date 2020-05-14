
from erosion.ImageStore import ImageStore
from erosion.Erosion import Erosion


if __name__ == '__main__':
    img = ImageStore.img_read("images/j.png")
    erosion = Erosion.ero_img(img)
    ImageStore.save_img(img=erosion, name_img="Erosion")
    print('El proyecto corrrio exitosamente')
