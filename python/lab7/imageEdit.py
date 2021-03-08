from PIL import Image

def tnails():
    try:
        image = Image.open('C:/it3038c-script/python/lab7/pillow1.jpg')
        image.thumbnail((90,90))
        image.save('C:/it3038c-script/python/lab7/pillowThumbnail.jpg')
        image1 = Image.open('C:/it3038c-script/python/lab7/pillowThumbnail.jpg')
        image1.show()
    except IOError:
        pass
tnails();