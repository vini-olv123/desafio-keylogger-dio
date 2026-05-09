import os
from cryptography.fernet import Fernet

#1. Criar a pasta de teste se ela não existir
caminho_pasta = "arquivos_alvo"
if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)
    with open(f"{caminho_pasta}/teste.txt", "w") as f:
        f.write("Dados sensiveis de teste")

#2. Gerar a chave
key = Fernet.generate_key()
with open("chave.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

#3. Processo de Criptografia
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith("dados.txt"):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        
        try:
            with open(caminho_completo, "rb") as f:
                conteudo = f.read()
            
            conteudo_criptografado = fernet.encrypt(conteudo)
            
            with open(caminho_completo, "wb") as f:
                f.write(conteudo_criptografado)
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

print("Processo finalizado. Verifique a pasta 'arquivos_alvo'.")
