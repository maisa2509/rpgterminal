#Exericicos

loja_comidas ={
    'laranja baiana':{
        'valor': 4.00,
    },
    'maca verde':{
        'valor': 5.00,
    },
    'coco verde':{
        'valor': 2.00,
    },
}

for k,v in loja_comidas.items():
  loja_comidas.get(k)['valor']*1.2
print(loja_comidas)

loja_comidas.update({'Mexerica': 4.00})
print(loja_comidas,'#Mexirica adicionada')

for chave, valor in loja_comidas.items():
  print(f"key:{chave}: value:'{valor}")

loja_comidas.pop('maca verde')
print(loja_comidas, '#Maca verde removida')