__author__ = 'Vostro3550'
import os
import sys
import codecs
from operator import attrgetter
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
arquivoenc = 1
dc = 3

#arq = open("DicLivro.txt","rb")
arq = open("inputs/pg74.txt","rb")
sai = open("DICCERTO.dic","w")
Ax = arq.read()

class Tripla():
    def __init__(self,vtri,vqtd):
        self.tri = []
        self.tri = vtri
        self.qtd = vqtd

print("ETAPA 1")
Triplas = []
SemRept = []
for x in range(len(Ax)-(dc-1)):
    trioEnt = Ax[x:x+dc]
    trip = []
    for t in trioEnt:
        trip.append(t)
    Triplas.append(trip)
    if trip not in SemRept:
        SemRept.append(trip)

    x+=1
print("ETAPA 2")
ComTot = [Tripla]
ComTot.clear()
for item in SemRept:
    tot = Triplas.count(item)
    ComTot.append((item,tot))

print("ETAPA 3")
ComTot.sort(key=lambda x: x[1])
print("ETAPA 4")
ComTot.reverse()
print("ETAPA 5")
for item in ComTot:
    for i in item[0]:
        sai.write(str(i)+" ")
    sai.write(str(item[1])+"\n")

sai.close()
print("ACABOU")


