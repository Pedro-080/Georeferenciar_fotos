from PIL import Image
import os
import hashlib



def calculate_hash(image_path):
    """Calcula o hash de uma imagem."""
    with Image.open(image_path) as img:
        img_hash = hashlib.md5(img.tobytes()).hexdigest()
    return img_hash




def remove_duplicates(folder_path):
    """Remove imagens duplicadas em uma pasta."""
    hashes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            img_hash = calculate_hash(image_path)

            print(img_hash)

            if img_hash in hashes:
                print(f"Duplicata encontrada: {filename}. Apagando...")
                # print(f"Duplicata encontrada: {filename}. Apagando...")
                os.remove(image_path)
            else:
                hashes[img_hash] = filename

    print("Processo concluído. Duplicatas removidas.")



folder_path = "fotos/"
diretorio_novo = "fotos/editadas/"


# Use o caminho da pasta onde estão as fotos


remove_duplicates(folder_path)
