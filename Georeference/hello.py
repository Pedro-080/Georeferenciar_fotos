import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image



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


pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"


if __name__ == "__main__":
    lista_relatorios = selecionar_fonte()[0]

    # arquivo_destino = selecionar_destino()
    print(F"LISTA: {lista_relatorios}")

    # image = Image.open(lista_relatorios)

    

    texto = pytesseract.image_to_string(lista_relatorios)

    

    print(texto)