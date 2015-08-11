__author__ = 'Vostro3550'
import random
import os

def criachave():
    nCar = 256
    chave = []

    tenhochave = 0
    if not os.path.exists("dic.bin"):
        ascii = []
        for i in range(0,nCar):
            ascii.append(i)

        print(ascii)
        for i in range(nCar):
            rnd = random.randint(0,(len(ascii)-1))
            chave.append(ascii[rnd])
            ascii.remove(ascii[rnd])
        tenhochave = 1
        arq = open("dic.bin",'wb')

        for i in range(nCar):
            temp = bytes(chave[i])
            arq.write(temp)

        arq.close()

        print('Chave gerada!')

    if tenhochave == 0:
        arq = open("dic.bin",'rb')
        #for i in range(nCar):
        linha = arq.read()
        r = [l for l in linha]
        print(max(r),r)

        for i in range(0,len(linha)):
            print(chr(linha[i]))
           # div = linha.split(' ')
           # div[1]= div[1].replace('\n','')
          #  chave[i][0] = chr(int(div[0]))
         #   chave[i][1] = chr(int(div[1]))
        arq.close()

    return chave

def cifratexto(texto,chave):
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(splited)):
        ln = int(ord(splited[i]))
        ch  = chave[ln]
        splited[i] = ch

    texto = ''
    for i in range(0,len(splited)):
        texto += str(splited[i])
    print('\nCifrado : '+str(texto)+'\n')
    return texto

def pChave(chave,ca):
    for i in range(0,len(chave)):
        if chave[i][1] == ca:
            return i


def decifratexto(texto,chave):
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(texto)):
        ps = pChave(chave,texto[i])
        splited[i] = chr(ord(chave[ps][0]))

    texto = ''
    for i in range(0,len(splited)):
        texto += str(splited[i])
    print('Decifrado : '+str(texto)+'\n')
    return texto

arq = open("entrada.txt",'r')
entrada = arq.read()
print('Entrada : '+entrada)

chave = criachave()

cifrado = cifratexto(entrada,chave)
decifrado = decifratexto(cifrado,chave)

if entrada == decifrado:
    print('O processo de cifragem e decifragem ocorreu perfeitamente!')
else:
    print('Algou deu errado com o processo!')





