nomecompleto = " taiana maiser "
nomecompleto = nomecompleto.strip()
print(nomecompleto)
print(f'nome limpo: {nomecompleto.strip()}')
nomecompleto = nomecompleto.replace('maiser' , 'silva')
print(nomecompleto)
procurar = nomecompleto.find ('a')
print(procurar)
comeca = nomecompleto.startswith('t')
termina = nomecompleto.endswith('p')
print(f'começa com t?{comeca}')
print(f'termina com p?{termina}')
compras = ['arroz' , 'chocalate' , 'cafe' , 'bolacha' , 'leite' , 'batata' , 'pepino' , 'chuchu']
print(compras)
print(compras[0])
print(compras[1])
print(compras[2])
print(compras[3])
print(compras[4])
print(compras[5])
print(compras[6])
print(compras[7])
def soma(a , b):
    soma = a + b
    return soma

    







