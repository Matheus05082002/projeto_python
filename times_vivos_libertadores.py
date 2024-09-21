times = set()
times.add('palmeiras')
times.add('flamengo')
times.add('fortaleza')
times.add('sao paulo')
times.add('fluminense')
times.add('atletico mineiro')
times.add('gremio')
times.add('botafogo')
print('os times brasileiros na libertadores são:', times)
times.remove('palmeiras')
times.remove('fortaleza')
times.remove('gremio')
elemento = 'palmeiras'
if elemento in times:
    print(f'o {elemento} está na libertadores')
else:
    print(f'o {elemento} não está na libertadores')

