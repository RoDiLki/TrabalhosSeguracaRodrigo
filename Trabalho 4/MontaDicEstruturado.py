__author__ = 'Vostro3550'
import os
import sys
import codecs
from operator import attrgetter
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
arquivoenc = 0
dc = 1

if arquivoenc == 0:
    arq = open("DicLivro.txt","r")
    arq1 = open("trips1.txt","w")
    dic = str(arq.read())
    dic = dic.replace("\n",' ')
    dic = dic.replace("\t",' ')
    dic = dic.replace("\r",' ')

    class Tripla:
        def __init__(self,tri,qtd):
            self.tri = tri
            self.qtd = qtd

    tTriplas = []
    i=0
    tTriplasSet = set()
    print("ETAPA 1")

    while i < (len(dic)-(dc-1)):
        tripla = str(dic[i:i+dc])
        tTriplas.append(tripla)

        if tripla not in tTriplasSet:
            tTriplasSet.add(tripla)
        i+=1

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
else:
    arq = open("outputs/pg74.enc","rb")
    sai = open("TriplasEnc1.txt","w")
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
print("ACABOU")


