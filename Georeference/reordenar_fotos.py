import os

# Defina o diretório onde estão os arquivos
diretorio = "Georeference/fotos/"
diretorio_novo = "Georeference/fotos/editadas/"

# Listar todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Filtrar apenas arquivos (ignorando diretórios)
arquivos = [f for f in arquivos if os.path.isfile(os.path.join(diretorio, f))]


# Criar um dicionário para armazenar os arquivos com a posição como chave
dicionario_arquivos = {index: arquivo for index, arquivo in enumerate(arquivos)}


#Definindo arquivos de limites
nome_arquivo1 = "BM07 - SDP-14.01.JPG"
nome_arquivo2 = "BM07 - SDP-14.20.JPG"

# #Definindo arquivos de limites
# nome_arquivo1 = "TAG_name.01.JPG"
# nome_arquivo2 = "TAG_name.20.JPG"



# Buscar as chaves correspondentes aos nomes dos arquivos
key_arquivo1 = next((key for key, value in dicionario_arquivos.items() if value == nome_arquivo1), None)
key_arquivo2 = next((key for key, value in dicionario_arquivos.items() if value == nome_arquivo2), None)

# Ordenar as chaves para garantir que percorramos no intervalo correto
chave_inicial, chave_final = sorted([key_arquivo1, key_arquivo2])


# for key, value in dicionario_arquivos.items():
#     if key>= chave_inicial and key<= chave_final:

#         print(f"{key} : {value}")




def copiar_renomeado(diretorio, nome_base):
    i = 1
    novo_nome = nome_base
    caminho_novo = os.path.join(diretorio, novo_nome)

    # Incrementar o sufixo até encontrar um nome que não existe
    while os.path.exists(caminho_novo):
        novo_nome = f"{nome_base}"
        caminho_novo = os.path.join(diretorio, novo_nome)
        i += 1

    return caminho_novo    


# for key, value in dicionario_arquivos.items():
#     if key>= chave_inicial and key<= chave_final:

#         print(f"{key} : {value}")



# for i, key in enumerate(range(chave_inicial, chave_final + 1), start=1):
#     print(f"{key} : {value}")



if __name__ == "__main__":
    for i, key in enumerate(range(chave_inicial, chave_final + 1), start=1):
        # Obter o nome atual do arquivo
        nome_atual = dicionario_arquivos[key]

        # Criar o novo nome no formato desejado, com 'i' formatado para dois dígitos
        novo_nome_temporario = f"TAG_name.{str(i).zfill(2)}.JPG"
        novo_nome = f"BM07 - SDP-14.{str(i).zfill(2)}.JPG"

        
        print(f"{nome_atual} - {novo_nome_temporario}")

        # Caminho completo para os arquivos
        caminho_atual = os.path.join(diretorio, nome_atual)

        # print(caminho_atual)

        caminho_novo_temporario = os.path.join(diretorio, novo_nome_temporario)
        caminho_novo = os.path.join(diretorio, novo_nome)

        # print(caminho_novo)

    #     caminho_novo = copiar_renomeado(diretorio_novo, novo_nome_temporario)

        # Renomear o arquivo
        os.rename(caminho_atual, caminho_novo_temporario)
        # os.rename(caminho_atual, caminho_novo)


        
    #     # Atualizar o dicionário com o novo nome
    #     dicionario_arquivos[key] = novo_nome


    for i, key in enumerate(range(chave_inicial, chave_final + 1), start=1):
        print(f"{key} : {value}")

    # for i, key in enumerate(range(chave_inicial, chave_final + 1), start=1):
    #     # Obter o nome atual do arquivo
    #     nome_atual = dicionario_arquivos[key]

    #     # Criar o novo nome no formato desejado, com 'i' formatado para dois dígitos
    #     novo_nome = f"BM07 - SDP-14.{str(i).zfill(2)}.JPG"

    #     # Caminho completo para os arquivos
    #     caminho_atual = os.path.join(diretorio, nome_atual)

    #     # caminho_novo = os.path.join(diretorio_novo, novo_nome)
    #     caminho_novo = copiar_renomeado(diretorio_novo, novo_nome)

    #     # Renomear o arquivo
    #     os.rename(caminho_atual, caminho_novo)
        
    #     # Atualizar o dicionário com o novo nome
    #     dicionario_arquivos[key] = novo_nome







    # for key, value in dicionario_arquivos.items():
    #     if key>= chave_inicial and key<= chave_final:

    #         print(f"{key} : {value}")

    # # print("hello world")



