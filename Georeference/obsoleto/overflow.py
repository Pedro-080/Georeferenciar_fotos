from PIL import Image
import piexif

def add_gps_to_image(input_file, output_file, latitude, longitude):
    try:
        # Abre a imagem
        img = Image.open(input_file)
        
        # Converte latitude e longitude para formato exigido pelo piexif
        lat_deg = (abs(latitude), 1)
        lon_deg = (abs(longitude), 1)
        lat_ref = 'N' if latitude >= 0 else 'S'
        lon_ref = 'E' if longitude >= 0 else 'W'
        
        # Verifica se existem metadados EXIF e carrega-os se existirem
        exif_dict = piexif.load(img.info.get('exif', b''))
        
        # Cria um novo conjunto de metadados EXIF se não existir
        if 'GPS' not in exif_dict:
            exif_dict['GPS'] = {}
        
        # Define os dados GPS
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = lat_ref
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = lat_deg
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = lon_ref
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = lon_deg
        
        # Converte de volta para o formato de bytes
        exif_bytes = piexif.dump(exif_dict)
        
        # Salva a imagem com os metadados atualizados
        img.save(output_file, "jpeg", exif=exif_bytes)
        
        print(f"Coordenadas GPS adicionadas com sucesso ao arquivo '{output_file}'.")
    except Exception as e:
        print(f"Erro ao adicionar coordenadas GPS: {e}")


# Exemplo de uso do código
input_file = 'fotos/1.jpeg'  # Substitua pelo caminho correto para o arquivo
output_file = 'fotos/1_test.jpeg'  # Nome do novo arquivo de saída
latitude = 37.7749
longitude = -122.4194

add_gps_to_image(input_file, input_file, latitude, longitude)
