dici_1 = {}
dici_1['nome'] = 'Maria'
dici_1['idade'] = 50
dici_1['peso'] = 80
dici_1['altura'] = 1.70
dici_2 = {'nome': 'Maria', 'idade': 50, 'peso': 80, 'altura': 1.70}
dici_3 = dict([('nome', 'Maria'), ('idade', 20), ('peso', 80), ('altura', 1.70)])
dici_4 = dict(zip(['nome', 'idade', 'peso', 'altura'] , ['Maria', 50, 80, 1.70]))
print(dici_1 == dici_2 == dici_3 == dici_4)
print(dici_1)