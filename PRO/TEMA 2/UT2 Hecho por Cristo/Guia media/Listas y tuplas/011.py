'''Se quiere realizar un programa que sume dos matrices. La matriz resultante 
de la suma de dos matrices se realiza sumando elemento por elemento y asignándolo a la 
misma posición.  
 
Veamos un ejemplo: 
 
A = [ [2, 3], [1, 0] ]  y  B =  [ [8 , 7], [-7, 4] ]  el resultado de la suma de A + B = [ [10 , 
10], [-6, 4] ] 
 
Se tiene que tener en cuenta que las matrices A y B deben coincidir en numero de filas y 
deben coincidir en número de columnas, por ejemplo: 
 
A = [ [2, 3], [1, 0], [-2, 5] ]  y  B =  [ [8 , 7], [-7, 4], [6, 9] ]  la suma de A + B = [ [10 , 
10], [-6, 4], [4, 14] ] 
 
Las matrices A y B se leen por teclado, para ello, se debe pedir primero el número de filas 
y de columnas de cada matriz, se debe verificar que se puede realizar la suma.  
 
En caso de que no se pueda realizar la suma se indica mensaje y se aborta el programa. 
 
Si se puede realizar se debe mostrar de la siguiente forma: 
 
 1 2    3 4   4   6 
-1 8    6 3   7  11 
 
Recuerden como hacer la escritura en columnas, explicado en un ejercicio en clase: '''
MATRIZ_A=[]
MATRIZ_B=[]
filas_a=[]
filas_b=[]
n_filas_a=int(input("Escribe un nº de filas para generar la matriz A: "))
n_columnas_a=int(input("Escribe un nº de columnas para la matriz A: "))
n_filas_b=int(input("Escribe un nº de filas para generar la matriz B: "))
n_columnas_b=int(input("Escribe un nº de columnas para la matriz B: "))
#para la generación de las filas y columnas de la matriz A - Formación de la matriz A.
for i in range(n_filas_a):
    filas_a=[]
    for j in range(n_columnas_a):
        num=int(input(f"Escriba un nº para la casilla > {i+1},{j+1} de la matriz A: "))
        filas_a.append(num)
    MATRIZ_A.append(filas_a)
#para la generación de las filas y columnas de la matriz B - Formación de la matriz B.
for i in range(n_filas_b):
    filas_b=[]
    for j in range(n_columnas_b):
        num=int(input(f"Escriba un nº para la casilla >{i+1},{j+1} de la matriz B: "))
        filas_b.append(num)
    MATRIZ_B.append(filas_b)
print(f"Las matrices resultantes: \nMatriz A > {MATRIZ_A}\nMatriz B > {MATRIZ_B}")
#para verificar si se pueden sumar, hay que preguntarnos si la matriz A tiene el mismo tamaño
#que la matriz B. Dicho de otra manera, si el nº de filas y columnas de A son IGUALES a las de B.
if n_filas_a==n_columnas_b and n_columnas_a==n_columnas_b:
    print(f"Las matrices A y B se pueden sumar ya que son del mismo orden.\nOrden Matriz A > {n_filas_a}x{n_columnas_a} | Orden Matriz B > {n_filas_b}x{n_columnas_b}")
    print(f"Calculando suma...")
    matriz_suma = []
    for i in range(len(MATRIZ_A)):
        fila_suma = [] #creamos la nueva matriz_suma resultado de la suma de AB
        for j in range(len(MATRIZ_B)):
            fila_suma.append(MATRIZ_A[i][j] + MATRIZ_B[i][j]) #Usando una de las longitudes, nos movemos por i j y sumamos
        matriz_suma.append(fila_suma)
    print(f"La nueva matriz SUMA > ")
    for fila in matriz_suma:
        print(" ".join(map(str, fila)))
else:
    print(f"Las matrices A y B no se pueden sumar ya que no tienen el mismo orden.\nOrden Matriz A > {n_filas_a}x{n_columnas_a} | Orden Matriz B > {n_filas_b}x{n_columnas_b}")
    exit()