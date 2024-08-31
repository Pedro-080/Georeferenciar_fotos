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


# # Função para cortar a imagem
# def crop_image(image, crop_box):
#     return image.crop(crop_box)


# image_name = "fotografia.jpeg"
# image_name = "corte.png"
# image_name = "fotografia.png"
image_name = "swiss.jpeg"


input_file = f'fotos/{image_name}'

# Carregar a imagem
image = Image.open(input_file)
# image.show(title="Imagem Original")

# Obter dimensões da imagem
width, height = image.size

# # Definir a caixa de corte para focar na metade inferior da imagem
# # A caixa de corte inclui a metade inferior da imagem
# crop_box = (0, height // 3, width, height)  # (left, upper, right, lower)
# cropped_image = crop_image(image, crop_box)
# # cropped_image.show(title="Imagem Cortada (Metade Inferior)")

# Converter para escala de cinza
gray_image = image.convert('L')
# gray_image.show(title="Imagem em Escala de Cinza")


# Aplicar binarização usando um threshold fixo
binary_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
# binary_image.show(title="Imagem Binarizada")

# Redimensionar a imagem usando Image.LANCZOS
resized_image = binary_image.resize((binary_image.width * 2, binary_image.height * 2), Image.LANCZOS)
# resized_image.show(title="Imagem Redimensionada")

# Aplicar filtro de desfoque para suavizar a imagem
filtered_image = resized_image.filter(ImageFilter.MedianFilter())
# filtered_image.show(title="Imagem Filtrada")

# image = cv2.imread(input_file)


pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"


text = pytesseract.image_to_string(filtered_image,lang="por")

print(text)

numbers = extract_numbers(text)

print("Valores numéricos extraídos:")
print(numbers)