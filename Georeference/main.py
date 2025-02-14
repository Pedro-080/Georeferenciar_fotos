from Foto import Foto

import tkinter as tk
from tkinter import filedialog, messagebox
import time
import re
from GPSPhoto import gpsphoto

# Grava o tempo inicial
inicio = time.time()



def selecionar_fonte():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivos_origem = filedialog.askopenfilenames(title="Selecione os arquivos para copiar")
    return arquivos_origem

def selecionar_destino():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    destino = filedialog.askdirectory(title="Selecione o diretório de destino")
    return destino

def add_gps_to_image(input_file,coordenadas, output_file = None ):
    photo = gpsphoto.GPSPhoto(input_file)

    # Criação do objeto GPSInfo com as coordenadas
    geo_tags = gpsphoto.GPSInfo(coordenadas)

    # Adiciona os dados GPS à imagem e salva em um novo arquivo
    photo.modGPSData(geo_tags, input_file)

    print(f"Novo arquivo salvo com Geotags: {output_file}")


if __name__ == "__main__":
    lista_de_fotos = selecionar_fonte()


    for file in lista_de_fotos:
        # if filename.endswith(".jpeg"):
        # print("-" * 50)
        # print(foto)
        foto = Foto(file)
        coordenadas = foto.coordenadas

        add_gps_to_image(file,coordenadas)

        print(coordenadas)


        # print(foto.texto)

        # is_utm = find_24M(foto.texto)
        # print(is_utm)

        # texto = pytesseract.image_to_string(foto)

        
        # numbers = extract_numbers(foto.texto)
        # print(numbers)






















# Grava o tempo final
fim = time.time()







# Calcula o tempo total decorrido
tempo_total = fim - inicio

print(f"Tempo de execução: {tempo_total:.4f} segundos")