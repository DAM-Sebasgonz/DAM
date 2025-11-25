'''
Una matriz cuadrada en matemática es una agrupación de números como la siguiente: 
Se pueden representar con listas de la siguiente forma: 
listaA = [ [1, 0], [1, 2] ] listaA = [ [-6, 1], [2, 1] ] 
listaA = [ [1, 0, 1], [0, 1, 0], [1, 0, 1] ] listaA = [ [1, 4, 6], [4, 2, 5], [6, 5, 3] ] 
listaA = [ [1, 5, 0, 1], [2, 8, 3, 2], [0, 4, 2, 0], [1, 0, 0, 1] ] 
listaA = [ [0, 1, 1, 0], [-1, 0, 4, 0], [0, 4, 8, 0], [-9, 2, 1, 8] ] 

Cada una de esas matrices tiene 2 diagonales: 

Escriba un programa en Python que calcule la suma de los elementos de cada una de las 
diagonales de una matriz. 
Los datos de entrada serán: 
Un número (n) que indica el orden de la matriz (número de filas y columnas que tiene) 
Los n al cuadrado elementos de la matriz. 
Luego se debe mostrar como resultado la suma de los elementos de la diagonal principal y la 
suma de los elementos de la diagonal secundaria.
 
Un ejemplo: 
La salida que debe mostrar el programa es: 
La matriz cuadrada que se ha leído: 
1 2 0 
3 1 4 
3 0 1 
La suma de los elementos de la diagonal principal es 3 
La suma de los elementos de la diagonal secundaria es 4 
Otro ejemplo 
La matriz cuadrada que se ha leído: 
8 7 5 
3 2 0 
1 4 6 
La suma de los elementos de la diagonal principal es 16 
La suma de los elementos de la diagonal secundaria es 8 '''
#1º parte: Generación de la matriz cuadrada por orden n.
matriz=[]
n=int(input("Escriba el orden de la matriz: "))
for i in range(n):
    fila = []  # Cada fila de la matriz / agregamos aqui los elementos de la nueva lista.
    for j in range(n): 
        num = input(f"Escriba un número para la posición ({i+1},{j+1}): ")
        fila.append(num)  # Agregar el número a la fila
    matriz.append(fila)  # Agregar la fila completa a la matriz
print("La matriz que se ha leído es:")
for i in range(n):
    print(" ".join(matriz[i]))  # Convertir cada fila en una cadena separada por espacios
#calcular la suma de los elementos de la diagonal principal:
suma_diagonal_principal=0
suma_diagonal_secundaria=0
for i in range(n):
    suma_diagonal_principal+=int(matriz[i][i])
for i in range(n):
    suma_diagonal_secundaria+=int(matriz[i][n-i-1])
print(f"La suma de la diagonal principal de la matriz es: {suma_diagonal_principal}")
print(f"La suma de la diagonal secundaria de la matriz es es: {suma_diagonal_secundaria}")
#MEJORAR EL PROGRAMA A QUE SUME FILAS Y COLUMNAS PARA QUE DE EL TOTAL DE CADA COSA:
suma_filas=0
suma_columnas=0
for i in range(n):
    for j in range(n):
        suma_filas+=int(matriz[i][j])
print(f"La suma de las filas dan: {suma_filas}")
for i in range(n):
    for j in range(n):
        suma_columnas+=int(matriz[j][i])
print(f"La suma de las columnas dan: {suma_columnas}")