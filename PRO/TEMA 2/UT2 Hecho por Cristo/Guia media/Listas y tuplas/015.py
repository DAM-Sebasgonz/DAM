'''Una matriz cuadrada se dice en “espejo” cuando la matriz y su transpuesta 
son iguales.  
 
La matriz de abajo es “en espejo” 
 
1 4 5 
4 2 6 
5 6 3 
 
Y esta no lo es: 
1 4 5 
4 2 7 
8 6 3'''
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

if matriz==matriz_transpuesta:
    print("Son espejos.")
else:
    print("No son espejos")
