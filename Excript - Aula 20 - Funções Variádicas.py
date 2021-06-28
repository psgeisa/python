"""
numeros_favoritos = {"pietro":[18,9], "katia":[7,14], "tiago":[6,4]}
for pessoa, numeros in numeros_favoritos.items():
    print("O número favorito de", pessoa.title(),"é:", numeros)

O interpretador do py utiliza o "+" acompanhado de "str" para alguns casos específicos...
tipo "print(texto + str(numero))" então ele transforma tudo que está dentro do parâmetro
em "string" pra poder executar o print

"""
numeros_favoritos = {'pietro': [18, 9], 'katia': [7, 14], 'tiago': [6, 4]}
for pessoa, numeros in numeros_favoritos.items():
    print("O número favorito de", pessoa.title(), " é " , numeros)
