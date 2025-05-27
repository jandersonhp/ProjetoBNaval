# Dicionário com as substituições desejadas.
# Faltam as letras com acento.
substituicoes = {
    'A': 'A1', 'B': 'A2', 'C': 'A3', 'D': 'A4', 'E': 'A5', 'F': 'A6', 'G': 'A7', 'H': 'A8', 'I': 'A9',
    'J': 'B1', 'K': 'B2', 'L': 'B3', 'M': 'B4', 'N': 'B5', 'O': 'B6', 'P': 'B7', 'Q': 'B8', 'R': 'B9',
    'S': 'C1', 'T': 'C2', 'U': 'C3', 'V': 'C4', 'W': 'C5', 'X': 'C6', 'Y': 'C7', 'Z': 'C8',
    'Ã': 'A1', 'Á': 'A1', 'À': 'A1',
    'Õ': 'B6', 'Ó': 'B6', 'Ô': 'B6',
    'É': 'A5', 'Ê': 'A5', 
    ' ': ' ', '!': '!', '?': '?', ',': ',',
    }

# Input do usuário e transformar o texto todo em maiúsculo.

def encriptar():
    texto = input("Digite o texto para encriptar: ").upper()
    texto_substituido = ""

# Substituição das letras no dicionário.
    for letra in texto:
        if letra in substituicoes:
            texto_substituido += substituicoes[letra]

#Função para retornar caso tenha algo errado.
        else:
            print('Tente remover os acentos e/ou caracteres especiais, e tente novamente: ')
            return encriptar()
    
    return texto, texto_substituido

# Resultado e texto original
# Texto original com F-String (Só pra eu me lembrar que existe f-string)
while True:
    texto_original, resultado = encriptar()
    print(f'Texto original:' + texto_original)
    print('Texto encriptado:', resultado)

    while True:
#Perguntar se quer encriptar outro texto
        encriptarNovo = input('Deseja encriptar outro texto? (S/N): ').upper()
#If para retornar ao início
        if encriptarNovo in ('S', 'SIM'):
            break
#Elif para encerrar o programa
        elif encriptarNovo in ('NÃO', 'N', 'NAO', 'NO'):
            print('Encerrando o programa.')
            exit()
    #Mensagem e volta, caso a pessoa não digite o correto.
        else:
            print('Digite apenas S ou N, por favor.')