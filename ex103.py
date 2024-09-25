def ficha(nome='desconhecido', gols=0):
    print(f'Player {nome} have score {gols} in the championship ')


name = str(input('Player name: ')).strip().upper()
gol = str(input('How many gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if name.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome=name, gols=gol)
