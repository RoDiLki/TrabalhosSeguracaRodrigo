__author__ = 'Vostro3550'

NomEnt =  "Entrada.txt"
ChavEnt = "Chave.txt"
NomSai = "Encripted.enc"


EntArq = open(NomEnt,"r")
Entrada = EntArq.read()
print("Entrada Lida!")
EntArq.close()

EntCha = open(ChavEnt,"r")
Chave = EntCha.read()
chave = int(chave)%256
print("Chave Lida!")
EntCha.close()

SaiArq = open(NomSai,"w")

splited =[]
for i in range(0,len(Entrada)):
    splited.append(Entrada[i])

encript =''
for i in range(0,len(splited)):
    splited[i] = chr((ord(splited[i]) + chave)%256)
    encript += splited[i]

encript = bytes(encript)

SaiArq.write(encript)
SaiArq.close()

