# Online Python - IDE, Editor, Compiler, Interpreter

nome = input("digite seu nome")
print('ola' +str(nome), 'seja bem vindo')

nota_1 = float(input("digite a primera nota"))
nota_2 = float(input("digite a segunda nota"))
nota_3 = float(input("digite a terceira nota"))
media = (nota_1+nota_2+nota_3) / 3
print ('a media da nota entre {:.1f} , {:.1f} e {:.1f} é {:.1f}.'.format(nota_1, nota_2, nota_3, media ))
print(media)
arredondamento = round(media)
if arredondamento >= 9.0 and arredondamento <= 10:
    print('A, parabens, voce foi aprovado')
elif arredondamento < 9.0 and arredondamento >= 7.5:
    print('B, parabens, voce foi aprovado')
elif arredondamento < 7.5 and arredondamento >= 6.0:
    print('C, parabens, voce foi aprovado')
elif arredondamento < 6.0 and arredondamento >= 4.0:
    print('D, voce foi reprovado')
else:
    print('E, voce foi reprovado')

print(f'a sua média final foi {arredondamento:,.2f}')