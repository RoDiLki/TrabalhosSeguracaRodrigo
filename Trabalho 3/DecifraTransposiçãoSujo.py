__author__ = 'Rodrigo'

import os


nChar = 256

nomeEnt = "outputs/pg1661.enc"

if os.path.exists(nomeEnt):
    arq = open(nomeEnt,'rb')
    Entrada = arq.read()
    print("Arquivo sujo lido!")
    arq.close()
else:
    print("Arquivo de origem nao encontrado!")

chave = 4

lin = set()

with open('DicPalavras.txt','r') as arq1:
    ent = []
    for line in arq1:
        ent.append(str(line).replace('\n',''))


    for i in range(len(ent)):
        lin.add(ent[i])

maior = 0
l1=[]
for i in Entrada:
    l1.append(i)

while True:
    chave += 1
    saida = []
    for i in range(len(l1)):
        saida.append(0)

    p = 0
    at =0

    for c in l1:
        if p >= len(l1):
            at += 1
            p = at
        saida[p] = c
        p += chave

    stri = (bytes(saida))
    stri1 = str(stri)
    equivalencias = 0

    for word in stri1.split():
        if word in lin:
            equivalencias += 1

    if equivalencias > maior:
        maior = equivalencias
        provChave = chave

    print('Total eq: ',equivalencias,' com a chave ',chave)
    if chave%50 == 0:
        print('Testadas 50 chaves\nChave com maior numero de equivalencias',provChave,' com total de',maior)
        input('press enter para rodar mais 50 chaves...')