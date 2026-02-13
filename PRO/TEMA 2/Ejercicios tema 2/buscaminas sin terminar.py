import random

# Esto es la cantidad de filas y de la mierda esa de columnas
fil = 8
col = 8
numbomba = 10

print("=" * 50) 
print("BUSCAMINAS - Tablero") #esto lo vi en tiktok y quedo bien jajaja
print("=" * 50)

# tablero vacío de 8x8
tablero = [[0 for _ in range(col)] for _ in range(fil)]

print("\nBombas colocadas en el tablero:")

bombas_colocadas = 0

while bombas_colocadas <= numbomba:
    # Que la esto seae aleatoria
    fila = random.randint(0, fil - 1)
    columna = random.randint(0, col - 1)
    
    # el esto coloca bombas en el tablero si no hay una bomba ya
    if tablero[fila][columna] != 'B':
        tablero[fila][columna] = 'B'
        bombas_colocadas += 1
