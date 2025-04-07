import os


def gerar_emails():
    print("""
    **************************************
    * GERADOR DE LISTA DE EMAILS          *
    **************************************
    """)

    # Opções de emails
    dominios = {
        '1': 'gmail.com',
        '2': 'outlook.com',
        '3': 'yahoo.com',
        '4': 'hotmail.com',
        '5': 'ifood.com',
        '6': 'customizado'
    }

    # Mostrar opções
    print("\nEscolha o domínio para os emails:")
    for key, value in dominios.items():
        print(f"{key} - {value}")

    # Obter escolha do usuário
    escolha = input("\nDigite o número da opção desejada ou '6' para customizar: ")

    # Validar escolha
    while escolha not in dominios:
        print("Opção inválida!")
        escolha = input("Digite o número da opção desejada: ")

    # Obter domínio
    if escolha == '6':
        dominio = input("Digite o domínio customizado (ex: empresa.com): ").lower()
        # Remover @ se o usuário digitou
        dominio = dominio.replace('@', '')
    else:
        dominio = dominios[escolha]

    # Pedir arquivo de entrada
    arquivo_entrada = input("\nDigite o caminho/nome do arquivo TXT com os nomes: ")

    # Verificar se arquivo existe
    while not os.path.exists(arquivo_entrada):
        print("Arquivo não encontrado!")
        arquivo_entrada = input("Digite o caminho/nome correto do arquivo TXT: ")

    # Pedir arquivo de saída
    arquivo_saida = input("\nDigite o nome do arquivo de saída (ex: emails.txt): ")

    # Processar arquivo
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f_entrada, \
                open(arquivo_saida, 'w', encoding='utf-8') as f_saida:

            for linha in f_entrada:
                nome = linha.strip()  # Remove espaços em branco e quebras de linha
                if nome:  # Só processa se a linha não estiver vazia
                    # Criar email: nome@dominio (em minúsculas e sem espaços)
                    email = f"{nome.replace(' ', '').lower()}@{dominio}\n"
                    f_saida.write(email)

        print(f"\nProcesso concluído! Emails gerados em {arquivo_saida}")
        print(f"Total de emails gerados: {sum(1 for line in open(arquivo_saida, 'r', encoding='utf-8'))}")

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")



if __name__ == "__main__":
    gerar_emails()