__author__ = 'Vostro3550'
import os
import sys
import codecs

arq = open("D1.txt","r")
dic = str(arq.read())

arq1 = open("trips.txt","w")

dic = dic.replace('\n',' ')

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print(dic)

#print(sys.stdout.encoding)

tTriplas = []
i=0
print('start')
while i < len(dic)-2:
    tripla = str(dic[i:i+3])
    ##tripla += '\n'
    #if tTriplas.count(tripla) == 0:
    tTriplas.append(tripla)
    #arq1.write(tripla)
    i+=1

print(tTriplas)

cnt = set()

for t in tTriplas:
    tot = tTriplas.count(t)
    if t not in cnt:
        cnt.add(t+'|'+str(tot))
        arq1.write(t+'|'+str(tot)+'\n')
print(cnt)


