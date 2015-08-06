__author__ = 'Levinski'

def cifratexto(texto,chave):
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    pk = 0
    for i in range(0,len(splited)):
        if pk < len(chave):
            splited[i] = chr((int(ord(splited[i])) + int(ord(chave[pk])))%256)
            pk += 1
        else:
            pk = 0
            splited[i] = chr((int(ord(splited[i])) + int(ord(chave[pk])))%256)

    texto = ''
    for i in range(0,len(splited)):
        texto += splited[i]
    print('\n\nCifrado : '+texto+'\n')

    return texto


def decifratexto(texto,chave):

    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    pk = 0
    for i in range(0,len(splited)):
        if pk < len(chave):
            splited[i] = chr((ord(splited[i]) - ord(chave[pk]))%256)
            pk += 1
        else:
            pk = 0
            splited[i] = chr((ord(splited[i]) - ord(chave[pk]))%256)

    texto = ''
    for i in range(0,len(splited)):
        texto += splited[i]
    print('\nDecifrado : '+texto+'\n')

    return texto


arq = open("texto.txt",'r')
entrada = arq.read()

print('Entrada : '+entrada)


arq2 = open("chave.txt",'r')
chave = arq2.read()

#chave = chave%len(entrada)

print('Key : ',chave)

cifrado = cifratexto(entrada,chave)
decifrado = decifratexto(cifrado,chave)

if entrada == decifrado:
    print('O processo de cifragem e decifragem ocorreu perfeitamente!')
else:
    print('Algou deu errado com o processo!')
