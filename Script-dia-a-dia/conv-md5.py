import hashlib

# Função para calcular o hash MD5 de uma senha
def calcular_md5(senha):
    md5 = hashlib.md5()
    md5.update(senha.encode('utf-8'))
    return md5.hexdigest()

# Nome do arquivo de entrada com as senhas em texto claro
arquivo_entrada = 'senhas.txt'

# Nome do arquivo de saída para os hashes MD5
arquivo_saida = 'pass-md5.txt'

# Lista para armazenar os hashes MD5
hashes_md5 = []

# Abra o arquivo de entrada e leia as senhas em texto claro
with open(arquivo_entrada, 'r') as arquivo:
    senhas = arquivo.readlines()

# Calcular o hash MD5 para cada senha e armazenar na lista
for senha in senhas:
    senha = senha.strip()  # Remova espaços em branco e quebras de linha
    hash_md5 = calcular_md5(senha)
    hashes_md5.append(hash_md5)

# Escrever os hashes MD5 no arquivo de saída
with open(arquivo_saida, 'w') as arquivo:
    for hash_md5 in hashes_md5:
        arquivo.write(hash_md5 + '\n')

print(f'Hashes MD5 foram salvos em {arquivo_saida}')
