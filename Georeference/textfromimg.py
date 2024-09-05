from PIL import Image, ImageFilter, ImageOps
import os
import pytesseract
import re
from pyproj import Proj, transform
from GPSPhoto import gpsphoto

# Função para cortar a imagem
def crop_image(image, crop_box):
    return image.crop(crop_box)

def extract_numbers(text):
    # Regex para encontrar números inteiros e negativos
    pattern = r'-?\b\d+\b'
    numbers = re.findall(pattern, text)
    
    # Converter para inteiros
    return [int(num) for num in numbers]

def tratar_img(input_file):
    # Carregar a imagem
    image = Image.open(input_file)

    width, height = image.size
    crop_box = (0, int(height * 0.7), width, height)  # (left, upper, right, lower)
    cropped_image = crop_image(image, crop_box)


    # Converter para escala de cinza
    gray_image = cropped_image.convert('L')

    # Redimensionar a imagem usando Image.LANCZOS
    resized_image = gray_image.resize((gray_image.width * 3, gray_image.height * 3), Image.LANCZOS)


    # Aplicar binarização usando um threshold fixo
    binary_image = resized_image.point(lambda x: 0 if x < 240 else 255, '1')

    
    # Aplicar filtro de desfoque para suavizar a imagem
    filtered_image = binary_image.filter(ImageFilter.MedianFilter())
    # filtered_image.show()





    # config = r'--psm 6'

    # text = pytesseract.image_to_string(filtered_image,lang="eng",config=config)
    text = pytesseract.image_to_string(filtered_image,lang="eng")


    test_file = "fotos/W039.jpeg"

    if input_file == test_file:
        filtered_image.show()
        # gaussian_image.show()
        print(text)



    return text
    ...

def utm_to_geographic(easting, northing, zone, hemisphere):
    # Crie um objeto de projeção para o sistema de coordenadas UTM
    utm_proj = Proj(proj='utm', zone=zone, ellps='WGS84', hemisphere=hemisphere, south=True)

    # Crie um objeto de projeção para o sistema de coordenadas geográficas
    geodetic_proj = Proj(proj='latlong', datum='WGS84')

    # Converta as coordenadas UTM para geográficas
    longitude, latitude = transform(utm_proj, geodetic_proj, easting, northing)
    
    print(f"( lat: {easting} , {northing} )")
    print(f"( lat: {latitude} , {longitude} )")
    
    return latitude, longitude

def add_gps_to_image(input_file, output_file, latitude, longitude):
    photo = gpsphoto.GPSPhoto(input_file)

    # Criação do objeto GPSInfo com as coordenadas
    geo_tags = gpsphoto.GPSInfo((latitude, longitude))

    # Adiciona os dados GPS à imagem e salva em um novo arquivo
    photo.modGPSData(geo_tags, output_file)

    print(f"Novo arquivo salvo com Geotags: {output_file}")

def find_24M(text):
    padrao = r"24M"
    match = re.search(padrao, text)
    return match
    ...

def find_swiss(text):
    padrao = r"Swiss"
    match = re.search(r'swiss', text, re.IGNORECASE)
    return match

folder_path = "fotos/"
output_path = "fotos/editadas/"

pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

utm_zone = 24
hemisphere = "S"

is_ok = 0
total_files = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".jpeg"):
        total_files+=1
        print("-" * 50)
        # print(filename)
        file_path = os.path.join(folder_path,filename)
        output_file = output_path+filename

        extracted_text = tratar_img(file_path)
        # print(extracted_text)
      
        path = os.path.join(output_path,file_path)

        # print(f"file_path: {file_path}")

        is_utm = find_24M(extracted_text)
        is_swiss = find_swiss(extracted_text)

        # print(f"swiss {is_swiss}")
        numbers = extract_numbers(extracted_text)

        # if numbers:
        #     print(f"extracted: {filename}")
        #     print(extracted_text)



        
        
        # print(type(numbers))
        # print(extracted_text)

        easting,northing = 0,0
        
        has_northing = any(len(str(number)) == 6 for number in numbers)
        has_easting = any(len(str(number)) == 7 for number in numbers)




        if is_utm:
            if has_northing and has_easting:
                # print(f"extracted: {filename}")
                for number in numbers:
                    if len(str(number)) == 6:
                        easting = number
                    elif len(str(number)) == 7:
                        northing = number
                print(f"easting: {easting}  northing: {northing}")
                is_ok+=1
                latitude, longitude = utm_to_geographic(easting, northing, utm_zone, hemisphere)
                add_gps_to_image(file_path, output_file, latitude, longitude)
                os.remove(file_path)
            else:
                print(f"error in: {filename}")
                print(extracted_text)
            

        if is_swiss:
            print(f"extracted: {filename}")
            print(extracted_text)
            # print(numbers)
        else:
            print(f"extracted: {filename}")
            # print(extracted_text)

        # print(f"easting: {easting}  northing: {northing}")

        # 



        # print(f"easting: {easting}  northing: {northing}")
        





print("=" * 50)
print(f"is_ok: {is_ok}")
print(f"total: {total_files}")
print(f"eficiencia: {is_ok/total_files*100}%")