import io
from PIL import Image
import requests

#Image.save(fp, format=None, **params)
print ('Image URL?')
url = input();
print ('File path?')
image_file_path = input();


def download_image(url, image_file_path):
    r = requests.get(url, timeout=4.0)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)

    with Image.open(io.BytesIO(r.content)) as im:
        im.save(image_file_path)

    print('Image downloaded from url: {} and saved to: {}.'.format(url, image_file_path))