__author__ = 'Vostro3550'

import os
import n

print(" ---- DECIFRA CEASAR ---- ")

nChar = 256
#NomEnt = input("\n Arquivo de origem (Cifrado) ->  ")
NomEnt = "outputs/pg11.enc"
enc = 0
if os.path.exists(NomEnt):
    EntArq = open(NomEnt,"rb")
    Entrada = EntArq.read()
    print("Origem Lida!")
    EntArq.close()
else:
    print("Arquivo de origem nao encontrado!")
    enc = 3

#NomAlvo = input("\n Arquivo Alvo (Decifrado) ->  ")
NomAlvo = "inputs/pg11.txt"
if os.path.exists(NomAlvo):
    EntArq = open(NomAlvo,"rb")
    Alvo = EntArq.read()
    print("Alvo Lido!")
    EntArq.close()
else:
    print("Arquivo Alvo nao encontrado!")
    enc = 3

if enc == 0:
    chave = 1
    if Entrada[0] > Alvo[0]:
        enc = 2
        chave = Entrada[0] - Alvo[0]
    else:
        enc = 1
        chave = Alvo[0] - Entrada[0]

    if enc == 1:
        saida = []
        NomSai = "Decifrado.txt"
        SaiArq = open(NomSai,"wb")
        for c in Entrada:
            saida.append((c + chave) % nChar)
        SaiArq.write(bytes(saida))
        SaiArq.close()
        print("\nArquivo gerado : "+NomSai)
        dif = 0
        for  a in range(len(Alvo)):
            if saida[a] != Alvo[a]:
                dif = 1
                break
        if dif == 0:
            print("Decifrado com sucesso utilizando a chave ",chave," !")
        else:
            print("Opps parece que a cifra usada nao e ceasar ou a chave esta errada")
    else:
        saida = []
        NomSai = "Decifrado.txt"
        SaiArq = open(NomSai,"wb")
        for c in Entrada:
            saida.append((c-chave) % nChar)
        SaiArq.write(bytes(saida))
        SaiArq.close()
        print("\nArquivo gerado : "+NomSai)

        dif = 0
        for s in range(len(saida)):
            if saida[s] != Alvo[s]:
                dif = 1
                break
        if dif == 0:
            print("Decifrado com sucesso utilizando a chave ",chave," !")
        else:
            print("Opps parece que a cifra usada nao e ceasar ou a chave esta errada")
    print("\nProcesso Finalizado!")
