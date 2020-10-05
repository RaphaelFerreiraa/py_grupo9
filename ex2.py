time = input('digite o nome do time:')
vitorias = int(input('digite as vitorias do time:'))
derrotas = int(input('digite as derrotas do time:'))
empates =int(input('digite os empates desse time:'))
jogos = vitorias+derrotas+empates
pontos_ganhos = vitorias *3+empates
print('O time' ,time, 'jogou',jogos,'jogos e obteve' ,pontos_ganhos,'pontos')