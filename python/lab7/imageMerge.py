from PIL import Image

image1 = Image.open('C:/it3038c-script/python/lab7/pillow.jpg')
image1.show()
image2 = Image.open('C:/it3038c-script/python/lab7/pillow1.jpg')
image2.show()

image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1)
new_image.paste(image2, (image1_size[0],0))
new_image.save('C:/it3038c-script/python/lab7/pillowMerge.jpg','JPEG')
new_image.show();