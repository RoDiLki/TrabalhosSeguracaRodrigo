__author__ = 'Vostro3550'

import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE CEASAR ---- ")
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
        print("Arquivo de entrada nao encontrado!")

    if os.path.exists(ChavEnt):
        EntCha = open(ChavEnt,"r")
        Chave = int(EntCha.read())
        chave = Chave%nChar
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave nao encontrado!")




    splited =[]
    for i in range(0,len(Entrada)):
        splited.append(Entrada[i])

    enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

    if enc == 1:
        NomSai = "Out.enc"
        SaiArq = open(NomSai,"w")
        for i in range(0,len(splited)):
            splited[i] = chr((ord(splited[i]) + chave)%nChar)
            SaiArq.write(splited[i])
        SaiArq.close()
        print("Arquivo gerado : "+NomSai)
    else:
        NomSai = "Out.dec"
        SaiArq = open(NomSai,"w")
        for i in range(0,len(splited)):
            splited[i] = chr((ord(splited[i]) - chave)%nChar)
            SaiArq.write(splited[i])
        SaiArq.close()
        print("Arquivo gerado : "+NomSai)

    print("Processo Finalizado!")

    out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
    if out == 0:
        break
