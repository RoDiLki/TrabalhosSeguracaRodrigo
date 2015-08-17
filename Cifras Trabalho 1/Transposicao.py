__author__ = 'Vostro3550'

import math
import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE TRANSPOSICAO ---- ")

def conversion(matriz,texto,chave,cols,enc):
    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"w")
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"w")
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
    #print(matriz)

    for i in range(chave):
        for j in range(cols):
            SaiArq.write(matriz[i][j])

    matriz.clear();
    SaiArq.close()
    print("Arquivo gerado : "+NomSai)

while True:
    nChar = 127
    NomEnt = input("\n Arquivo de origem ->  ")
    enc = 0
    if os.path.exists(NomEnt):
        EntArq = open(NomEnt,"r")
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
        chave = Chave%nChar
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave não encontrado!")
        enc = 3

    if enc == 0:

        splited =[]
        for i in range(0,len(Entrada)):
            splited.append(Entrada[i])

        cols = math.ceil(len(Entrada)/chave)

        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        if enc == 1:
            matriz = [""] * chave
            for i in range(chave):
                matriz[i] = [""] * cols
            conversion(matriz,Entrada,chave,cols,enc)
        else:
            matriz = [""] * cols
            for i in range(cols):
                matriz[i] = [""] * chave
            conversion(matriz,Entrada,cols,chave,enc)

        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
            break
