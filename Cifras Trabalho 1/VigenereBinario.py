__author__ = 'Vostro3550'

import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE VIGENERE ---- ")
while True:
    nChar = 256
    NomEnt = input("\n Arquivo de origem ->  ")
    enc=0
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
        EntCha = open(ChavEnt,"rb")
        chave = EntCha.read()
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave não encontrado!")
        enc = 3

    if enc == 0:
        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        saida = []
        if enc == 1:
            NomSai = "Out.enc"
            SaiArq = open(NomSai,"wb")
            pk = 0
            for x in Entrada:
                if pk < len(chave):
                    saida.append((  x + chave[pk])%nChar)
                    #print(splited[i])
                    pk += 1
                else:
                    pk = 0
                    saida.append((x + chave[pk])%nChar)

            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("Arquivo gerado : "+NomSai)
        else:
            NomSai = "Out.dec"
            SaiArq = open(NomSai,"wb")
            pk = 0
            for x in Entrada:
                if pk < len(chave):
                    saida.append((  x - chave[pk])%nChar)
                    #print(splited[i])
                    pk += 1
                else:
                    pk = 0
                    saida.append((x - chave[pk])%nChar)
            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("Arquivo gerado : "+NomSai)
        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
            break
