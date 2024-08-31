from PIL import Image, ImageFilter, ImageOps
import os
import pytesseract
import re
from pyproj import Proj, transform
from GPSPhoto import gpsphoto

def tratar_img(input_file):
    # Carregar a imagem
    image = Image.open(input_file)

    # Converter para escala de cinza
    gray_image = image.convert('L')

    # Aplicar binarização usando um threshold fixo
    binary_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')

    # Redimensionar a imagem usando Image.LANCZOS
    resized_image = binary_image.resize((binary_image.width * 2, binary_image.height * 2), Image.LANCZOS)

    # Aplicar filtro de desfoque para suavizar a imagem
    filtered_image = resized_image.filter(ImageFilter.MedianFilter())

    text = pytesseract.image_to_string(filtered_image,lang="por")

    return text
    ...
