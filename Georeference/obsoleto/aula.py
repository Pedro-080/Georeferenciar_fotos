from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('fotos/test.jpg')
# img = Image.open('fotos/1.jpeg')

exif_data = img._getexif()
# print(exif_data)

# for key, value in exif_data.items():
#     print(key,value)

if exif_data is not None:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag,tag)
        print(f"{tag_name}: {value}")