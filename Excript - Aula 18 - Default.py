"""
def login(usuario="root", senha="123"):
    print("Usuario: ", usuario)
    print("Senha: ", senha)
login()
"""
#Parâmetros posicionais
def dados_pessoais (nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome, sobrenome, idade, sexo))
dados_pessoais("Claudio", "Rogerio", 30, True)

#Parâmetros nomeados
dados_pessoais(sobrenome="Silva", nome="Claudio", sexo=True, idade=30 )

