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
