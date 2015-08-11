__author__ = 'Vostro3550'

name = str("teste.bin")
arq = open(name,"wb")
for i in range(256):
    temp = str(chr(i))
    data = temp.encode('utf-8')
    arq.write(data)

arq.close()

arq = open(name,"rb")
linha = arq.read()
r = [l for l in linha]

print(max(r),r)