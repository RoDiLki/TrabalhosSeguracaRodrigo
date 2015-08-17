__author__ = 'Vostro3550'

import os

ChavEnt = "Chave.txt"
print(" ---- CIFRA DE CEASAR ---- ")
while True:
    nChar = 256
    NomEnt = input("\n Arquivo de origem ->  ")
    enc = 0
    if os.path.exists(NomEnt):
        EntArq = open(NomEnt,"rb")
        Entrada = EntArq.read()
        print("Entrada Lida!")
        EntArq.close()
    else:
        print("Arquivo de entrada nao encontrado!")
        enc = 3

    if os.path.exists(ChavEnt):
        EntCha = open(ChavEnt,"r")
        Chave = int(EntCha.read())
        chave = Chave%nChar
        print("Chave Lida!")
        EntCha.close()
    else:
        print("Arquivo de Chave nao encontrado!")
        enc = 3

    if enc == 0:
        enc =int(input("\n1 - Criptografar\n2 - Descriptografar\n-> "))

        if enc == 1:
            saida = []
            NomSai = "Out.enc"
            SaiArq = open(NomSai,"wb")
            for c in Entrada:
                saida.append((c + chave) % nChar)
            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("Arquivo gerado : "+NomSai)
        else:
            saida = []
            NomSai = "Out.dec"
            SaiArq = open(NomSai,"wb")
            for c in Entrada:
                saida.append((c-chave) % nChar)
            SaiArq.write(bytes(saida))
            SaiArq.close()
            print("Arquivo gerado : "+NomSai)

        print("Processo Finalizado!")

        out = int(input("\n\n 0 - Sair \n 1 - De novo \n ->"))
        if out == 0:
            break
