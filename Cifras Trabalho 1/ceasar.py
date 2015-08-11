__author__ = 'Levinski'
import sys

def decifratexto (texto,chave):

    splited = []
    for i in range(0,len(texto)):
        splited.append(texto[i])

    for i in range(0,len(splited)):
            splited[i] = chr((ord(splited[i]) + chave)%256)


    texto= ''
    for i in range(0,len(splited)):
        texto += splited[i]
    print('Decifrado : '+texto+'\n')
    return  texto


arq = open("entrada.txt",'r')
entrada = arq.read()

print('Entrada : '+entrada)
print(entrada)

arq2 = open("chave.txt",'r')
chave = int(arq2.read())

chave = chave%256

print('Key : ',chave)

splited = []
for i in range(0,len(entrada)):
    splited.append(entrada[i])

for i in range(0,len(splited)):
    splited[i] = chr((ord(splited[i]) - chave)%256)

print("Buceta")
texto = ''
for i in range(0,len(splited)):
    texto = texto+splited[i]
print('Decifrado : '+texto+'\n')

arq = ("Encripted.enc","w")
arq.write(texto);
arq.close()







cifrado = cifratexto(entrada,chave)
decifrado = decifratexto(cifrado,chave)

if entrada == decifrado:
    print('O processo de cifragem e decifragem ocorreu perfeitamente!')
else:
    print('Algou deu errado com o processo!')
