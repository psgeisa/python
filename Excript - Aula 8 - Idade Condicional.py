'''
idade = int(input("Digite sua idade: "))

if (idade<=0):
    print("Não pode ser!")
else:
    if (idade>150):
        print("Ta brincando?!")
    else:
        if (idade<18):
            print("Você precisa ser maior de 18")
        else:
            print("ok")
#OU

idade = int(input("Digite sua idade: "))

if (idade<=0):
    print("Não pode ser!")
elif (idade>150):
     print("Ta brincando?!")
elif (idade<18):
     print("Você precisa ser maior de 18")
else:
     print("ok")
'''

num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))

#operadores
if (num1 == num2): #operador de igualdade
    print("o numero %d é igual a %d. " %(num1,num2))
if (num1 != num2): #operador de diferença
    print("o numero %d é diferente de %d. " %(num1,num2))
if (num1 < num2): #operador comparativo menor
    print("o numero %d é menor que %d. " %(num1,num2))
if (num1 > num2): #operador comparativo maior
    print("o numero %d é maior que %d. " %(num1,num2))
if (num1 >= num2): #operador comparativo maior ou igual
    print("o numero %d é maior ou igual a %d. " %(num1,num2))
if (num1 <= num2): #operador comparativo menor ou igual
    print("o numero %d é menor ou igual a %d. " %(num1,num2))
