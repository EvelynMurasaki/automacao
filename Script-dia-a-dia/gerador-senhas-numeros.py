import random

# Aponta aqui quantos numeros aleatorios voce quer gerar, sei la 10 e vai gerar 10 numeros aleatorios
quantidade = 10

with open("numeros_9_digitos_aleatorio.txt", "w") as f:
    gerados = set()
    while len(gerados) < quantidade:
        numero = f"{random.randint(0, 999999999):09d}"
        if numero not in gerados:
            f.write(f"{numero}\n")
            gerados.add(numero)
