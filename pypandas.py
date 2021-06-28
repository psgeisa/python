import pandas as pd

# ler arquivo inteiro
x = pd.read_excel(r'caminhoderede\cartas_mensais.xlsx')

# imprimir arquivo inteiro
print(x)

# imprimir determinada coluna
print(x['Criado'])

# imprimir determinado elemento
print(x['Criado'][3])

# criar arquivo
d = {
    'Nomes': ['Ana', 'Julia', 'Pedro'], # colA
    'Idade': ['27', '28', '30'], # colB
    'Altura': ['1.60', '1.90', '1.85'] # colC   
    }
dados = pd.DataFrame(data=d)
print(dados)

# gerando arquivo excel
dados.to_excel('dados.xlsx', index = False)
