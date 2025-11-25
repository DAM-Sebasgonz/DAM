'''Se quiere modificar el programa anterior de tal forma que además de sumar 
matrices  el  problema  pueda  restarlas  (A  –  B).  La  resta  de  matrices  tiene  las  mismas 
restricciones  que  la  suma  y  los  elementos  del  resultado  se  obtienen  restando  a  los 
elemento de la matriz A los de la matriz B. 
 
El programa debe ampliarse para que al comenzar a ejecutarse contemple el siguiente 
menú:  
 
1. Leer A 
2. Leer B 
3. Verificar que A y B son compatibles  
4. A + B 
5. A - B 
9. Salir 
'''            
MATRIZ_A=[]
MATRIZ_B=[]
while True:
    try:
        seleccion=int(input("Haga una selección entre:\n1- Leer A\n2- Leer B\n3- Verificar que A y B son compatibles\n4- A+B\n5- A-B\n9- Salir\n Elección > "))
    except:
        print("No se permiten caracteres literales.")
    else:
        match seleccion:
            case 1:
                n_filas_a=int(input("Escribe un nº de filas para generar la matriz A: "))
                n_columnas_a=int(input("Escribe un nº de columnas para la matriz A: "))
                for i in range(n_filas_a):
                    filas_a=[]
                    for j in range(n_columnas_a):
                        num=int(input(f"Escriba un nº para la casilla > {i+1},{j+1} de la matriz A: "))
                        filas_a.append(num)
                    MATRIZ_A.append(filas_a)
            case 2:
                n_filas_b=int(input("Escribe un nº de filas para generar la matriz B: "))
                n_columnas_b=int(input("Escribe un nº de columnas para la matriz B: "))
                for i in range(n_filas_b):
                    filas_b=[]
                    for j in range(n_columnas_b):
                        num=int(input(f"Escriba un nº para la casilla >{i+1},{j+1} de la matriz B: "))
                        filas_b.append(num)
                    MATRIZ_B.append(filas_b)
            case 3:
                if len(MATRIZ_A)==len(MATRIZ_B):
                    compatibles=True
                    for i in range(len(MATRIZ_A)):
                        if len(MATRIZ_A[i])!=len(MATRIZ_B[i]): #fragmento para comparar columnas
                            compatibles=False
                            break
                    if compatibles:
                        print(f"Las matrices A y B son compatibles entre si.")
                    else:
                        print("Las matrices no son compatibles: diferentes columnas en al menos una fila.")
                else:
                    print("Las matrices no son compatibles: diferente número de filas.")  
            case 4:
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
            case 5:
                print(f"Calculando suma...")
                matriz_resta = []
                for i in range(len(MATRIZ_A)):
                    fila_resta = [] #creamos la nueva matriz_resta resultado de la resta de AB
                    for j in range(len(MATRIZ_B)):
                        fila_resta.append(MATRIZ_A[i][j] - MATRIZ_B[i][j]) #Usando una de las longitudes, nos movemos por i j y restamos
                    matriz_resta.append(fila_resta)
                print(f"La nueva matriz RESTA > ")
                for fila in matriz_resta:
                    print(" ".join(map(str, fila)))  
            case 9:
                print("Saliendo.")
                exit()
            case _:
                print("Error. Continue nuevamente introduciendo un nº válido.")
                continue