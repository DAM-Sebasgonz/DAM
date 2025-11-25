'''Ejercicio 02: Diseñar un programa que calcule e imprima la suma de los números de cada 
una filas de una matriz. Luego debe imprimir las sumas de los elementos por columnas. 
 
La matriz se crea en el código del programa. '''
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
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
