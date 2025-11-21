numero_filas = int(input("Ingrese el numero de filas que sea tener: "))

for i in range(numero_filas, 0, -1):  
    for j in range(1, i + 1):
        print(j, end=" ") 
    print() 
