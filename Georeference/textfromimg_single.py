from PIL import Image, ImageFilter, ImageOps
# import cv2
import pytesseract
import re

def extract_numbers(text):
    # Regex para encontrar números inteiros
    pattern = r'-?\b\d+\b'
    numbers = re.findall(pattern, text)
    
    # Converter para inteiros
    return [int(num) for num in numbers]

def tratar_img(input_file):
    # Carregar a imagem
    image = Image.open(input_file)

    width, height = image.size
    crop_box = (0, int(height * 0.8), width, height)  # (left, upper, right, lower)
    cropped_image = crop_image(image, crop_box)


    # Converter para escala de cinza
    gray_image = cropped_image.convert('L')

    # Aplicar binarização usando um threshold fixo
    binary_image = gray_image.point(lambda x: 0 if x < 235 else 255, '1')

    # Redimensionar a imagem usando Image.LANCZOS
    resized_image = binary_image.resize((binary_image.width * 2, binary_image.height * 2), Image.LANCZOS)

    # Aplicar filtro de desfoque para suavizar a imagem
    filtered_image = resized_image.filter(ImageFilter.MedianFilter())
    
    # cropped_image.show()
    # gray_image.show()
    # binary_image.show()
    # resized_image.show()
    filtered_image.show()

    text = pytesseract.image_to_string(filtered_image,lang="eng")

    return text
    ...


# Função para cortar a imagem
def crop_image(image, crop_box):
    return image.crop(crop_box)


# image_name = "P001.jpeg"
# image_name = "P002.jpeg"
# image_name = "P003.jpeg"
image_name = "Energisa 9268"


input_file = f'fotos/{image_name}'

pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = tratar_img(input_file)

# text = pytesseract.image_to_string(gray_image,lang="por")

print(text)

# numbers = extract_numbers(text)

# print("Valores numéricos extraídos:")
# print(numbers)