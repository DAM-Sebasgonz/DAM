'''La transpuesta de una matriz es la matriz a la que obtiene al cambiar las 
filas por columnas y viceversa de la matriz original. 
 
Veamos un ejemplo: 
 
Si la matriz A es:    1 2 3 
                      4 5 6 
 
La transpuesta de la matriz A es: 
  1 4 
  2 5 
  3 6 
 
Realice  un  programa  que  lea  una  matriz,  calcule  su  transpuesta  y  muestre  ambas  por 
pantalla.'''
matriz = []
matriz_transpuesta=[]

orden_filas = int(input("Escriba un orden de filas para crear una matriz: "))
orden_columnas=int(input("Escriba un orden de columnas para crear una matriz: "))

# Creamos la matriz de orden x orden
for i in range(orden_filas):
    fila = []
    for j in range(orden_columnas):
        posicion = int(input(f"Escriba un nº para la posición {i+1},{j+1} > "))
        fila.append(posicion)
    matriz.append(fila)
for j in range(orden_columnas):
    fila_transpuesta=[]
    for i in range(orden_filas):
        fila_transpuesta.append(matriz[i][j])
    matriz_transpuesta.append(fila_transpuesta)

print(f"Matriz original:\n" + "\n".join([" ".join(map(str, fila)) for fila in matriz]))
print(f"Matriz transpuesta:\n" + "\n".join([" ".join(map(str, fila)) for fila in matriz_transpuesta]))
