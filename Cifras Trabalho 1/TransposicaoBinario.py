__author__ = 'Vostro3550'

import math
import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE TRANSPOSICAO ---- ")

def conversion(texto,chave,cols,enc):
    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"wb")
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"wb")

    matriz = []

    chv = 0
    coluna = []
    for t in texto:
        if chv == chave:
            matriz.append(coluna)
            coluna = []
            chv = 0
        coluna.append(t)
        chv += 1

    if len(coluna) <= chave:
        while len(coluna) < chave:
            coluna.append(127)
        matriz.append(coluna)

    saida =[]
    ja=0
    for j in range(chave):
        for i in range(0,cols):
            if matriz[i][j] == 127 and i < cols and enc == 2:
                ja=1
            else:
                saida.append(matriz[i][j])

    SaiArq.write(bytes(saida))
    SaiArq.close()
    print("Arquivo gerado : "+NomSai)

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
    else:
        print("Arquivo de Chave não encontrado!")
        enc = 3

    if enc == 0:
        cols = math.ceil(len(Entrada)/chave)

        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        if enc == 1:

            conversion(Entrada,chave,cols,enc)
        else:
            conversion(Entrada,cols,chave,enc)

        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
           break
