from PIL import Image
import piexif
import os 

#abre a imagem
def open_image(file_name):
    try:
        img = Image.open(file_name)
        print(f"Imagem {file_name} aberta com sucesso.")
        return img
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
        return None
    except IOError:
        print(f"Erro: Não foi possível abrir o arquivo {file_name}.")
        return None

#carrega a imagem
def load_exif_data(img):
    try:
        exif_data = piexif.load(img.info.get('exif', b''))
        print("Metadados EXIF carregados com sucesso.")
        return exif_data
    except Exception as e:
        print(f"Erro ao carregar metadados EXIF: {e}")
        return None

#verifica dados de GPS
def has_gps_info(exif_data):
    gps_ifd = exif_data.get('GPS', {})
    if gps_ifd:
        lat = gps_ifd.get(piexif.GPSIFD.GPSLatitude)
        lon = gps_ifd.get(piexif.GPSIFD.GPSLongitude)
        if lat and lon:
            return True
    return False

# def add_gps_info_to_image(file_name, lat, lon):
#     img = open_image(file_name)
#     if img:
#         exif_data = load_exif_data(img)
#         if exif_data is None:
#             exif_data = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
        
#         add_gps_info(img, exif_data, lat, lon)

# def add_gps_info(img, exif_data, lat, lon):
#     lat_deg = convert_to_degrees(abs(lat))
#     lon_deg = convert_to_degrees(abs(lon))

#     lat_ref = 'N' if lat >= 0 else 'S'
#     lon_ref = 'E' if lon >= 0 else 'W'

#     gps_ifd = {
#         piexif.GPSIFD.GPSLatitudeRef: lat_ref,
#         piexif.GPSIFD.GPSLatitude: lat_deg,
#         piexif.GPSIFD.GPSLongitudeRef: lon_ref,
#         piexif.GPSIFD.GPSLongitude: lon_deg,
#     }

#     exif_data['GPS'] = gps_ifd
#     exif_bytes = piexif.dump(exif_data)

#     img.save(file_name, "jpeg", exif=exif_bytes)
#     print(f"Coordenadas GPS adicionadas com sucesso ao arquivo {file_name}.")


def add_gps_to_image(input_file, output_file, latitude, longitude):
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Arquivo '{input_file}' não encontrado.")
        
        # Abre a imagem
        img = Image.open(input_file)
        
        # Converte latitude e longitude para formato exigido pelo piexif
        lat_deg = (abs(latitude), 1)
        lon_deg = (abs(longitude), 1)
        lat_ref = 'N' if latitude >= 0 else 'S'
        lon_ref = 'E' if longitude >= 0 else 'W'
        
        exif_gps = {
            piexif.GPSIFD.GPSLatitudeRef: lat_ref,
            piexif.GPSIFD.GPSLatitude: lat_deg,
            piexif.GPSIFD.GPSLongitudeRef: lon_ref,
            piexif.GPSIFD.GPSLongitude: lon_deg,
        }
        
        # Carrega os metadados existentes da imagem
        exif_dict = piexif.load(img.info.get('exif', b'') or b'')
        
        # Atualiza ou adiciona os metadados GPS
        exif_dict['GPS'] = exif_gps
        
        # Converte de volta para o formato de bytes
        exif_bytes = piexif.dump(exif_dict)
        
        # Salva a imagem com os metadados atualizados
        img.save(output_file, "jpeg", exif=exif_bytes)
        
        print(f"Coordenadas GPS adicionadas com sucesso ao arquivo '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Erro ao adicionar coordenadas GPS: {e}")
    except Exception as e:
        print(f"Erro inesperado ao adicionar coordenadas GPS: {e}")
    



    # img.save(output_file, "jpeg", exif=exif_bytes)
    # print(f"Coordenadas GPS adicionadas com sucesso ao arquivo '{output_file}'.")


    
    # # Inicializa um novo conjunto de metadados EXIF se não existir
    # if not exif_data:
    #     exif_data = {'0th': {}, 'Exif': {}, 'GPS': {}}
    
    # lat_deg = (abs(latitude), 1)
    # lon_deg = (abs(longitude), 1)
    # lat_ref = 'N' if latitude >= 0 else 'S'
    # lon_ref = 'E' if longitude >= 0 else 'W'
    
    # gps_ifd = {
    #     piexif.GPSIFD.GPSLatitudeRef: lat_ref,
    #     piexif.GPSIFD.GPSLatitude: (lat_deg, (1, 1)),
    #     piexif.GPSIFD.GPSLongitudeRef: lon_ref,
    #     piexif.GPSIFD.GPSLongitude: (lon_deg, (1, 1)),
    # }
    
    # exif_data['GPS'] = gps_ifd
    # exif_bytes = piexif.dump(exif_data)
    
    # # img.save(output_file, "jpeg", exif=exif_bytes)
    # print(f"Coordenadas GPS adicionadas com sucesso ao arquivo '{output_file}'.")


        



# # Exemplo de uso do primeiro bloco
# file_name = 'fotos/1.jpeg'  # Substitua pelo caminho correto para o arquivo
# # file_name = 'fotos/test.jpg'  # Substitua pelo caminho correto para o arquivo

# image = open_image(file_name)

# # Exemplo de uso do quarto bloco
# if image:
#     exif_data = load_exif_data(image)
#     if exif_data and has_gps_info(exif_data):
#         print("A imagem possui metadados de coordenadas GPS.")
#     else:
#         print("A imagem não possui metadados de coordenadas GPS.")



# Exemplo de uso do código simplificado
input_file = 'fotos/1.jpeg'  # Substitua pelo caminho correto para o arquivo
output_file = 'fotos/1_edit.jpeg'  # Nome do novo arquivo de saída
latitude = 37.7749
longitude = -122.4194

add_gps_to_image(input_file, output_file, latitude, longitude)