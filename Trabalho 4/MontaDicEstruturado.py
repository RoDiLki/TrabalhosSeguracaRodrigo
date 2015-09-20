__author__ = 'Vostro3550'
import os
import sys
import codecs
from operator import attrgetter
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

arquivoenc = 1
if arquivoenc == 0:
    arq = open("DicLivro.txt","r")
    arq1 = open("trips.txt","w")
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

    while i < len(dic)-2:
        tripla = str(dic[i:i+3])
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
    arq = open("D1.txt","rb")
    arq1 = open("tripsEnc1.txt","w")
    Ax = arq.read()
    trio = []*3
    tTriplas = [trio]

    class Tripla:
        def __init__(self,id,tri,qtd):
            self.id = id
            self.tri = [tri] #tri
            self.qtd = qtd

    print("ETAPA 1")
    tTriplasSet = [trio]
    for x in range(len(Ax)-2):

        trio = Ax[x:x+3]
        xxx = []
        xxx.append(trio[0])
        xxx.append(trio[1])
        xxx.append(trio[2])
        tTriplas.append(xxx)
        achou = 0
        for st in tTriplasSet:
            print(st)
            if st[1][0] == xxx[0] and st[1][1] == xxx[1] and st[1][2] == xxx[2]:
                achou = 1
                break

        if achou == 0:
            tTriplasSet.add(xxx)
        x+=1

    print(tTriplasSet)
    input()
    sax = [Tripla]
    sax.clear()
    print("ETAPA 2")
    i=1
    for t in tTriplasSet:
        tot = tTriplas.count(t)
        sax.append((i,t,tot))
        i+=1
    print("ETAPA 3")
    sax.sort(key=lambda x: x[1])
    print("ETAPA 4")
    sax.reverse()

    print("ETAPA 5")
    for t in sax:
        arq1.write(str(t[0][0])+" "+str(t[0][1])+" "+str(t[0][2])+'|'+str(t[1]))
    arq1.close()
print("ACABOU")


