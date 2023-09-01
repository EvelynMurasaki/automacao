import csv

# Função para separar os dados do arquivo CSV
def separar_dados(arquivo_csv):
    with open(arquivo_csv, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        resultados = []
        sucesso = 0
        falha = 0
        acao_requerida = 0
        for row in reader:
            try:
                application_name = row['Application Name']
                test_type = row['Test type']
                security_test_id = row['Security test ID']
                category = row['Category']
                result = row['Result']
                resultados.append([application_name, test_type, security_test_id, category, result])
                if result == 'Success':
                    sucesso += 1
                elif result == 'Fail':
                    falha += 1
                elif result == 'To be decided':
                    acao_requerida += 1
            except KeyError:
                print("Chave não encontrada no arquivo CSV. Verifique se o cabeçalho está correto.")
    resultados_ordenados = sorted(resultados, key=lambda x: (x[4] != 'Success', x[4] != 'Fail', x[4] != 'To be decided'))
    return resultados_ordenados, sucesso, falha, acao_requerida

# Arquivo CSV de exemplo
arquivo_csv = 'dados.csv'

# Separar os dados do arquivo CSV
resultados, sucesso, falha, acao_requerida = separar_dados(arquivo_csv)

# Exibir os resultados
print('Sucesso (Success):', sucesso)
print('Falha (Fail):', falha)
print('Ação requerida (To be decided):', acao_requerida)
print('')

print('Resultados separados:')
for resultado in resultados:
    print('Application Name:', resultado[0])
    print('Test type:', resultado[1])
    print('Security test ID:', resultado[2])
    print('Category:', resultado[3])
    print('Result:', resultado[4])
    print('------------------------')
