from PIL import Image, ImageFilter, ImageOps
import pytesseract
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import re
from pyproj import Proj, transform

class Foto:
    def __init__(self,file):
        self.file = file
        self.test = self.Tratar_foto(self.file)
        self.texto = self.Tratar_img(self.file)
        self.coordenadas = self.Extrair_coordenadas(self.texto)    
        # self.geoTag = self._Gerar_gps_to_image(self.coordenadas)


    def Tratar_foto(self,file):
        print(f"File: {self.file}")
        ...


    def Tratar_img(self,input_file):
        # Carregar a imagem
        image = Image.open(input_file)

        width, height = image.size
        crop_box = (0, int(height * 0.8), width, height)  # (left, upper, right, lower)
        # cropped_image = self._crop_image(image, crop_box)
        cropped_image = image.crop(crop_box)


        # Converter para escala de cinza
        gray_image = cropped_image.convert('L')

        # Redimensionar a imagem usando Image.LANCZOS
        resized_image = gray_image.resize((gray_image.width * 3, gray_image.height * 3), Image.LANCZOS)


        # Aplicar binarização usando um threshold fixo
        binary_image = resized_image.point(lambda x: 0 if x < 235 else 255, '1')

        
        # Aplicar filtro de desfoque para suavizar a imagem
        filtered_image = binary_image.filter(ImageFilter.MedianFilter())
        # filtered_image.show()

        # config = r'--psm 6'

        # text = pytesseract.image_to_string(filtered_image,lang="eng",config=config)
        text = pytesseract.image_to_string(filtered_image,lang="eng")


        return text

    def _extract_numbers(self, text):
        # Regex para encontrar números inteiros e negativos
        pattern = r'-?\b\d+\b'
        numbers = re.findall(pattern, text)
        
        # Converter para inteiros
        return [int(num) for num in numbers]

    def _utm_to_geographic(self,easting, northing, zone=24, hemisphere='S'):
        # Crie um objeto de projeção para o sistema de coordenadas UTM
        utm_proj = Proj(proj='utm', zone=zone, ellps='WGS84', hemisphere=hemisphere, south=True)

        # Crie um objeto de projeção para o sistema de coordenadas geográficas
        geodetic_proj = Proj(proj='latlong', datum='WGS84')

        # Converta as coordenadas UTM para geográficas
        longitude, latitude = transform(utm_proj, geodetic_proj, easting, northing)

        
        return latitude, longitude



    def Extrair_coordenadas(self, texto):
        numbers = self._extract_numbers(texto)
        easting,northing = 0,0

        for number in numbers:
            if len(str(number)) == 7:
                northing = number
            if len(str(number)) == 6:
                easting = number
        # print(f"northing: {northing}")
        # print(f"easting: {easting}")

        latitude,longitude = self._utm_to_geographic(easting,northing)

        return (latitude,longitude)
        # print(f"longitude: {longitude}")
        # print(f"latitude: {latitude}")


    # def _Gerar_gps_to_image(self, coordenadas):
    #     photo = gpsphoto.GPSPhoto(input_file)

    #     # Criação do objeto GPSInfo com as coordenadas
    #     geo_tags = gpsphoto.GPSInfo((latitude, longitude))



    #     # Adiciona os dados GPS à imagem e salva em um novo arquivo
    #     photo.modGPSData(geo_tags, output_file)

    #     print(f"Novo arquivo salvo com Geotags: {output_file}")