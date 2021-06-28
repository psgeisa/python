
"""
a = 10
b = 25
c = 66
x = int(input("digite um numero:" ))

if(x == a or x == b or x == c):
    print("o numero está contido nos meus parâmetros")
else:
    print("o numero não está contido nos meus parâmetros")

#ou

if(x in [a, b, c]):
    print("o numero está contido nos meus parâmetros")
else:
    print("o numero não está contido nos meus parâmetros")
"""
cores = ["azul", "amarelo", "vermelho", "branco"]

#Loop
while True: #Loop infinito, leia "enquanto verdade foi verdadeira..."
    cor = input("Digite o nome de uma cor, "
                  "ou ZERO para sair do programa: ")
    if(cor=="0"):
        break
    #Verificando se a cor digitada está na lista
    elif cor in cores:
        print("essa cor está na lista")
    else:
        print("essa cor não está na lista")
