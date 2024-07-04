from exif import Image

def add_gps_info(file_name, lat, lon):
    with open(file_name, 'rb') as img_file:
        img = Image(img_file)
    
    img.gps_latitude = (lat, 0, 0)
    img.gps_latitude_ref = 'N' if lat >= 0 else 'S'
    img.gps_longitude = (lon, 0, 0)
    img.gps_longitude_ref = 'E' if lon >= 0 else 'W'
    
    with open(file_name, 'wb') as new_img_file:
        new_img_file.write(img.get_file())

# Exemplo de uso
add_gps_info('minha_foto.jpg', 37.7749, -122.4194)
