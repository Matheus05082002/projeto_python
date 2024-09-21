convidados = ['Matheus', 'Paulo', 'Ana Paula', 'Marcos', 'Hugo', 'Deise', 'Brenda', 'Lucas']
confirmados = ['Matheus', 'Deise', 'Marcos', 'Hugo']
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
for pessoa in nao_confirmados:
    print(pessoa)