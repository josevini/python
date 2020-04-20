tabela = ('Atlético-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo',
          'Ceará SC', 'Corinthinas', 'Coritiba', 'Flamengo', 'Fluminense',
          'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
          'Bragantino-SP', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco da Gama')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 15)
print(f'Os 5 primerios são {tabela[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {tabela[16:20]}')
print('-=' * 15)
time = 'sAnToS'.capitalize()
pos = tabela.index(time) + 1
print(f'O {time} está na {pos}ª posição')
