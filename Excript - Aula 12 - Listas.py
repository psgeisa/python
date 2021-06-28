"""
#apenas percorrendo a lista
lista_nums = [100, 200, 300, 400]
for item in lista_nums:
print(item)

"""

#operando com índice
lista_nums = [100, 200, 300, 400]
lista_indice = [0, 1, 2, 3]
for item in lista_indice:
    lista_nums[item] += 1000
print(lista_nums)

#operando com range
lista_nums = [100, 200, 300, 400]
for item in range(0, 4):
    lista_nums[item] += 1000
print(lista_nums)

#simplificando o range
lista_nums = [100, 200, 300, 400, 600]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)

#operando com enumerate
lista_nums = [100, 200, 300, 400, 600]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
