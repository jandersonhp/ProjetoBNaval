# Dicionário com as substituições desejadas.
# Faltam as letras com acento.
substituicoes = {
    'A': 'A1', 'B': 'A2', 'C': 'A3', 'D': 'A4', 'E': 'A5', 'F': 'A6', 'G': 'A7', 'H': 'A8', 'I': 'A9',
    'J': 'B1', 'K': 'B2', 'L': 'B3', 'M': 'B4', 'N': 'B5', 'O': 'B6', 'P': 'B7', 'Q': 'B8', 'R': 'B9',
    'S': 'C1', 'T': 'C2', 'U': 'C3', 'V': 'C4', 'W': 'C5', 'X': 'C6', 'Y': 'C7', 'Z': 'C8',
    'Ã': 'A1',
}

# Input do usuário
texto = input("Digite o texto para encriptar: ").upper()

# Substituição
texto_substituido = ""

for letra in texto:
    if letra in substituicoes:
        texto_substituido += substituicoes[letra]
    else:
        texto_substituido += letra

# Resultado
print("Texto encriptado:", texto_substituido)
