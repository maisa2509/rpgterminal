loja_fruta = {
    'melancia':3.00,
    'pitaya': 14.00,
    'mandioca': 4.00,
}
#função get: método usado para acessar o valor do dicionário ->
preco_uva = loja_fruta.get('uva',{})
print('Uva:',preco_uva)

#função update: método usado para atualizar os valores do dicionário
loja_fruta.update({'uva': 8.90,'tomate':10})
print(loja_fruta,'#tomate adicionado')

# função pop: método para remover uma chave
#específica de um dicionário e retornar
#o valor associado a ela.
loja_fruta.pop('tomate')
print(loja_fruta,'#tomate removido')

# função items: método de leitura de um dicionário,
#que separa key e value do mesmo.