__author__ = 'Vostro3550'

dicArq = open("trips3.txt","r")
encArq = open("TriplasEnc3.txt","r")
dicSai = open("dicionario3.dic","wb")
tcomb = 3
class Tripla():
    def __init__(self,vtri,vqtd):
        self.tri = []
        self.tri = vtri
        self.qtd = vqtd

Dic = [Tripla]
Dic.clear()
while True:
    line = dicArq.readline();
    line.replace('\n',"")
    if not line:
        break
    tr = line.split("|")
    trip =[]
    for c in tr[0]:
        trip.append(ord(c))
    Dic.append((trip,int(tr[1])))

print((Dic))
#print(Dic[:20])

Enc = [Tripla]
Enc.clear()
while True:
    line = encArq.readline();
    line.replace('\n',"")
    if not line:
        break
    tr = line.split()

    trip =[]
    trip.append(int(tr[0]))
    if tcomb == 2 or tcomb == 3:
        trip.append(int(tr[1]))
    if tcomb == 3:
        trip.append(int(tr[2]))

    Enc.append((trip,int(tr[tcomb])))

print((Enc))
#print(Enc[:20])


print("Montar possivel dicionario")

PossivelDic = []
for i in range(256):
    PossivelDic.append(0)

i = 0
while i <= 80:
    nodic = Dic[i][0]
    noenc = Enc[i][0]
    print(nodic[0])
    if PossivelDic[nodic[0]] == 0:
        PossivelDic[nodic[0]] = noenc[0]
    if tcomb == 2 or tcomb == 3:
        if PossivelDic[nodic[1]] == 0:
            PossivelDic[nodic[1]] = noenc[1]
    if tcomb == 3:
        if PossivelDic[nodic[2]] == 0:
            PossivelDic[nodic[2]] = noenc[2]

    i+=1

print(len(PossivelDic),PossivelDic)
equiv = 0
for i in PossivelDic:
    if i != 0:
        equiv += 1
print(equiv,"  letras encontradas")
dicSai.write(bytes(PossivelDic))
