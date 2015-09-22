__author__ = 'Vostro3550'

dicArq = open("trips33.dic","r")
encArq = open("DICCERTO.dic","r")
dicSai = open("dicionarioCERTO3.dic","wb")
tcomb = 3

class Tripla():
    def __init__(self,vtri,vqtd):
        self.tri = []
        self.tri = vtri
        self.qtd = vqtd

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

Dic = [Tripla]
Dic.clear()
while True:
    line = dicArq.readline();
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

    Dic.append((trip,int(tr[tcomb])))

print((Dic))
#print(Enc[:20])


print("Montar possivel dicionario")
cx = 63
PossivelDic = []
for i in range(256):
    PossivelDic.append(cx)

i = 0

while i <= 20:
    nodic = Dic[i][0]
    noenc = Enc[i][0]
    #print(nodic[0])
    if PossivelDic[nodic[0]] == cx and noenc[0] not in PossivelDic:
        PossivelDic[nodic[0]] = noenc[0]
    if tcomb == 2 or tcomb == 3:
        if PossivelDic[nodic[1]] == cx and noenc[1] not in PossivelDic:
            PossivelDic[nodic[1]] = noenc[1]
    if tcomb == 3:
        if PossivelDic[nodic[2]] == cx and noenc[2] not in PossivelDic:
            PossivelDic[nodic[2]] = noenc[2]

    i+=1

print("Dicionario: ",PossivelDic)
equiv = 0
for i in PossivelDic:
    if i != cx:
        equiv += 1

print(nodic);

print(equiv,"  letras encontradas")
dicSai.write(bytes(PossivelDic))
