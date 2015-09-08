__author__ = 'Vostro3550'

import os

nChar = 256

nomeEnt = "outputs/ax.enc"

if os.path.exists(nomeEnt):
    arq = open(nomeEnt,'rb')
    Entrada = arq.read()
    print("Arquivo sujo lido!")
    arq.close()
else:
    print("Arquivo de origem nao encontrado!")

lEnt = []
for e in Entrada:
    lEnt.append(e)


chaveTamanho = 1


fatias =[]
i = 1
nRept = 0
cRept = ''
repts = []

#Entrada.count(Entrada[i:i+chaveTamanho],0,len(Entrada))

while i < (len(Entrada)-chaveTamanho):
    ax = []
    ax.append(Entrada.count(Entrada[i:i+chaveTamanho],0,len(Entrada)))
    ax.append(Entrada[i:i+chaveTamanho])
    repts.append(ax)
    i+=chaveTamanho

for i in range(len(repts)):
    print(repts.count(repts[i]),repts[i][1])
    input()