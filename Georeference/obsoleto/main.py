from exif import Image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
from PIL import Image as pilimg


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
fotos = 'fotos/2.jpeg'

ft_num = 1

add_gps_info(fotos, 37.7749, -122.4194)


# # Abrir a imagem
img_pillow = pilimg.open(fotos)

# # Exibir a imagem
img_pillow.show()