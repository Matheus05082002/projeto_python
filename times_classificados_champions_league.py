times_italia = ['Milan', 'Inter de Milão', 'Juventus', 'Roma', 'Lazio', 'Bologna', 'Atalanta', 'Napoli']
classificados_italia = ['Juventus', 'Milan', 'Inter de Milão', 'Napoli', 'Roma']
nao_classificados_italia =  [italia for italia in times_italia if italia not in classificados_italia]
for equipe_italia in nao_classificados_italia:
    print(equipe_italia)
times_inglaterra = ['manchester city', 'manchester united', 'liverpool', 'everton', 'tottenham', 'arsenal', 'chelsea', 'wolves', 'aston villa']
classificados_inglaterra = ['arsenal', 'manchester city', 'chelsea', 'liverpool']
nao_classificados_inglaterra = [inglaterra for inglaterra in times_inglaterra if inglaterra not in classificados_inglaterra]
for equipe_inglaterra in nao_classificados_inglaterra:
    print(equipe_inglaterra)
times_franca = ['psg', 'lens', 'olympique marseille', 'lyon', 'lille', 'monaco', 'rennes']
classificados_franca = ['monaco', 'psg', 'lyon', 'lens']
nao_classificados_franca = [franca for franca in times_franca if franca not in classificados_franca]
for equipe_franca in nao_classificados_franca:
    print(equipe_franca)
times_alemanha = ['bayer leverkusen', 'bayer de munique', 'borussia dortmund', 'stuttgart', 'eintracht frankfurt', 'wolfsburg', 'schalke 04']
classificados_alemanha = ['bayer de munique', 'borussia dortmund', 'stuttgart', 'bayer leverkusen']
nao_classificados_alemanha = [alemanha for alemanha in times_alemanha if alemanha not in classificados_alemanha]
for equipe_alemanha in nao_classificados_alemanha:
    print(equipe_alemanha)
times_espanha = ['barcelona', 'real madrid', 'girona', 'vilarreal', 'atletico de madrid', 'valencia']
classificados_espanha = ['barcelona', 'real madrid', 'girona', 'atletico de madrid']
nao_classificados_espanha = [espanha for espanha in times_espanha if espanha not in classificados_espanha]
for equipe_espanha in nao_classificados_espanha:
    print(equipe_espanha)
    

