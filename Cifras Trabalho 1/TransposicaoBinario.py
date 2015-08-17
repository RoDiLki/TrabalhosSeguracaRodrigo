__author__ = 'Vostro3550'

import math
import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE TRANSPOSICAO ---- ")

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
        EntCha = open(ChavEnt,"r")
        Chave = int(EntCha.read())
        chave = Chave
        print("Chave Lida!")
        EntCha.close()
        if chave > len(Entrada):
            print("Chave demasiadamente grande em relação a entrada!")
            enc = 3
    else:
        print("Arquivo de Chave não encontrado!")
        enc = 3

    if enc == 0:

        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        if enc == 1:
            NomSai = "Out.enc"
            SaiArq = open(NomSai,"wb")
            saida = []
            for c in range(chave):
                p = c
                while p < len(Entrada):
                    saida.append(Entrada[p])
                    p += chave

            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("\nArquivo gerado : "+NomSai)
        else:
            NomSai = "Out.dec"
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
            print("\nArquivo gerado : "+NomSai)

        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
           break
