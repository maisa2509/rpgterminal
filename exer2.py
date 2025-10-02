loja_carro ={
    'fiat':{
        'preco':26000,
        'cor':'rosa'
    },
    'corsa':{
        'preco':30000,
        'cor':'verde'
    },
    'celta':{
        'preco':50000,
        'cor':'roxo'
    }
  }

# função items: método de leitura de um dicionário,
#que separa key e value do mesmo.
for k,v in loja_carro.items():
    loja_carro.get(k)['preco']*=1.15
    print(loja_carro)

#função get: método usado para acessar o valor do dicionário ->
preco_fiat = loja_carro.get('fiat',{})
print('Fiat:',preco_fiat)

#função update: método usado para atualizar os valores do dicionário
loja_carro.update({'fiat': 10.90,'corsa':10})
print(loja_carro,'#corsa adicionado')

# função pop: método para remover uma chave
#específica de um dicionário e retornar
#o valor associado a ela.
loja_carro.pop('corsa')
print(loja_carro,'#corsa removido')