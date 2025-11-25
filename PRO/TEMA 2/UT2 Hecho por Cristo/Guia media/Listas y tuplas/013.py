matriz = []
suma_columnas = 0
suma_filas = 0
diagonal_sec = 0
diagonal_ppal = 0

orden = int(input("Escriba un orden para crear una matriz cuadrada: "))

#CREACION DE LA MATRIZ DE ORDEN AxA - MATRIZ CUADRADA
for i in range(orden):
    fila = []
    for j in range(orden):
        posicion = int(input(f"Escriba un nº para la posición {i+1},{j+1} > "))
        fila.append(posicion)
    matriz.append(fila)
#CHIVATO PARA SABER QUE SE CREA LA MATRIZ
print("Matriz creada:", matriz)

# CÁLCULO DE LA CONSTANTE MÁGICA (CM)
CONSTANTE_MAGICA = (orden * (orden ** 2 + 1)) // 2
print(f"Constante mágica: {CONSTANTE_MAGICA}")

# SUMA DE LA MATRIZ - por filas.
for i in range(orden):
    suma_filas += sum(matriz[i])

# SUMA DE LA MATRIZ - por columnas.
for i in range(orden):
    suma_columnas += sum(matriz[j][i] for j in range(orden))

# SUMA DE LAS DIAGONALES DE LA MATRIZ - DIAGONAL PPAL
for i in range(orden):
    diagonal_ppal += matriz[i][i]

# SUMA DE LA DIAGONAL SECUNDARIA
for i in range(orden):
    diagonal_sec += matriz[i][orden - i - 1]

# COMPROBACIÓN FINAL SI LA MATRIZ DE ORDEN X ES MÁGICA
if suma_filas//orden == CONSTANTE_MAGICA and suma_columnas//orden == CONSTANTE_MAGICA and diagonal_ppal == CONSTANTE_MAGICA and diagonal_sec == CONSTANTE_MAGICA:
    print(f"La matriz cuadrada de orden {orden}x{orden}\n> {matriz} \nes mágica ya que la suma de sus filas, columnas y diagonales da cada una {CONSTANTE_MAGICA}")
else:
    print("No es mágica")