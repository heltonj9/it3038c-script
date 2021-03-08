import io
#url = bit.ly/3v3NGc
from PIL import Image
import requests

print('Image URL?')
url = input()
print('File path?')
image_file_path = input()

PIL.Image.open(io.BytesIO(request.urlopen(url).read())).save(image_file_path)