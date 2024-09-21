precos_em_euros = [200, 300, 400]
taxa_de_cambio = 6.0
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_euros))
print(precos_em_reais)
print('os precos em reais são' +str(precos_em_reais))


