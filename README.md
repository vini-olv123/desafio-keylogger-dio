## Estrutura
* `encrypter.py`: Script responsável por gerar uma chave, localizar arquivos em uma pasta alvo e criptografá-los.
* `decrypter.py`: Script que utiliza a chave gerada para descriptografar os arquivos e restaurar o acesso original.

## 🚀 Como Executar (Ambiente de Teste)
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca necessária:
   ```bash
   pip install cryptography
   ```
3. Crie uma pasta chamada `arquivos_alvo` e coloque arquivos de texto irrelevantes dentro.
4. Execute o `encrypter.py` para simular o ataque.
5. Execute o `decrypter.py` para simular a recuperação dos dados.

## 🛡️ Como se Proteger?
Andei pesquisando sobre, percebi que existem mais defesas contra ataques de sequestro de dados, como:
1. **Backups Regulares:** Manter cópias de segurança em locais offline ou na nuvem com versionamento.
2. **Atualização de Sistemas:** Manter o SO e softwares atualizados para corrigir brechas de segurança.
3. **Conscientização:** Não abrir anexos ou clicar em links de e-mails suspeitos (Phishing).
4. **Endpoint Protection (EDR/Antivírus):** Utilizar ferramentas que monitorem comportamentos suspeitos em tempo real.
