"""
#Exemplo 1
s = "Iterando strings"

for c in s:
    print(c)

#Exemplo 1
s = "Iterando strings"
indice = 0

while indice < len(s):
    print(indice,s[indice]) #valor do índice e carectere respectivo
    indice+=1

"""
#Exemplo 3 - a função enumerate tem como carcterística principal: vincular objeto a numeros int não negativos
for k,v in enumerate("Iterando strings"):
    print(k,v)