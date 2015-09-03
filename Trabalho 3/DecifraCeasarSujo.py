__author__ = 'Vostro3550'

import os

nChar = 256

nomeEnt = "outputs/pg11.enc"

if os.path.exists(nomeEnt):
    arq = open(nomeEnt,'rb')
    Entrada = arq.read()
    print("Arquivo sujo lido!")
    arq.close()
else:
    print("Arquivo de origem nao encontrado!")
chave = 4
arq1 = open('trips.txt','r')
lin =[]
l = ""
while (l = arq1.readline()):
    l = arq1.readline()
    l = l.replace('\n','')
    lin.append(l)

while True:
    chave += 1
    saida = []
    for c in Entrada:
        saida.append((c + chave) % nChar)
    NomSai = "Decifrado.txt"
    SaiArq = open(NomSai,"wb")
    SaiArq.write(bytes(saida))
    SaiArq.close()
    print('Decifrado com chave',chave,' executar testes com triplas')

    #trp = arq1.read()

    i = 0
    equivalencias = 0
    while i < (len(saida)-2):
        s = ""
        tripla = str(saida[i:i+3])
        s += str(tripla[1])
        s += str(tripla[2])
        s += str(tripla[3])
        #print(s)
        for l in lin:
            if s == l:
                equivalencias += 1
        i+=3


    print('Total eq: ',equivalencias,' com a chave ',chave)

    input('press enter...')