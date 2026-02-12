# juego de números

from random import randint

while True:
    valor_a_adivinar = randint(-50, 50)
    if valor_a_adivinar != 0:
        break

turno = 'MJ'
pos_turno = randint(0, 1)

while valor_a_adivinar != 0:
    print(f'Valor actual = {valor_a_adivinar}')
    print(f'Turno {'de la Máquina' if turno[pos_turno] == 'M' else 'del Jugador'} -->', end = ' ')
    if turno[pos_turno] == 'M':
        jugada = randint(1,10)
        print(f'{jugada}')
    else:
        jugada = int(input())

    if valor_a_adivinar < 0:
        valor_a_adivinar += jugada
    elif valor_a_adivinar > 0:
        valor_a_adivinar -= jugada

    if valor_a_adivinar:
        pos_turno = (pos_turno + 1) % 2
        
print(f'El ganador es {'la Máquina' if turno[pos_turno] == 'M' else 'el Jugador'}')