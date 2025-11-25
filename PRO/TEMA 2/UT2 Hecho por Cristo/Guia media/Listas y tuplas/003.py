'''Ejercicio 03: - Modificar el programa anterior para los datos de las listas se ingresen por 
teclado.'''
matriz=[]
for elto in range (3):
    fila=[]
    for elemento in range(3):
        elemento=int(input(f"Añade un elemento {elemento+1} para la fila {elto+1}: "))
        fila.append(elemento)
    matriz.append(fila)
suma_columnas=0
#para la suma de las filas:
for i in range(3):  # Cambié el rango a 3 porque hay 3 filas /reinicia con la iteración 4 y 8
    suma_filas = 0
    for j in range(3):  # También cambié este rango a 3 porque hay 3 columnas
        suma_filas += matriz[i][j]
    print(f"Suma de la fila {i + 1}: {suma_filas}")
for i in range(3):
    suma_columnas=0
    for j in range(3):
        suma_columnas+=matriz[j][i]
    print(f"Suma de la columna {i + 1}: {suma_columnas}")
