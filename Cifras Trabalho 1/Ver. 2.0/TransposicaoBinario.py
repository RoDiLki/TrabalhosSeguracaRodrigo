__author__ = 'Vostro3550'

import math
import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE TRANSPOSICAO ---- ")

def conversion(matriz,texto,chave,cols,enc):
    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"wb")
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"wb")

    for i in range(len(texto),(cols*chave)+1):
        texto += bytes(0)
    print(len(texto))
    j=0
    k=0
    i=0


    for t in texto:
        if j < chave:
            #matriz[j].append(texto[i])
            matriz[j][k] = t
            i+=1
            j+=1
        else:
            j=0
            k+=1
    #rint(matriz)

    saida =[]
    for i in range(chave):
        for j in range(cols):
            saida.append(matriz[i][j])

    for s in saida:
        SaiArq.write(bytes(s))


    matriz.clear();
    SaiArq.close()
    print("Arquivo gerado : "+NomSai)

while True:
    nChar = 256
    NomEnt = input("\n Arquivo de origem ->  ")

    if os.path.exists(NomEnt):
        EntArq = open(NomEnt,"rb")
        Entrada = EntArq.read()
        print("Entrada Lida!")
        #print(Entrada)
        EntArq.close()
    else:
        print("Arquivo de entrada não encontrado!")
        break

    if os.path.exists(ChavEnt):
        EntCha = open(ChavEnt,"r")
        Chave = int(EntCha.read())
        chave = Chave
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave não encontrado!")
        break

    cols = math.ceil(len(Entrada)/chave)

    enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

    if enc == 1:
        matriz = [bytes()] * chave
        for i in range(chave):
            matriz[i] = [bytes()] * cols
        conversion(matriz,Entrada,chave,cols,enc)
    else:
        matriz = [bytes()] * cols
        for i in range(cols):
            matriz[i] = [bytes()] * chave
        conversion(matriz,Entrada,cols,chave,enc)

    print("Processo Finalizado!")

    out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
    if out == 0:
        break
