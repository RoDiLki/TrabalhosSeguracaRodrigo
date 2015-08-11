__author__ = 'Vostro3550'

import os
import random

ChavEnt = "dic.dic"
print(" ---- CIFRA DE SUBSTITUICAO ---- ")


def criachave(nCar):
    chave = []
    ascii = []
    for i in range(0,nCar):
        ascii.append(i)

    for i in range(nCar):
        rnd = random.randint(0,(len(ascii)-1))
        chave.append(chr(ascii[rnd]))
        ascii.remove(ascii[rnd])
    tenhochave = 1
    arq = open("dic.dic",'w')

    for i in range(nCar):
        #temp = bytes(chave[i])

        arq.write(chave[i])
    arq.close()
    print('Chave gerada!')
    return chave

def lechave():
    chave =[]
    arq = open("dic.dic",'rb')
    linha = arq.read()
    r = [l for l in linha]
    #print(max(r),r)

    for i in range(0,len(r)):
        #print(chr(r[i]))
        chave.append(chr(r[i]))
    arq.close()

    return chave

def pChave(chave,ca):
    for i in range(0,len(chave)):
        if chave[i] == ca:
            return i


while True:
    nChar = 127
    NomEnt = input("\n Arquivo de origem ->  ")

    if os.path.exists(NomEnt):
        EntArq = open(NomEnt,"r")
        Entrada = EntArq.read()
        print("Entrada Lida!")
        #print(Entrada)
        EntArq.close()
    else:
        print("Arquivo de entrada não encontrado!")

    if os.path.exists(ChavEnt):
       chave = lechave()
    else:
       chave = criachave(nChar)


    splited =[]
    for i in range(0,len(Entrada)):
        splited.append(Entrada[i])

    enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"w")

        for i in range(0,len(splited)):
            ln = int(ord(splited[i]))
            ch  = chave[ln]
            splited[i] = ch
            SaiArq.write(splited[i])
        SaiArq.close()
        print("Arquivo gerado : "+NomSai)
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"w")
        for i in range(0,len(splited)):
            ps = pChave(chave,splited[i])
            splited[i] = chave[ps]
            SaiArq.write(splited[i])

        SaiArq.close()
        print("Arquivo gerado : "+NomSai)

    print("Processo Finalizado!")

    out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
    if out == 0:
        break
