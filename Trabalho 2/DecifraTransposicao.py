__author__ = 'Vostro3550'

import os
import math

print(" ---- DECIFRA TRANSPOSICAO ---- ")

nChar = 256
NomEnt = input("\n Arquivo de origem (Cifrado) ->  ")
enc = 0
if os.path.exists(NomEnt):
    EntArq = open(NomEnt,"rb")
    Entrada = EntArq.read()
    print("Origem Lida!")
    EntArq.close()
else:
    print("Arquivo de origem nao encontrado!")
    enc = 3

NomAlvo = input("\n Arquivo Alvo (Decifrado) ->  ")
if os.path.exists(NomAlvo):
    EntArq = open(NomAlvo,"rb")
    Alvo = EntArq.read()
    print("Alvo Lido!")
    EntArq.close()
else:
    print("Arquivo Alvo nao encontrado!")
    enc = 3

if enc == 0:
    chave = 1
    while True:
        print('Chave Atual: ',chave)
        if chave == len(Entrada):
            break

        NomSai = "Decifrado.txt"
        SaiArq = open(NomSai,"wb")
        saida = ['0']*len(Entrada)
        p = 0
        at =0
        for c in Entrada:
            if p >= len(Entrada):
                at += 1
                p = at
            saida[p] = c
            p += chave

        SaiArq.write(bytes(saida))
        SaiArq.close()

        #print('Saida : ',len(saida),'  Alvo : ',len(Alvo))
        tam = 0
        if len(saida) > len(Alvo):
            tam =  len(saida)
        else:
            tam = len(Alvo)
        for s in range(tam):
            if saida[s] != Alvo[s]:
                print('Posicao erro - ',s)
                dif = 1
                break
        if dif == 0:
            print("Decifrado com sucesso utilizando a chave ",chave," !")
            break;
        else:
            chave += 1

    print("\nProcesso Finalizado!")
