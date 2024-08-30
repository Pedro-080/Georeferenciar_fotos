from PIL import Image
import piexif

def add_gps_info(file_name, lat, lon):
    try:
        img = Image.open(file_name)
        exif_dict = piexif.load(img.info.get('exif', b''))
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
        return
    except IOError:
        print(f"Erro: Não foi possível abrir o arquivo {file_name}.")
        return

    # Converter latitude e longitude para o formato adequado
    def convert_to_degrees(value):
        degrees = int(value)
        minutes = int((value - degrees) * 60)
        seconds = (value - degrees - minutes/60) * 3600
        return ((degrees, 1), (minutes, 1), (int(seconds * 100), 100))

    lat_deg = convert_to_degrees(abs(lat))
    lon_deg = convert_to_degrees(abs(lon))

    lat_ref = 'N' if lat >= 0 else 'S'
    lon_ref = 'E' if lon >= 0 else 'W'

    gps_ifd = {
        piexif.GPSIFD.GPSLatitudeRef: lat_ref,
        piexif.GPSIFD.GPSLatitude: lat_deg,
        piexif.GPSIFD.GPSLongitudeRef: lon_ref,
        piexif.GPSIFD.GPSLongitude: lon_deg,
    }

    exif_dict['GPS'] = gps_ifd
    exif_bytes = piexif.dump(exif_dict)

    img.save(file_name, "jpeg", exif=exif_bytes)
    print(f"Coordenadas GPS adicionadas com sucesso ao arquivo {file_name}.")

# Exemplo de uso
fotos = 'fotos/1.jpeg'

ft_num = 1

add_gps_info(fotos, 37.7749, -122.4194)

