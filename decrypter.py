import os
from cryptography.fernet import Fernet

#1. Carregar a chave gerada
with open("chave.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

#2. Localizar e descriptografar os arquivos
caminho_pasta = "arquivos_alvo"
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith("dados.txt"):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        
        with open(caminho_completo, "rb") as f:
            conteudo_criptografado = f.read()
        
        conteudo_original = fernet.decrypt(conteudo_criptografado)
        
        with open(caminho_completo, "wb") as f:
            f.write(conteudo_original)

print("Arquivos restaurados com sucesso!")
