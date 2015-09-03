__author__ = 'Vostro3550'

arq = open("DicLivro.txt","r")
dic = str(arq.read())

arq1 = open("trips.txt","w")

dic = dic.replace('\n',' ')

tTriplas = []
i=0
print('start')
while i < len(dic)-2:
    tripla = str(dic[i:i+3])
    tripla+='\n'
    if tTriplas.count(tripla) == 0:
        tTriplas.append(tripla)
        arq1.write(tripla)
    i+=1


arq1.close()