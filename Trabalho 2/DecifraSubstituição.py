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

    saida = []
        #print('Saida : ',len(saida),'  Alvo : ',len(Alvo))
    for i in range(256):
        saida.append(0)

    for i in range(len(Entrada)):
        saida[Alvo[i]] = Entrada[i]


    print("Decifrado com sucesso !")
    NomSai = "Decifrado.txt"
    SaiArq = open(NomSai,"wb")
    SaiArq.write(bytes(saida))
    SaiArq.close()


    print("\nProcesso Finalizado!")
