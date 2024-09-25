times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'First 5 times is {times[0:5]}')
print(f'Last 5 teams is {times[-4:]}')
print(f'Alphabetic order {sorted(times)}')
print(f'Chapecoense is in {times.index("Chapecoense")+1} position')