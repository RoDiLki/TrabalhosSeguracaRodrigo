__author__ = 'Levinski'
import math

def conversion(matriz,texto,chave,cols):
    j=0
    k=0
    i=0
    while True:
        if i == len(texto):
            break
        if j < chave:
            matriz[j][k] = texto[i]
            i+=1
            j+=1
        else:
            j=0
            k+=1
    print(matriz)
    texto = ''
    for i in range(chave):
        for j in range(cols):
            texto += matriz[i][j]
    return texto

def cifratexto(texto,chave):
    cols = math.ceil(len(texto)/chave)
    matriz = [''] * chave
    for i in range(chave):
        matriz[i] = [''] * cols

    texto = conversion(matriz,texto,chave,cols)
    print('Cifrado : ',texto)
    return texto



def decifratexto(texto,chave):
    cols = math.ceil(len(texto)/chave)
    matriz = [''] * cols
    for i in range(cols):
        matriz[i] = [''] * chave
    texto = conversion(matriz,texto,cols,chave)
    print('Decifrado : ',texto)
    return texto


arq = open("entrada.txt",'r')
entrada = arq.read()

print('Entrada : '+entrada)


arq2 = open("chave.txt",'r')
chave = int(arq2.read())

chave = chave%len(entrada)

print('Key : ',chave)

cifrado = cifratexto(entrada,chave)
decifrado = decifratexto(cifrado,chave)

if entrada == decifrado:
    print('O processo de cifragem e decifragem ocorreu perfeitamente!')
else:
    print('Algou deu errado com o processo!')
