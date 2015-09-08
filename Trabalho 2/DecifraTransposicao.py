__author__ = 'Vostro3550'

import os
import math

print(" ---- DECIFRA TRANSPOSICAO ---- ")

nChar = 256
#NomEnt = input("\n Arquivo de origem (Cifrado) ->  ")
NomEnt = "outputs/pg1342.enc"
enc = 0
if os.path.exists(NomEnt):
    EntArq = open(NomEnt,"rb")
    Entrada = EntArq.read()
    print("Origem Lida!")
    EntArq.close()
else:
    print("Arquivo de origem nao encontrado!")
    enc = 3

#NomAlvo = input("\n Arquivo Alvo (Decifrado) ->  ")
NomAlvo = "inputs/pg1342.txt"

if os.path.exists(NomAlvo):
    EntArq = open(NomAlvo,"rb")
    Alvo = EntArq.read()
    print("Alvo Lido!")
    EntArq.close()
else:
    print("Arquivo Alvo nao encontrado!")
    enc = 3

if enc == 0:
    chave = 2
    l1=[]
    for i in Entrada:
        l1.append(i)
    l2=[]
    for i in Alvo:
        l2.append(i)
    while True:
        print('Chave Atual: ',chave)
        if chave == len(Entrada):
            break

        saida = []
        for i in range(len(l1)):
            saida.append(0)

        p = 0
        at =0

        for c in l1:
            if p >= len(l1):
                at += 1
                p = at
            saida[p] = c
            p += chave

        dif = 0
        achou = 0
        for s in range(len(l2)):
            if saida[s] != l2[s]:
                dif = 1
                break



        if dif == 0:
            print("Decifrado com sucesso utilizando a chave ",chave," !")
            NomSai = "Decifrado.txt"
            SaiArq = open(NomSai,"wb")
            SaiArq.write(bytes(saida))
            SaiArq.close()
            break;
        else:
            chave += 1

    print("\nProcesso Finalizado!")
