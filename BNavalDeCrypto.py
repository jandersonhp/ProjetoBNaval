# Dicionário com as substituições desejadas.
substituicoes = {
'A1': 'A', 'A2': 'B', 'A3': 'C', 'A4': 'D', 'A5': 'E', 'A6': 'F', 'A7': 'G', 'A8': 'H', 'A9': 'I',
'B1': 'J', 'B2': 'K', 'B3': 'L', 'B4': 'M', 'B5': 'N', 'B6': 'O', 'B7': 'P', 'B8': 'Q', 'B9': 'R',
'C1': 'S', 'C2': 'T', 'C3': 'U', 'C4': 'V', 'C5': 'W', 'C6': 'X', 'C7': 'Y', 'C8': 'Z'
    }

# Input do usuário com o texto encriptado.
def decriptar():
    texto = input("\nCole o texto encriptado: ")
    texto_substituido = texto

#Fazer a substituição rodando cada chave e valor no dicionário.
    for chave, valor in substituicoes.items():
        texto_substituido = texto_substituido.replace(chave, valor)

    return texto, texto_substituido

# Resultado e texto original
while True:
    texto_encriptado, resultado = decriptar()
    print(f'\nTexto encriptado: {texto_encriptado}')
    print(f'Texto original: {resultado}')

    while True:
#Perguntar se quer desencriptografar outro texto
        decriptarNovo = input('\nDeseja desencriptografar outro texto? (S/N): ').strip().upper()
#If para retornar ao início
        if decriptarNovo in ('S', 'SIM'):
            break
#Elif para encerrar o programa
        elif decriptarNovo in ('NÃO', 'N', 'NAO', 'NO'):
            print('Encerrando o programa.\n')
            exit()
    #Mensagem e volta, caso a pessoa não digite o correto.
        else:
            print('Digite apenas S ou N, por favor.')