times = ['Palmeiras', 'Corinthians', 'São Paulo', 'Santos', 'Flamengo']
print("antes da listcomp =", times)
times = [item.lower() for item in times]
print("depois da listcomp =", times)