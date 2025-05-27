# Dicionário com as substituições desejadas.
# Faltam as letras com acento.
substituicoes = {
    'A': 'A1', 'B': 'A2', 'C': 'A3', 'D': 'A4', 'E': 'A5', 'F': 'A6', 'G': 'A7', 'H': 'A8', 'I': 'A9',
    'J': 'B1', 'K': 'B2', 'L': 'B3', 'M': 'B4', 'N': 'B5', 'O': 'B6', 'P': 'B7', 'Q': 'B8', 'R': 'B9',
    'S': 'C1', 'T': 'C2', 'U': 'C3', 'V': 'C4', 'W': 'C5', 'X': 'C6', 'Y': 'C7', 'Z': 'C8',
    'Ã': 'A1',
}

# Input do usuário
#Função para retornar caso tenha algo errado.
def encriptar():
    texto = input("Digite o texto para encriptar: ").upper()
    texto_substituido = ""

    for letra in texto:
        if letra in substituicoes:
            texto_substituido += substituicoes[letra]
        else:
            print('Use apenas letras.')
            return encriptar()
    
    return texto_substituido

# Resultado
while True:
    resultado = encriptar()
    print("Texto encriptado:", resultado)

    while True:
#Perguntar se quer encriptar outro texto
        encriptarNovo = input('Deseja encriptar outro texto? (S/N): ').upper()
#If para retornar ao início
        if encriptarNovo == 'S' or encriptarNovo == 'SIM':
            break
#Elif para encerrar o programa
        elif encriptarNovo == 'N' or encriptarNovo == 'NAO' or encriptarNovo == 'NÃO':
            print('Encerrando o programa.')
            exit()
    #Mensagem e volta, caso a pessoa não digite o correto.
        else:
            print('Digite apenas S ou N, por favor.')