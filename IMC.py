
# Online Python - IDE, Editor, Compiler, Interpreter

nome = input('digite seu nome')
print('olá'+str(nome),'seja bem vindo')

peso = float(input('digite seu peso'))
altura = float(input('digite sua altura'))
IMC = peso / (altura ** 2)
arredondamento = round(IMC)
print(f'{arredondamento:,.2f}')
if IMC < 18.5:
    print('baixo peso')
elif IMC >= 18.5 and IMC < 25:
    print('peso normal')
elif IMC >= 25 and IMC < 30:
    print('sobrepeso')
else:
    print('obesidade')
    
print(f'o seu indice de massa corporal é {arredondamento:,.2f}')