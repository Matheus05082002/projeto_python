
# Online Python - IDE, Editor, Compiler, Interpreter

salario = float(input("digite seu salario"))

if salario <= 280:
    porcentagem = salario * 20 / 100
    salarionovo = salario + porcentagem
elif salario > 280 and salario <= 700:
    porcentagem = salario * 15 / 100
    salarionovo = salario + porcentagem
elif salario > 700 and salario <= 1500:
    porcentagem = salario * 10 / 100
    salarionovo = salario + porcentagem
else:
    porcentagem = salario * 5 / 100
    salarionovo = salario + porcentagem
    
arredondamento = round(salarionovo)
print('o valor acrescentado no seu salario foi' +str(porcentagem))
print(f'o seu salario novo é {arredondamento:,.2f}')