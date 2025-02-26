import itertools

# Mapeamento de substituições para "leet speak"
leet_dict = {
    'a': ['a', '4', '@'],
    'b': ['b', '8'],
    'e': ['e', '3'],
    'g': ['g', '9', '6'],
    'i': ['i', '1', '!'],
    'l': ['l', '1', '|'],
    'o': ['o', '0'],
    's': ['s', '5', '$'],
    't': ['t', '7', '+'],
    'm': ['m', 'M'],
    'n': ['n', 'N']
}

# Pede a palavra base
palavra_base = input("Digite a palavra base: ")

def gerar_leet_variacoes(palavra):
    possibilidades = []
    for letra in palavra:
        if letra.lower() in leet_dict:
            possibilidades.append(leet_dict[letra.lower()])
        else:
            possibilidades.append([letra])

    return ["".join(p) for p in itertools.product(*possibilidades)]

def adicionar_sufixos(wordlist):
    sufixos = ['', '123', '2024', '!', '@', '#', '01', '007', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
    return [palavra + suf for palavra in wordlist for suf in sufixos]

wordlist = gerar_leet_variacoes(palavra_base)
wordlist = adicionar_sufixos(wordlist)
with open("wordlist_personalizada.txt", "w", encoding="utf-8") as arquivo:
    for palavra in wordlist:
        arquivo.write(palavra + "\n")

print(f" Wordlist criada com {len(wordlist)} palavras! Arquivo: wordlist_personalizada.txt")
