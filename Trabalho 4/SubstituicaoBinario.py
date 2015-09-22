__author__ = 'Vostro3550'

import os
import random

ChavEnt = "dicionarioCERTO3.dic"

print(" ---- CIFRA DE SUBSTITUICAO ---- ")


def criachave(nCar):
    chave = []
    ascii = []

    for i in range(256):
        ascii.append(i)


    for i in range(nCar):
        rnd = random.randint(0,(len(ascii)-1))
        chave.append(ascii[rnd])
        ascii.remove(ascii[rnd])
    tenhochave = 1
    arq = open(ChavEnt,'wb')
    arq.write(bytes(chave))
    arq.close()
    print('Chave gerada!')
    print(chave)
    return chave

def lechave():
    chave =[]
    arq = open(ChavEnt,'rb')
    linha = arq.read()

    for i in linha:
        chave.append(i)
    arq.close()
    print('Chave Lida!')

    return chave

def pChave(chave,ca):
    j = 0;
    for i in chave:
        if i == ca:
            #print(i," == ",ca)
            #print(j)
            return j
        j+=1
    return 63;

while True:
    nChar = 256
    NomEnt = input("\n Arquivo de origem ->  ")
    enc = 0
    if os.path.exists(NomEnt):
        EntArq = open(NomEnt,"rb")
        Entrada = EntArq.read()

        print("Entrada Lida!")
        #print(Entrada)
        EntArq.close()
    else:
        print("Arquivo de entrada não encontrado!")
        enc = 3
    if os.path.exists(ChavEnt):
       chave = lechave()
    else:
       chave = criachave(nChar)


    if enc == 0:
        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        if enc == 1:
            NomSai = "Out.enc"
            SaiArq = open(NomSai,"wb")
            saida=[]
            for i in Entrada:
                ln = int(i);
                #print(ln ,' -> ',chave[ln])
                saida.append(chave[ln])
            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("Arquivo gerado : "+NomSai)
        else:
            NomSai = "Out.dec"
            SaiArq = open(NomSai,"wb")
            saida =[]
            for i in Entrada:
                ps = pChave(chave,i)
                #print(ps,' < - ',i)
                saida.append(ps)


            SaiArq.write(bytes(saida))

            SaiArq.close()
            print("Arquivo gerado : "+NomSai)

        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
            break
