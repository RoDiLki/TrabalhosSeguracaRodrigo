__author__ = 'Vostro3550'

import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE VIGENERE ---- ")
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
        EntCha = open(ChavEnt,"r")
        chave = EntCha.read()
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave não encontrado!")

    splited =[]
    for i in range(0,len(Entrada)):
        splited.append(Entrada[i])

    enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"w")
        pk = 0
        for i in range(0,len(splited)):
            if pk < len(chave):
                splited[i] = chr((int(ord(splited[i])) + int(ord(chave[pk])))%nChar)
                SaiArq.write(splited[i])
                pk += 1
            else:
                pk = 0
                splited[i] = chr((int(ord(splited[i])) + int(ord(chave[pk])))%nChar)
                SaiArq.write(splited[i])

        SaiArq.close()
        print("Arquivo gerado : "+NomSai)
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"w")
        pk = 0
        for i in range(0,len(splited)):
            if pk < len(chave):
                splited[i] = chr((ord(splited[i]) - ord(chave[pk]))%nChar)
                SaiArq.write(splited[i])
                pk += 1
            else:
                pk = 0
                splited[i] = chr((ord(splited[i]) - ord(chave[pk]))%nChar)
                SaiArq.write(splited[i])

        SaiArq.close()
        print("Arquivo gerado : "+NomSai)
    print("Processo Finalizado!")

    out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
    if out == 0:
        break
