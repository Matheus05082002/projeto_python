
# Online Python - IDE, Editor, Compiler, Interpreter

gols = float(input("digite o numero de gols:"))
partidas = float(input("digite o numero de partidas:"))
media = gols / partidas
print(media)
if media >= 0.4:
    print('craque')
elif media < 0.4 and media >= 0.2:
    print('jogador mediano')
else:
    print('bagre')
    
print('a media entre {:.1f} e {:.1f} é {:.1f}.'.format(gols, partidas, media))
print('a sua media de gols é:'+str(media))
