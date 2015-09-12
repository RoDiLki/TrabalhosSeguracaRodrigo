__author__ = 'Vostro3550'
import os
import sys
import codecs
from operator import attrgetter

arq = open("DicLivro.txt","r")
dic = str(arq.read())

arq1 = open("trips.txt","w")

dic = dic.replace('\n',' ')

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#print(dic)

#print(sys.stdout.encoding)

class Tripla:
    def __init__(self,tri,qtd):
        self.tri = tripla
        self.qtd = qtd

tTriplas = []
i=0
tTriplasSet = set()
print("ETAPA 1")

while i < len(dic)-2:
    tripla = str(dic[i:i+3])
    tTriplas.append(tripla)
    if tripla not in tTriplasSet:
        tTriplasSet.add(tripla)
    i+=1

#print(tTriplas)

ax = [Tripla]
ax.clear()

print("ETAPA 2")
for t in tTriplasSet:
    tot = tTriplas.count(t)
    ax.append((t,tot))

print("ETAPA 3")
ax.sort(key=lambda x: x[1])
print("ETAPA 4")
ax.reverse()

print("ETAPA 5")
for t in ax:
    arq1.write(t[0]+'|'+str(t[1])+'\n')

arq1.close()

print("ACABOU")


