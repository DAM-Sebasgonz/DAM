# Lectura de valores para n = 3

cuadrado = []

for i in range (3):
    fila = []
    for j in range (3):
        valor = int(input(f"valor de la posicion {i}, {j} "))
        fila.append(valor)
    cuadrado.append(fila)

print(*cuadrado, sep="\n")

for fila in cuadrado:
    if sum(fila) != 15:
        print("El cuadrado no es magico")
        exit(0)


for pos_col in range(3):
    if cuadrado [0][pos_col] + cuadrado[1][pos_col] + cuadrado [2][pos_col] != 15:
        print("El cuadrado no es magico")
        exit(0)

if cuadrado [0][0] + cuadrado[1][1] + cuadrado[2][2] != 15:
    print("El cuadrado no es magico")
    exit(0)

if cuadrado [0][2] + cuadrado[1][1] + cuadrado[2][0] != 15:
    print("El cuadrado no es magico")
    exit(0)