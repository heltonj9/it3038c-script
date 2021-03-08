To install Pillow, you must first make sure you have Pip installed. To install both these programs, use the commands:
  python -m pip install pip
  python -m pip install pillow

The three things I decided to do with pillow was first displaying an image, second editing the size of an image to the size of a thumbnail, and third merging two images together
into one combined image.

For each of these tasks, you must start the script off with the command 
"from PIL import Image". 
This command works the same as importing any other program you will be using.
Also, for each of these tasks, you must have the exact filepath for each of the images, and for the merge file, you must come up with a filepath you want to save the merged image into.

To display an image out of its file, you use the following script:
  from PIL import Image
  im = Image.open("C:/it3038c-script/python/lab7/pillow.jpg")   #Instead of "C:/it3038c-script/python/lab7/pillow.jpg", you would put your own image's filepath.
  im.show()

To edit the size of an image, you would use the following script:
  from PIL import Image
  
  def tnails():
    try:
      image = Image.open('C:/it3038c-script/python/lab7/pillow1.jpg')
      image.thumbnail((W,H))  #w = width, h = height. Instead of using those letters, you would input a number for each of them. 
      image.save('C:/it3038c-script/python/lab7/pillowThumbnail.jpg')
      image1 = Image.open('C:/it3038c-script/python/lab7/pillowThumbnail.jpg')
      image1.show()
    except IOError:
      pass
  tnails();

To merge two images to form one image side-by-side, you would use the following script:
  from PIL import Image
  
  image1 = Image.open('C:/it3038c-script/python/lab7/pillow.jpg')
  image1.show()
  image2 = Image.open('C:/it3038c-script/python/lab7/pillow1.jpg')
  image2.show()
  
  image1 = image1.resize((W, H))  #Once again, instead of W and H, input Width and Height desired
  image1_size = image1.size
  image2_size = image2.size
  new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
  new_iamge.paste(image1)
  new_image.paste(image2, (image1_size[0],0))
  new_image.save('C:/it3038c-script/python/lab7/pillowMerge.jpg', 'JPEG')
  new_image.show();
  
  
  The source for all my information about pillow is from the following website:
  https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm
