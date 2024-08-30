import pandas as pd
from GPSPhoto import gpsphoto
from pyproj import Proj, transform

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


# Caminho para a planilha Excel
excel_file = 'tabela.xlsx'

# Ler a planilha
df = pd.read_excel(excel_file)
# print(df)


for index, row in df.iterrows():
    try:
        image_name = row['endereco']
        easting = row['Coord_x']
        northing = row['Coord_y']
        utm_zone = row['Zone']
        hemisphere = row['Hemisferio']  # Supondo que há uma coluna para o hemisfério

        latitude, longitude = utm_to_geographic(easting, northing, utm_zone, hemisphere)

        # Defina os arquivos de entrada e saída
        input_file = f'fotos/{image_name}'
        output_file = f'fotos/editadas/{image_name}'

        # Adicione as coordenadas geográficas à imagem
        add_gps_to_image(input_file, output_file, latitude, longitude)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
       

# input_file = 'fotos/1.jpeg'  # Substitua pelo caminho correto para o arquivo
# output_file = 'fotos/1_edit.jpeg'  # Nome do novo arquivo de saída

# photo = gpsphoto.GPSPhoto(input_file)

# tages = (33.6315, -111.9525)

# geotages = gpsphoto.GPSInfo(tages)

# photo.modGPSData(geotages,output_file)
# print("New fille saved With Geotages")