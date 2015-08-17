__author__ = 'Vostro3550'

import os
import math

print(" ---- DECIFRA VIGENERE ---- ")

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
    l1=[]
    for i in Entrada:
        l1.append(i)
    l2=[]
    for i in Alvo:
        l2.append(i)

    NomSai = "Chave_Vigenere.txt"
    SaiArq = open(NomSai,"wb")
    tam = 0
    if len(l1) > len(l2):
        tam =  len(l2)
    else:
        tam = len(l1)
    pk = 0
    saida= []
    for x in range(tam):
        print('l1: ',l1[x],'  l2: ',l2[x])
        saida.append((l1[x] - l2[x])%nChar)
    SaiArq.write(bytes(saida))
    SaiArq.close()


    print("Decifrado com sucesso, chave no arquivo ",NomSai," !")


    print("\nProcesso Finalizado!")
