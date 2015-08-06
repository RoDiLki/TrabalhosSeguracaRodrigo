import random
import os
import math

def menuOP ():
    menu = input("\n\nMetodo de Cifragem \n 1- Cifra de Ceasar \n 2- Cifra de Transposicao \n 3- Cifra de Vigenere \n 4- Cifra de Substituicao \n 0- Sair \n-> ")
    return int(menu)

###################################################################################

def criachave():
    nCar = 127
    chave = ['']*nCar
    for i in range(nCar):
        chave[i] = ['']*2

    tenhochave = 0
    if not os.path.exists("dic.txt"):
        ascii = []
        for i in range(0,nCar):
            ascii.append(chr(i))

        for i in range(nCar):
            chave[i][0] = ascii[i]

        for i in range(nCar):
            rnd = random.randint(0,(len(ascii)-1))
            chave[i][1] = ascii[rnd]
            ascii.remove(ascii[rnd])
        tenhochave = 1
        arq = open("dic.txt",'w')
        for i in range(nCar):
            a = int(ord(chave[i][0]))
            b = int(ord(chave[i][1]))
            temp = str(a)+' '+str(b)+'\n'

            arq.write(temp)
        arq.close()
        print('Chave gerada!')

    if tenhochave == 0:
        arq = open("dic.txt",'r')
        for i in range(nCar):
            linha = arq.readline()
            div = linha.split(' ')
            div[1]= div[1].replace('\n','')
            chave[i][0] = chr(int(div[0]))
            chave[i][1] = chr(int(div[1]))
        arq.close()

    return chave

############################################################################

def cifratextoS(texto,chave):
    print("\n\nSUBISTUICAO\n")
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(splited)):
        ln = int(ord(splited[i]))
        ch  = chave[ln][1]
        splited[i] = ch

    texto = ''
    for i in range(0,len(splited)):
        texto += str(splited[i])
    print('\nCifrado : '+str(texto)+'\n')
    return texto

##################################################################################

def pChave(chave,ca):
    for i in range(0,len(chave)):
        if chave[i][1] == ca:
            return i

##################################################################################

def decifratextoS(texto,chave):
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

#######################################################################

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
    texto = ''
    for i in range(chave):
        for j in range(cols):
            texto += matriz[i][j]
    return texto

##############################################################################

def cifratextoT(texto,chave):
    print("\n\nTRANSPOSICAO")
    cols = math.ceil(len(texto)/chave)
    matriz = [''] * chave
    for i in range(chave):
        matriz[i] = [''] * cols

    texto = conversion(matriz,texto,chave,cols)
    print('Cifrado : ',texto)
    return texto
################################################################################

def decifratextoT(texto,chave):
    cols = math.ceil(len(texto)/chave)
    matriz = [''] * cols
    for i in range(cols):
        matriz[i] = [''] * chave
    texto = conversion(matriz,texto,cols,chave)
    print('Decifrado : ',texto)
    return texto

################################################################################

def cifratextoV(texto,chave):
    print("\n\nVIGENERE\n")
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

    texto= ''
    print(splited)
    for i in range(0,len(splited)):
        texto += splited[i]
    print('Cifrado : ',texto)

    return texto

############################################################################

def decifratextoV(texto,chave):
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

###################################################################################

def cifratextoC (texto,chave):
    print("\n\nCEASAR\n")
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(splited)):
        splited[i] = chr((ord(splited[i]) - chave)%256)

    texto = ''
    for i in range(0,len(splited)):
        texto += splited[i]
    print('cifrado : '+texto+'\n')
    return texto

###############################################################################

def decifratextoC (texto,chave):
    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(splited)):
            splited[i] = chr((ord(splited[i]) + chave)%256)


    texto= ''
    for i in range(0,len(splited)):
        texto += splited[i]
    print('Decifrado : '+texto+'\n')
    return  texto

######################################################################################

while True:
    arq = open("entrada.txt",'r')
    entrada = arq.read()
    menu = menuOP()
    decifrado = ''
    if menu == 1:
        chave = input("Digite a chave(numero): ")
        chave = int(chave)%256
        cifrado = cifratextoC(entrada,chave)
        decifrado = decifratextoC(cifrado,chave)
    elif menu == 2:
        chaveT = input("Digite a chave(numero) : ")
        chaveT = int(chaveT)%len(entrada)
        cifrado = cifratextoT(entrada,chaveT)
        decifrado = decifratextoT(cifrado,chaveT)
    elif menu == 3:
        chaveV = input("Digite a chave(texto/numero) : ")
        cifrado = cifratextoV(entrada,str(chaveV))
        decifrado = decifratextoV(cifrado,chaveV)
    elif menu == 4:
        chaveS = criachave()
        cifrado = cifratextoS(entrada,chaveS)
        decifrado = decifratextoS(cifrado,chaveS)
    elif menu == 0:
        break

    if entrada == decifrado:
        print('O processo de cifragem e decifragem ocorreu perfeitamente!')
    else:
        print('Algou deu errado com o processo!')