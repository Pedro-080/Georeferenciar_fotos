import os

# Defina o diretório onde estão os arquivos
diretorio = "fotos/"
diretorio_novo = "fotos/editadas/"
# folder_path = "fotos/"
# output_path = "fotos/editadas/"

# Defina o novo nome base
novo_nome_base = 'L'

# Listar todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# print(arquivos)

# Filtrar apenas arquivos (ignorando diretórios)
arquivos = [f for f in arquivos if os.path.isfile(os.path.join(diretorio, f))]

# Renomear os arquivos sequencialmente
for i, nome_arquivo in enumerate(arquivos, start=27):
    # Extensão do arquivo
    extensao = os.path.splitext(nome_arquivo)[1]
    
    numero_formatado = str(i).zfill(3)

    # Novo nome do arquivo
    novo_nome = f"{novo_nome_base}{numero_formatado}{extensao}"

    # Caminho completo antigo e novo
    caminho_antigo = os.path.join(diretorio, nome_arquivo)
    caminho_novo = os.path.join(diretorio_novo, novo_nome)
    
    # Renomear o arquivo
    os.rename(caminho_antigo, caminho_novo)

print("Arquivos renomeados com sucesso!")
